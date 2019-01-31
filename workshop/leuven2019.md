---
title: ChildBrain pre-conference workshop in Leuven, Belgium
---

# FieldTrip workshop in Bern, Switzerland

-   By whom: Raul Granados, Simon Homölle
-   When: 5 February 2019
-   Where: Pre-conference training courses at the ChildBrain conference in Leuven <http://www.baci-conference.com>
-   Local organization: Raul Granados.

## How should you prepare for the workshop?

For the hands on session, we kindly require you to bring a functional laptop with MATLAB and FieldTrip installed. This session will be divided in a theoretical introduction, followed by the practical session, for which we ask you to read the points below:
-   We expect that you know the basics of MATLAB and that you already have experience with MEG/EEG preprocessing and analysis.
-   As the focus is on source reconstruction, topics that will NOT be covered in great detail are segmenting, artifact handling, averaging, frequency and time-frequency analysis, statistics.
-   If you are not familiar with MATLAB or are not certain about your MATLAB skills, please go through the “MATLAB for psychologists” tutorial on http://www.antoniahamilton.com/matlab.html to understand the FieldTrip toolbox design please read the FieldTrip reference paper.
-   We will not spend too much time on understanding how MATLAB works and how FieldTrip organizes the data. Therefore if you have never done any FieldTrip analysis in MATLAB before, you should read this introduction tutorial.

In the first workshop hands-on session we will start with preprocessing EEG data, but will not spend too much time on understanding how MATLAB works and how FieldTrip organizes the data. Therefore if you have never done any FieldTrip analysis in MATLAB before, you should read this [introduction tutorial](/tutorial/introduction).
_We will start at 9:00 sharp and will finish around 12:00._

#### Tuesday

| 09:00-09:15 | Welcome       |
| 09:15-10:15 | Lecture       |
| 10:15-10:30 | Coffee break  |
| 10:45-12:00 | Hands on      |

First of all we have to download the pediatric head model from https://www.pedeheadmod.net.

To get going, you need to start MATLAB. Then, you need to issue the following command

    restoredefaultpath
    cd path_to_fieldtrip
    addpath(pwd)
    ft_defaults

{% include markup/danger %}
Please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using the startup.m file than the path GUI.

Please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed.
{% include markup/end %}

The restoredefaultpath command clears your path, keeping only the
official MATLAB toolboxes. The addpath(pwd) statement adds the
present working directory, i.e. the directory containing the fieldtrip
main functions. The ft_defaults command ensures that all required
subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check the present working directory.

After installing FieldTrip to your path, you need to change into the hands-on specific directory, containing the data that is necessary to run the specific hands-on session. These folders are located in C:\\FieldTrip_workshop\\.
