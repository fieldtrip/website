---
title: Measuring the timing delay and jitter for a real-time application
tags: [example, realtime]
---

# Measuring the timing delay and jitter for a real-time application

## Timing of a closed loop system

The idea is to make a trigger-echo application. Triggers are sent (e.g., via MATLAB and a serial port) to a trigger channel (e.g., a PPT of the MEG system). Then we can read from that trigger channel (sampled along with the data) and once the trigger is detected, we can either write to another trigger channel, or write to the same channel but use different value for the trigger. The example below was used to measure trigger echo delays in the MEG system at FCDC. I was sending triggers (pulses of height 4), that were then recorded on trigger channel UPPT001. I then read this channel data online from shared memory and did a flank detection -of flanks with height 4- on the fly. Once, the flank was detected, I wrote another pulse (of a different height) on the same channel. The difference between the two flanks (the one sent and the one received) is a measure of the delay in the loop.The data was then saved on disk and the delays between the sent and received triggers were analyzed offline.

    matlab1 --> trig1  --> acquisition  --> buffer --> matlab2 --> trig2
                                ^                                   |
                                |                                   |
                                -------------------------------------

On the trigger sending side, the code looks something like this:

    %% create MATLAB serial object related to the port, where the triggers are to be sent
    %% make sure all instruments/serial objects are closed
    delete(instrfind);
    fclose('all');

    %% open serial port, here we open a serial port,which is directly connected to UPPT001 channel of the MEG system
    %% Creating serial port object now its connected to COM7
    serobjw = serial('/dev/ttyS0');

    %% open it
    fopen(serobjw);

    %% set trigger codes, here we will be sending a 4
    tr=4;
    duration=0.9; %% inter trigger interval

    %% send a bunch of triggers
    for n=1:3000
      fwrite(serobjw,tr);
      pause(duration);
    end

    %% close serial port
    fclose(serobjw);

On the receiving side (the machine, that reads the data online from shared memory), we need to read the appropriate trigger channel, detect incoming triggers and then once a trigger is detected, write a new trigger to the data (in this case this was done by sending a command to serial port that was connnected to PPT1 of the MEG system and recorded on channel UPPT001 with the data).

    %% This is where we are reading the data from from, this, in this case shared memory for the MEG at FCDC
    cfg.headerfile = 'shm://';
    cfg.dataset    = 'shm://';

    % Trigger channel to read from
    cfg.channel = 'UPPT001';

    %% below follows the destination for ft_write_event (i.e. for closing the loop), this in this case is a serial port connected to trigger channel UPPT001 on the MEG ACQ console
    outstream = 'serial:/dev/ttyS0'; %% syntax outstream = 'serial:`<port>`?key1=value1&key2=value2&...';

    % translate dataset into datafile+headerfile
    cfg = ft_checkconfig(cfg, 'dataset2files', 'yes');
    cfg = ft_checkconfig(cfg, 'required', {'datafile' 'headerfile'});

    % start by reading the header from the realtime buffer
    hdr = ft_read_header(cfg.headerfile, 'headerformat', cfg.headerformat, 'cache', true, 'retry', true);
    cfg.blocksize = hdr.nSamples / hdr.Fs; %% the size of one data segment in shared memory, typically ~70 samples


    %% set the default configuration options
    if ~isfield(cfg, 'dataformat'),     cfg.dataformat = [];      end % default is detected automatically
    if ~isfield(cfg, 'headerformat'),   cfg.headerformat = [];    end % default is detected automatically
    if ~isfield(cfg, 'eventformat'),    cfg.eventformat = [];     end % default is detected automatically
    if ~isfield(cfg, 'overlap'),        cfg.overlap = 0;          end % in seconds
    if ~isfield(cfg, 'bufferdata'),     cfg.bufferdata = 'first'; end % first or last
    if ~isfield(cfg, 'readevent'),      cfg.readevent = 'yes';    end % capture events?
    if ~isfield(cfg, 'jumptoeof'),      cfg.jumptoeof = 'yes';    end % jump to end of file at initialization
    if ~isfield(cfg, 'datafile'),       cfg.datafile = 'shm://';  end % input stream

    %% Note: best to start reading from first available sample; i.e. cfg.bufferdata = 'first';

    %% define a subset of channels for reading
    cfg.channel = ft_channelselection(cfg.channel, hdr.label);
    chanindx    = match_str(hdr.label, cfg.channel);
    nchan       = length(chanindx);

    if strcmp(cfg.jumptoeof, 'yes')
      prevSample = hdr.nSamples * hdr.nTrials;
    else
      prevSample  = 0;
    end

    count       = 0;
    % determine the size of blocks to process
    blocksize = round(cfg.blocksize * hdr.Fs);
    overlap   = round(cfg.overlap*hdr.Fs);


    %% as we will be doing flank detection on the fly on short segments, we have to
    %% make sure that the data is padded, such that no triggers go missing
    pad = 0;

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % this is the general BCI loop where realtime incoming data is handled
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    while true

        hdr = ft_read_header(cfg.headerfile, 'headerformat', cfg.headerformat, 'cache', true);

        %% see whether new samples are available
        newsamples = (hdr.nSamples*hdr.nTrials-prevSample);

        if newsamples>=blocksize

            % determine the samples to process

            begsample  = prevSample+1;
            endsample  = prevSample+blocksize ;

            %%         this allows overlapping data segments
            if overlap && (begsample>overlap)
                begsample = begsample - overlap;
                endsample = endsample - overlap;
            end

            %%        remember up to where the data was read
            prevSample  = endsample;
            count       = count + 1;
            fprintf('processing segment %d from sample %d to %d\n', count, begsample, endsample);

            %%         read data segment of trigger channel  from buffer

            dat = ft_read_data(cfg.datafile, 'header', hdr, 'dataformat', cfg.dataformat, 'begsample', begsample, 'endsample', endsample, 'chanindx', chanindx, 'checkboundary', false);
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            %         from here onward it is specific to the method of detecting events
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

                %% differentiate data segment in trigger channel
                diff_dat = diff([pad dat]);
                %% pad the subsequent segment with the end sample of the previous one, prior to differentiation.
                %% As differentiation is done on short segments here, if padding is not done, some flanks can be missed
                pad = dat(end);

                %% detect flanks in UPPT001 that are of certain size (here size 4, corresponding to the ones we are sending)
                smp=find(diff_dat==4);

                if~isempty(smp) %% if there is such an incoming event(in_event)
                    smp = smp + begsample; %% get sample number with respect to the beginning of the recording;
                    %% get it in FieldTrip event format
                    in_event = [];
                    in_event.type   = 'flank';
                    in_event.sample = smp;
                    in_event.value=diff_dat(smp-begsample);
                    %% and display it
                    disp(in_event);

                    %% Once incoming event is detected, create new outcoming event with the same sample number but different value
                    out_event=[];
                    out_event.sample   = event.sample; %% is this correct?
                    out_event.type     = 'flank';
                    out_event.offset   = [];
                    out_event.value    = 16; %% set this to a different value
                    out_event.duration = 1;
                    %% write this event (of size 16) on serial port that goes to the same trigger channel (UPT001)

                    ft_write_event(outstream, out_event);

                end %% if not empty smp
       end % if enough new samples
    end % while true

Once, the data is saved on disk (in a ctf .ds), we can now detect incoming and outgoing triggers.
We could use **[ft_read_event](/reference/fileio/ft_read_event)** to detect the pulses but first we need to make sure , that incoming and outgoing triggers always come in couplets.

We can just plot the trigger channel:

    filename='fullpath_to_dataset.ds'
    cfg.dataset=filename;
    hdr=ft_read_header(cfg.headerfile);
    cfg.channel = ft_channelselection('UPPT001', hdr.label);
    chanindx    = match_str(hdr.label, cfg.channel);
    dat = ft_read_data(cfg.dataset, 'header', hdr, 'chanindx', chanindx);
    %% as the data here was recorded in trials I reshape them back into a continuous time series
    data_r=reshape(dat,[size(dat,1)*size(dat,2),1]);
    figure
    plot(data_r);

This then looks a bit like this figure.

{% include image src="/assets/img/example/measuring_the_timing_delay_and_jitter_for_a_real-time_application/sent_and_received_triggers_head_localization_off.jpg" %}

i.e. a train of couplets comprising a 4 followed by a 16. We can now extract the incoming and detected events;

    %% Read events
    event=ft_read_event(filename);
    %% Filter events that are recorded on the relevant channel
    evt=ft_filter_event(event,'type','UPPT001');

    %% Incoming triggers, remember these were of value 4
    trig_in_buff=ft_filter_event(event,'type','UPPT001','value',4);
    %% Outgoing (detected) triggers, these are of value 16
    trig_out_buff=ft_filter_event(event,'type','UPPT001','value',16);
    %5 convert them to arrays
    for s=1:size(trig_in_buff,1),
        in_sample(s)=trig_in_buff(s).sample;
    end
    for s=1:size(trig_out_buff,1),
        out_sample(s)=trig_out_buff(s).sample;
    end
    %% calculate loop delay in samples
    diff_in_sampl=out_sample-in_sample;


    diff_in_sampl=out_sample-in_sample;

The data I obtained (at a sampling rate of 1200) after sending about 3000 triggers looks like this:

{% include image src="/assets/img/example/measuring_the_timing_delay_and_jitter_for_a_real-time_application/picture_3.png" %}

This is rather consistent with a uniform distribution between 100-250ms

{% include image src="/assets/img/example/measuring_the_timing_delay_and_jitter_for_a_real-time_application/picture_2.png" %}

## Timing of a closed system using the FT buffer to do the online streaming

This is largely similar to the above, but using a different way of accessing the data in realtim

a) Instead of using **AcqBuffer** as a daemon for managing the shared memory, we use **acq2ftx**. This tool basically grabs the data out of the CTF shared memory as soon as **Acq** writes it there, and forwards it to a FieldTrip buffer. It also automatically parses the generated .res4 file, analyses trigger channels, and turns flanks in those trigger channels into FieldTrip buffer events.

b) The MATLAB scripts that read/process the data do **not** access the shared memory anymore, but only the FieldTrip buffer. This allows for a more robust and decoupled operation by avoiding unsynchronized and interfering access to the same resources by multiple processes at the same time. For example, for determining whether there are new samples and/or events, we do not rely on `ft_read_header_shm` anymore, but can use `ft_poll_buffer` (or but also `ft_read_header` for reading the complete header information including the `.res4` file).

This is how we tested the timing of this system on the CTF275 system at the FCDC:

1) In a console we start the streaming of the data with `acq2ft`

   acq2ftx -:1972:GER:1:\*

This means set up a buffer on the localhost (or other machine, whose name needs to be specified instead of the - sign) on port 1972, and stream both data and events. The three flags GER stand for: G) apply gains E) send events R) transmit extended header information (.res4). In this example, we do not downsample (1) and stream all channels (\*).

2) We now start the MEG data acquisition, on Acq.

3) Again using a separate MATLAB session we repeatedly send trigger codes of value 4 to a serial port, which -after serial to parallel conversion- in this case was connected the the MEG console via Parallel Port 1. The triggers then get recorded on disk (channel UPPT01).

    clear all;
    close all;
    delete(instrfind);
    fclose('all');
    %% open serial port
    serobjw = serial('/dev/ttyS0');        % Creating serial port object now its connected to COM7
    serobjw.Baudrate = 115200;             % Set the baud rate at the specific value
    set(serobjw, 'Parity', 'none');        % Set parity as none
    set(serobjw, 'Databits', 8);           % set the number of data bits
    set(serobjw, 'StopBits', 1);           % set number of stop bits as 1
    set(serobjw, 'Terminator', '');        % set the terminator value to newline
    set(serobjw, 'OutputBufferSize', 512); % Buffer for write operation, default it is 512
    get(serobjw) ;
    fopen(serobjw);

    % outstream = 'serial:/dev/ttyS0';
    pause(5)

    %% set trigger codes
    tr=4;
    duration=0.2;
    rand_offset=.1;
    tic;
    t_read=zeros(200,1);
    for n=1:200
      fwrite(serobjw,tr);
      %out_event.value=4;
      %write_event(outstream, out_event);

      t_read(n)=toc;

      %pause(duration + rand_offset*rand);
      pause(duration+ rand_offset);
      disp(n)
    end

4) Now using a different MATLAB session we access the FT buffer on the localhost:

   cfg = [];
   cfg.headerfile = 'buffer://localhost:1972';
   cfg.dataset = 'buffer://localhost:1972';

We now want to read the STIM REF channel at which the trigger arrives (UPPT001) and then send an echo (a trigger of different value) to the same channel, so we can subsequently calculate the delay from the recorded data.

    %% this is the channel that we will be reading from
    cfg.channel = 'UPPT001';

    %% The destination for writing the echo trigger, this is a serial port that ultimately also gets recorded on UPPT001
    outstream = 'serial:/dev/ttyS0';

    %% Setup and open the serial port to write the echo
    delete(instrfind);
    fclose('all');
    % bits=bitsi('com3');

    %% open serial port
    serobjw = serial('/dev/ttyS0');              % Creating serial port object now its connected to COM7
    serobjw.Baudrate = 115200;              % Set the baud rate at the specific value
    set(serobjw, 'Parity', 'none');        % Set parity as none
    set(serobjw, 'Databits', 8);           % set the number of data bits
    set(serobjw, 'StopBits', 1);           % set number of stop bits as 1
    set(serobjw, 'Terminator', '');        % set the terminator value to newline
    set(serobjw, 'OutputBufferSize', 512); % Buffer for write operation, default it is 512
    get(serobjw) ;
    fopen(serobjw);

Now we start the streaming of the data using `ft_poll_buffer`

    while true
      newNum = ft_poll_buffer(cfg.headerfile);

Note that this is replacing the reading of the header in the previous example, i.e.

      hdr = read_header(cfg.headerfile, 'headerformat', cfg.headerformat, 'cache', true);

remember that we were only interested in the hdr.nSamples, which allows to determine whether there any new samples (when compared to the remembred previous sample).
The number of new samples is now already returned by the ft_poll_buffer function ==newNum.nsamples. We therefore replace hdr.nSamples in our code with this number

      hdr.nSamples = newNum.nsamples;
      hdr.nTrials  = 1;
      % see whether new samples are available
      newsamples = (hdr.nSamples*hdr.nTrials-prevSample);

5) Now, to detect the triggers we have two options: To do flank detection on the fly (by differentiating the trigger channel), or to read the relevant event

        ....
        if newsamples>=blocksize
        disp('newsamples')
        % determine the samples to process

        begsample  = prevSample+1;
        endsample  = prevSample+blocksize ;

        %         this allows overlapping data segments
        if overlap && (begsample>overlap)
          begsample = begsample - overlap;
          endsample = endsample - overlap;
        end

        %         remember up to where the data was read
        prevSample  = endsample;
        count       = count + 1;
        fprintf('processing segment %d from sample %d to %d\n', count, begsample, endsample);

        %         read data segment from buffer

        dat = read_data(cfg.datafile, 'header', hdr, 'dataformat', cfg.dataformat, 'begsample', begsample, 'endsample', endsample, 'chanindx', chanindx, 'checkboundary', false);
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %         from here onward it is specific to the method of detecting events
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        if use_read_event~=1 %% just read respecified channel and do flank detection using time differentiation and value matching
          diff_dat = diff([pad dat]);
          pad = dat(end);
          %% detect flanks in UPPT001 that are of size 4
          smp=find(diff_dat==4);
          if~isempty(smp) %% if there is such an event
            smp = smp + begsample; %% get sample number with respect to the beginning of the recording\
            %% create event
            event = [];
            event.type   = 'trigger';
            event.sample = smp;
            event.value=diff_dat(smp-begsample);
            %% display
            disp(event);
            %% create event with same sample number but different value
            out_event=[];
            out_event.sample=event.sample; %% is this correct?
            out_event.type = 'echo';
            out_event.offset = [];
            out_event.value=16;
            out_event.duration=1;
            %% write this event (of size 16) on serial port that goes  to
            %% UPT001
            disp(out_event);
            %write_event(outstream, out_event);
            fwrite(serobjw, out_event.value);
          end


        else %% use read_event function that does the flank detection

          onl_event = read_event(cfg.datafile, 'header', hdr, 'minsample',prev_ev+1);
          evt=filter_event(onl_event(:),'type',cfg.channel,'value',4);

          if ~isempty(evt)
            disp(evt)
            prev_ev=max([evt.sample]);
            fwrite(serobjw,16);

          end
        end

        end % if enough new samples
    end % while true

6) Both trigger and flank are now recorded on the same channel (here UPTT001). Now we can offline calculate the delays in the online loop:

   %% set path to data on disk
   filename=pwd;
   %% read events
   event=read_event(filename);
   %% read trigger events
   trig_in_buff=filter_event(event,'type','UPPT001','value',4);
   %% read echos
   trig_out_buff=filter_event(event,'type','UPPT001','value',16);

   %% extract sample numbers of these events in array
   smp_out=[trig_out_buff.sample]';
   smp_in=[trig_in_buff.sample]';

    %% sort these events ( this might be unnecessary if echos always follow the triggers, i.e there were no missing events and delays in loop were not larger than inter trigger interval)
    %% sort
    all_smp=[smp_in;smp_out];
    [s,i]=sort(all_smp,'ascend')
    %% also remember event values
    val_out=[trig_out_buff.value]';
    val_in=[trig_in_buff.value]';
    all_val=[val_in;val_out];
    %% sorted samples
    all_smp=all_smp(i);
    %% sorted values
    all_val=all_val(i);
    %% now assign trigger and echo's back to sorted samples
    smp_in=all_smp(all_val==4);
    smp_out=all_smp(all_val==16);

7) We can now calculate the time difference between each trigger and the echo that followed i

    diff_in_s=smp_out-smp_in; %% in samples
    hdr=read_header(filename); %% read header to get sample rate to get difference in time
    diff_in_s=(smp_out-smp_in)./hdr.Fs; %% in [s]

We can now plot the distribution of all delay

    figure,
    hist(diff_in_s,50)
    xlabel('delay echo-trigger in [s]')
    title(sprintf(' HL before and after, No of trig =2000, Fs =%d Hz, Nchans = %d',hdr.Fs, hdr.nChans));

and plot the sample number of the echo against the sample number of the sent trigger. Accumulative delays will be seen as a departure from linearity with increasing sample number.

    figure
    plot(smp_in,smp_out, 'x')
    xlabel('sample No of trigger')
    ylabel('sample No of trigger-echo')
    title(sprintf('HL before and after: not continuous,Fs =%d Hz, Nchans = %d',hdr.Fs, hdr.nChans))

Below follow the results of the testing in the DCCN for continuous head localization (HL) or head localization before and after (HL off) and two sampling rates (1200Hz, and 4KHz

### CHL on, Fs=1200, Nchans=341

NOTE: this is a configuration previously considered as buggy, which is now working

{% include image src="/assets/img/example/measuring_the_timing_delay_and_jitter_for_a_real-time_application/delay_hist._1200hz.jpg" %}

We now also plot the sample number of the echo against the sample number of the trigger that preceded i

{% include image src="/assets/img/example/measuring_the_timing_delay_and_jitter_for_a_real-time_application/trigger_smp_vs_echo_smp.jpg" %}

This shows no samples missing and no accumulative delays

### CHL off, Fs=1200, Nchans=311

{% include image src="/assets/img/example/measuring_the_timing_delay_and_jitter_for_a_real-time_application/delay_hist._1200hz_hl_off.jpg" %}

We note that the delays are smaller when the continuous HL is off. This is probably to do with an additional data granularity related to the time required to fit a dipole while doing continuous localization- more details on this will follow soon...

As the speed of the streaming is proportional to the number odf samples in the buffer (how fast the buffer gets filled) this is expected to increase a) with increasing channel numbers b) with increasing sample rate

Here we increase the sampel rate to Fs=4000Hz

### CHL on, Fs=4KHz, Nchans=341

{% include image src="/assets/img/example/measuring_the_timing_delay_and_jitter_for_a_real-time_application/delay_hist_hl_on_fs_4khz.jpg" %}

Comparing Figure 3 to Figure 1a, we see that the delays have decreased.

We now use the 2nd option for detecting events: using ft_read_event. Note that this now does not read from the shared memory buffer but directly from the FieldTrip buffer. Previously some events may have gone undetected , therefore we also need to check the matching of trigger to echo

### CHL on, Fs=4KHz

The events were detected with `ft_read_event`.

{% include image src="/assets/img/example/measuring_the_timing_delay_and_jitter_for_a_real-time_application/trigger_smp_vs_echo_smp_4khz_read_ev.jpg" %}

This shows no events missing and no accumulative delays.The delay distribution is in Figure 5.

{% include image src="/assets/img/example/measuring_the_timing_delay_and_jitter_for_a_real-time_application/delay_hist_hl_on_fs_4khz_detection_read_ev.jpg" %}

Although, here we only have 200 delays (compared to 2000 before), we see that the detection of triggers with read*event is not faster than with the online flank detection, although we might be able to squeeze out a bit more performance (reduce latency) once we use a clever scheme for only reading \_new* events. This also depends on whether **acq2ftx** first writes the events or the samples to the buffer.

## Timing of data blocks with and without head localization

Since **acq2ftx** constantly monitors the state of the shared memory ringbuffer slot that Acq is about to fill next, it can determine the timing of those blocks quite accurately. We carried out a quick test where we measured the delay between the arrival of successive data blocks in shared memory using the ''gettimeofday'' system call, which on Odin (running a 2.4 kernel) yields an accuracy of about 10ms. During the operation, we looked at the time **dT** between each two slots, but also monitored the mean and standard deviation of that value.

Without head localization, **dT** matches the block size of the MEG system up to quantization effects due to the low timer resolution. For example, if the block size is 82 samples and the sampling rate is 1200Hz, the duration of one block is slightly less than 70ms, and consequently **dT** comes out as 60 or 80ms roughly alternatingly. The mean of **dT** quickly approaches the theoritcal block duration.

With continuous head localization however, we observed a wider spread of **dT** values around the (still correct) mean. This effect is most visible for high sampling rates. For example, at 4000Hz and 80 samples blocksize, the theoretical block duration is 20ms. The **dT** values reported by **acq2ft** however are often 0, but sometimes go up to 100 or 120ms. This means that with continuous head localization turned on, **Acq** fills the shared ringbuffer with considerable temporal jitter. We have not written the timing values to disk yet and thus cannot make accurate statements, but it seems that the head localization calculation buffers the data for about 100ms independent of the sampling frequency, and writes it out in bursts of 4-5 slots into the shared memory.

We should a) try to measure these timing issues more accurately, and b) try to find a combination of sampling rate and block size (by varying the amount of transmitted channels) such that the jitter is minimised.

## Timing of the CTF MEG system data stream

The first example shows how you can read data from a real-time acquisition ssytem (in this example it is the MEG system at the FCDC) and determine the timing of each data block as it comes in.

    filename = 'buffer://odin:1972';

    numiter = 100
    clear t s
    tic

    for i=1:numiter
     disp(i)

     % read the header to see whether new samples are available
     hdr = ft_read_header(filename, 'cache', true);

     t(i) = toc;
     s(i) = hdr.nTrials*hdr.nSamples;

     if i>1
       % read a block of data, note that some read requests will pertain to an empty block
       dat = ft_read_data(filename, 'header', hdr, 'begsample', s(i-1), 'endsample', s(i));
     end

    end % for numiter

    % subtract the time and sample from the first iteration
    s = s-s(1);
    t = t-t(1);

    figure
    plot(t, s, '.')
    xlabel('time (s)')
    xlabel('sample number')

    figure
    plot(s./t)
    title('number of samples per second')
    xlabel('iteration number')

## Timing of the ft_read_header function

To test the timing of the detection of new data in the buffer, without actually reading and processing the data, you can use the following code. The **[ft_realtime_signalproxy](/reference/realtime/example/ft_realtime_signalproxy)** function will write some random noise data to a buffer:

    cfg = [];
    cfg.channel = [1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32];
    cfg.fsample= 1000;      % in Hz
    cfg.blocksize = 0.040;  % in seconds
    ft_realtime_signalproxy(cfg)

You can read the data in another MATLAB session on the same computer. In this case we'll just look at how much data is available in the buffe

    for i=1:inf,
      hdr = ft_read_header('buffer://localhost:1972');
      disp(hdr.nSamples);
    end

This will show you something like

    ...
    12160
    12160
    12160
    12160
    12160
    12160
    12160
    12200
    12200
    12200
    12200
    12200
    12200
    12200
    12240
    12240
    12240
    12240
    12240
    12240
    ...

You can notice the number of samples increasing now and then with 40 samples (the blocksize in **[ft_realtime_signalproxy](/reference/realtime/example/ft_realtime_signalproxy)**). In this example, it increases approximately every 7th iteration of the **[ft_read_header](/reference/fileio/ft_read_header)** function. That means that the **[ft_read_header](/reference/fileio/ft_read_header)** function is called 7 times in the time that it took to collect 40 data samples, corresponding to 7 calls per 40 ms, or 5.7 ms per single call to **[ft_read_header](/reference/fileio/ft_read_header)**.

## Timing of the ft_read_header function when accessing shared memory, performed on the CTF275 MEG system at the FCDC

The code below will give you a sense for the distribution of time delays associated with accessing shared memor

    clear read_*
    tic
    n = 1000;
    t1 = zeros(1,n);
    t0 = toc;
    for i=1:n
      hdr = ft_read_header('shm://');
      t1(i) = toc;
    end
    t1 = t1 - t0;
    plot(t1*1000); % in miliseconds

A typical distribution of access times is below:

{% include image src="/assets/img/example/measuring_the_timing_delay_and_jitter_for_a_real-time_application/delay_read_header_acq_buffer.jpg" %}
