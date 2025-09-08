---
title: How to ask good questions to the community?
tags: [support, email]
category: faq
redirect_from:
    - /faq/how_to_ask_good_questions_to_the_community/
    - /faq/emaillist_howtoask/
---

The FieldTrip community is represented on the [email discussion list](/discussion_list). You can also sign up and ask for help if you are stuck in using FieldTrip. Asking good questions there (and giving useful answers) is the key to a successful community. However, please do some research yourself on them before approaching fellow researchers on the discussion list. Keep in mind that several hundreds of researchers around the world will get note of your question and will spend their valuable time on reading your question. In addition, also keep career perspectives into mind. By asking your first question on the mailing list (which could be before you wrote your first paper), they will get a first impression of you and may start to form a picture of you, be it as a prospective colleague or collaborator. Many of the members are senior researchers and might have a job opening and are looking for you! But, don't be afraid to ask questions, we really appreciate if you approach us and we will try to help, even if your question turns out to have a trivial answer :)

{% include image src="/assets/img/faq/emaillist_howtoask/peanutsediting.jpg" width="400" %}

To facilitate you in asking good quality questions, this FAQ serves as a guide for

- what questions to ask
- when to ask a questions
- how to ask a question

Also note that when you become more experienced, you can (and should) help other users by answering their questions! The community lives from giving and sharing!

## What kind of questions should be asked?

A question can be anything, from asking about whether an error is a bug or a user-error, fundamental questions on how an algorithm works or asking for advise on how to design the analysis given a specific research question or hypothesis. Anything that is related to FieldTrip, but also anything general about electrophysiological data analysis is welcome. We love a variety of topics, so questions about fundamental neuronal mechanism are as welcome as asking if FieldTrip can be used to assessing temporal dependencies of seismic activity, or just to advertise your (neuro-)job opening or neuro-software.

## When to ask a question?

Feel free to ask a question any time, be it day or night.

Actually, the intention of 'when?' is 'what should you have done before asking a question?'. Of course, think thoroughly yourself about possible answers. Use Google and the FieldTrip webpage to search for keywords and try to put your question into perspective with papers by other researchers. Spend at least about an hour of time for finding an answer yourself before turning to the discussion list. That way, you can guarantee that you tried yourself finding an answer. Often, you will find that the answer is more trivial than expected. By going through the process yourself of thinking about how to best search for the answer (and eventually finding an answer yourself), you will learn much more about 'whatever you are looking for' than by asking someone else.

## How to ask a question?

The better you describe the problem or state the question, the more likely you will get help. Better hereby does not mean more information. As being concise is a key skill of a scientist, show off by staying concise (but complete) when writing to the mailing list. Completeness of the question and background information is equally important though. This counts for all kind of questions, be it directly FieldTrip related or about anything else. A useful tip: Before sending your mail, read the message thoroughly and think whether all necessary information for a person naive to your question is included. Does it make sense what you wrote? Is there too much information? Remember that many people are busy and won't like having (a) long conversations asking you to provide more information and (b) reading through much more than 10 sentences per mail.

{% include markup/yellow %}
If it comes to asking questions about FieldTrip including the following is a must:

- The cfg you used
- The fields of your data structure
- The line you called that gave an error / that you would like to ask a question on
- The exact error message you got

The cfg and data can be displayed in MATLAB using the display(variable_name) command. Call display(cfg) and display(data) and copy the answer over to include it in your mail.

If you have data to share and it exceeds 1 MB, do not send it as attachment, but use a file hosting service as explained [here](/faq/organization/datasharing).
{% include markup/end %}

## Example message

Here is an example of an inefficient question:

{% include markup/skyblue %}
Subject: HELP

**I am getting to load Eyetracking data from .EDF to .ASC then wish to have the image present on the screen in order t draw ROIs. As I follow the step from this link https://www.fieldtriptoolbox.org/getting_started/eyelink. The function of FieldTrip called "dataset2file.m" cannot accept file type of structure in MATLAB**. The error message show "Undefined function 'dataset2files' for input arguments of type 'struct'." How can I change the code so the function can read structure file.

`<no name>`
{% include markup/end %}

If this is your first mail, please introduce yourself shortly.

{% include markup/skyblue %}
Subject: Improper matrix assignment in ft_functionname

Dear community,

My name is MyName MyLastname and I am working in the BigBoss lab in MyCity on intracranial and extracranial Brain-Computer Interfaces. Currently I am analyzing data of a side-project, where we recorded using combined EEG/fMRI.

I tried using ft_functionname to assess spatio-temporal aspects of my data. When I call ft_functionname, I expect to get a structure with several fields, which I can subsequently plot using ft_XXXplot. However, I receive the following error message:

    ??? In an assignment A(:) = B, the number of elements in A and B
    must be the same.
    Error in ==> ft_functionname at 23
    data.time(cfg.time) = time;

The cfg and data I use are as follows:

    >> display(cfg)

    cfg.time = -1:0.25:0;
    cfg.freq = 1:32;
    ...

    >> display(data)

    data.freq = [1 2 3 ... 32]
    data.time = <1x321 cell>
    ...

I uploaded my cfg and data on WeTransfer as it is too large as attachment; you can download it from <http://www.wetransfer.com/xxx>.

Can someone tell me if there is something wrong with the cfg settings I use or if I am doing something wrong at any other place? The last days, I tried using ... and ... but without success. Also I expected ... to be wrong, but after running intensive tests I could not find anything wrong with it. Any help would be appreciated.

Best,

MyName
{% include markup/end %}
