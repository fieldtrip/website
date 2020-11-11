
create signal (ongoing alpha) + some noise
    n = 100;
    x = randn(n,2000);
    x = ft_preproc_bandpassfilter(x, 1000, [8 12], [], 'firws');
    x = x+randn(n,2000)./10;

    y = x;
    z = x;
    q = x;

create a transient and add this to the ongoing signal in 4 flavours
    transient = (sin((2.*pi.*(0:149))./150)).*[ones(1,75) ones(1,75)./2];
    for k = 1:size(y,1)
      % add a transient around 0-150 ms -> jittered case
      % add a transient around 0-150 ms -> jittered case + variable amplitude
      jitter = randi(80,1,1)-40;
      amp    = rand(1,1).*0.5;
      y(k,(1001:1150)+jitter) = y(k,(1001:1150)+jitter)+0.25.*transient;
      z(k,(1001:1150)+jitter) = z(k,(1001:1150)+jitter)+amp.*transient;
      
      % add a transient at 0-150 ms -> ideal case
      x(k,1001:1150) = x(k,1001:1150)+0.25.*transient;
      
      % add a variable amplitude transient
      q(k,1001:1150) = q(k,1001:1150)+amp.*transient;
      
    end
    figure;plot(z');
    figure;plot(y');
    figure;plot(x');
    figure;plot(q');


create an ft-like data structure
    data = [];
    data.trial = cell(1,n);
    data.time  = cell(1,n);
    for k = 1:n
      data.trial{k} = [x(k,:);q(k,:);y(k,:);z(k,:)];
      data.time{k}  = ((0:1999)./1000)-1;
    end

    data.label = {'latfix-ampfix';'latfix-ampvar';'latvar-ampfix';'latvar-ampvar'};

estimate the ERP
    tlck = ft_timelockanalysis([], data);
    figure;plot(tlck.time, tlck.avg); legend(tlck.label);
subtract the ERP from the data
    data_minus_erp = data;
    for k = 1:numel(data.trial)
      data_minus_erp.trial{k} = data.trial{k} - tlck.avg;
    end

do time-frequency decomposition
    cfg = [];
    cfg.method = 'mtmconvol';
    cfg.foi = 2:2:20;
    cfg.output = 'pow';
    cfg.toi = data.time{1};

    cfg.t_ftimwin = ones(1,numel(cfg.foi)).*0.5;
    cfg.taper = 'hanning';
    cfg.keeptrials = 'yes';
    freq = ft_freqanalysis(cfg, data);
    freq_minus_erp = ft_freqanalysis(cfg, data_minus_erp);

    fd = ft_freqdescriptives([], freq);
    fd_minus_erp = ft_freqdescriptives([] ,freq_minus_erp);

express power relative to a baseline
    cfg = [];
    cfg.baseline = [-0.6 -0.2];
    cfg.baselinetype = 'relchange';
    fd = ft_freqbaseline(cfg, fd);
    fd_minus_erp = ft_freqbaseline(cfg, fd_minus_erp);

create an ordered layout for the 4 channels
    cfg = [];
    cfg.layout = 'ordered';
    cfg.rows   = 2;
    cfg.columns = 2;
    layout = ft_prepare_layout(cfg, fd);

    cfg = [];
    cfg.xlim    = [-0.6 0.6]; % avoid plotting the filter edges
    cfg.layout = layout;
    cfg.showlabels = 'yes';
    ft_multiplotTFR(cfg,fd); % note there's an issue with recent versions (i.e. mid 2020) of ft_multiplotTFR so one needs the latest version of FT for this to work
    ft_multiplotTFR(cfg,fd_minus_erp); 

