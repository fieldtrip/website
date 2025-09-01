---
title: M/EEG analysis workshop in Jyväskylä, Finland
---

There will be a M/EEG analysis workshop in Jyvaskyla, focussing on connectivity analysis. On one of the days we will use FieldTrip for the teaching, on the other day we will use MNE-Python. This workshop is part of a summer school: [International summer school on understanding learning in the brain](http://cibr.jyu.fi/en/training/brain-summerschool2017/scientific_program).

- By whom: Simo Monto, Matti Stenroos, Jan Kujala, Jan-Mathijs Schoffelen and others
- When: 15-16 June 2017

More details are provided by the local organizers [here](http://cibr.jyu.fi/en/training/brain-summerschool2017/scientific_program).

## How should you prepare for the workshop?

{% include markup/yellow %}
In this workshop we will have a steep learning curve. We will move from basic preprocessing to channel and source-level connectivity. Given the limited amount of time, it is **important** that you come well prepared.
{% include markup/end %}

If you are not familiar with MATLAB or are not certain about your MATLAB skills, please go through the "MATLAB for psychologists" tutorial on <http://www.antoniahamilton.com/matlab.html>

Please read the [FieldTrip reference paper](http://www.hindawi.com/journals/cin/2011/156869/) to understand the toolbox design.

Furthermore, we recommend you to watch the following online videos prior to the workshop. Note that these video lectures cannot be quickly glanced over. You should **plan ahead and take your time** to go through them.

- [FieldTrip toolbox introduction, 1 hour](https://www.youtube.com/watch?v=eUVL_twWNdk)
- [MEG basics and instrumentation, 15 minutes](https://www.youtube.com/watch?v=CPj4jJACeIs)

The content of the shorter second lecture is also covered in the first, but presented differently and therefore possibly useful to get a good understanding of the signals that we deal with.

For most of the hands-on session, we will create some simulated data to learn and understand about some basic connectivity measures. We will also process some real data, but will not spend too much time on understanding how MATLAB works and how FieldTrip organizes the data. Therefore if you have never done any FieldTrip analysis in MATLAB before, you should read this [introduction tutorial](/tutorial/intro/introduction) and you should go through the [MEG preprocessing tutorial](/tutorial/sensor/eventrelatedaveraging). Depending on your understanding of MATLAB and MEG, you can **simply read** the preprocessing tutorial (which will take you 30 minutes) or download the example data and **go through it step by step** (which will take you 2 hours).

{% include markup/yellow %}
So overall there is about 2 to 5 hours of preparation required from you prior to the workshop!
{% include markup/end %}

## Getting started with the hands-on sessions

For the hands-on sessions we will use MATLAB R2015b, which you can start from the Taskbar shortcut. To ensure that everything runs smooth, we will work with a clean and well-tested version of FieldTrip that we have installed on all computers. Importantly, the tutorial data does not have to be downloaded but will also have been distributed on the computers.

In order to get started, and ensure that all paths are set correctly, after you start up MATLAB, you need to navigate to C:\\MyTemp\\MEGSummerschool\\training_data\\toolkit_jyvaskyla\\, and type 'startup' on the command line. This command ensures that the MATLAB path is set correctly to include the necessary FieldTrip functions.

Next, the hands-on sessions are pretty self explanatory. The tutorials contain quite some text to read, providing background, and then some sections of MATLAB code, which you are to execute on the command line. The most efficient way to do this, is to copy-and-paste the sections of MATLAB code into a MATLAB-script (for novices: this is a text file that you can edit, and from which you can easily execute code). If you are unsure about how to do this, ask a knowledgeable colleague, or one of the tutors.

{% include markup/red %}
In general, please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using the startup.m file than the path GUI.

Furthermore, please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed (see this [FAQ](/faq/matlab/installation)).
{% include markup/end %}

- morning

  - 1h Lecture on some aspects related to connectivity analysis on M/EEG data. Measures of directed interactions, interpretational issues, and howto's.
  - 1.5h handson [Connectivity](/tutorial/connectivity)

- afternoon
  - 1.5h handson [Networkanalysis](/tutorial/connectivity/networkanalysis)
