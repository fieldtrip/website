---
title: SPM Source reconstruction demo
tags: [meg-uk-2015]
---

During this demo we will estimate the current sources on the cortical surface that gave rise to the electromagnetic activity we measured with MEG and EEG outside the head. To do so, we first need to build a head model, based on the individual MRI, coregister the head model and our M/EEG data and then build a forward model which describes how sources in the brain appear on the different M/EEG sensors. We will then apply two different inversion approaches, both in a Bayesian framework: the Multiple Sparse Priors and the Minimum Norm solution. We will compare the model evidences for these distributed imaging approaches and source localise the evoked oscillatory activity at a particular time-frequency window.

We start by opening SPM1

- First go to the source reconstruction demo folder: cd C:/workshop/spm-source-demo.

- Type 'spm eeg' in the command line to start SPM.

#### Create Head Model and Forward Model

We will use the subject's structural MRI to define meshes describing the cortex, skull and scalp of our subject. Due to the different conductivities (for example between the skull and the scalp) the geometry of the head is important to derive realistic physical forward models that predict how cortical current sources map onto the M/EEG sensors.

1.  In the SPM window click on the batch button. In the batch window select “SPM – M/EEG - Source reconstruction - Head model specification”
2.  Double-click on “M/EEG datasets” and select “PapMcbdspmeeg_run_01_sss” from the Sensor-level statistics demo as input file. This file contains artifact corrected single trial data for EEG, MEG magnetometers, planar gradiometers and combined gradiometers.
3.  Next, set the inversion index to “3”. This index allows you to track different types of forward models and inverse solutions and compare their log model evidences. We choose “3” here as we will later use some pre-calculated inversion models filed under the inversion indices 1 and 2.
4.  Additional comments relating to each index can be inserted if “comments” is selected. We leave this field empty for now.
5.  In the field “meshes” first select “mesh source”. From here specify “Individual structural image” and select the NIfTI file “mprage.nii”. The mesh resolution can be kept as normal (approximately 4000 vertices per hemisphere). This step will generate scalp, skull and cortical meshes by warping meshes from a template brain with the inverse spatial normalisation of the subject's brain.
6.  To coregister the MRI and M/EEG data, please select “specify coregistration parameters”. We first need to specify the fiducials, with coordinates in the space of the MRI image selected. Here we will define “Nasion” and the left and right pre-auricular points “LPA” and “RPA”.
7.  Set the first M/EEG fiducial label to 'Nasion'.
8.  For the Nasion, highlight “How to specify”, select “type MRI coordinates” and enter '[2 81 -4]'
9.  Then specify the second fiducial label as 'LPA' and enter '[-77 -14 -23 ]' for MRI coordinates; the final fiducial label is 'RPA', with MRI coordinates '[83 -20 -25]'.
10. Select “no” for the “use headshape points” option.
11. Finally, for the forward model itself, we highlight “EEG head model”, and specify this as “EEG BEM”; we select “MEG head model” and specify this as “Single Shell”.

You can now run this batch file by pressing the green “run” button. Note that at this stage the model parameters are saved, but the lead fields themselves are not estimated until inversion.

#### Review the head model and forward model

1.  You can review the head model and the forward model by pressing the “3D Source Reconstruction” button within the SPM window.
2.  This will create a new window; select “Load” and choose the “PapMcbdspmeeg_run_01_sss.mat” file. You can find the forward model we just computed under the inversion index “3” (use the “next” and “previous” buttons to navigate between different inversion indices).
3.  On the left hand side of the “source localisation” window, select the “display” button below the “MRI” button. This will bring up the scalp (orange), inner and outer skull (red) and cortical (blue) meshes of the subject's brain. Note that the fiducials are shown by cyan discs.
4.  Next, select the “display” button beneath “Co-register” and then select “MEG” when asked what to display. The graphics window should the sensor locations in green discs, the digitized headpoints in small red dots, the fiducials in the MEG data as purple diamonds, and the MRI fiducials as cyan discs again. The overlap between MRI and MEG fiducials indicates how well the data have been coregistered.
5.  Finally, select “Display”, located beneath “Forward Model”, and select again “MEG”. You should see an image displaying the MEG sensor locations relative to the cortical mesh and the single shell fitted to the inner skull mesh.

#### Model Inversion

We will next compute the inverse solutions and compare two distributed source reconstruction approaches. Since the inverse problem is ill-posed, prior information must be included to give a unique solution. We will first apply the **Multiple Sparse Priors** approach; this corresponds to a sparse prior on the sources, namely that only a few sources are activ

1.  Go back to the Batch Editor, under “file” open a new batch and select “SPM - M/EEG - Source reconstruction – Source Inversion”
2.  Select the same input file “PapMcbdspmeeg_run_01_sss.mat”, and set the inversion index to “1”. We will make use of some pre-calculated inversion models created earlier for indices 1 and 2.
3.  We will invert the data for Famous, Unfamiliar and Scrambled faces: highlight “what conditions to include” and select “All”.
4.  Next highlight inversion parameters, choose “custom” and keep the inversion type as “GS”. Greedy Search (GS) is one of several fitting algorithms for optimising the MSP approach; we choose GS here because it is quickest and works well for these data.
5.  Then enter the time window of interest as “[-100 800]”
6.  We want to consider all frequencies; please set the frequency window of interest to “[0 256]”.
7.  Select “yes” for the “PST Hanning window”. In this example we do not provide “Source priors” and don't want to “Restrict solutions”; these fields remain unchanged. You can find an example on how to include fMRI-based location priors into source reconstruction in the SPM12 manual chapter on multimodal and multisubject data fusion.
8.  As final step use “Select Modalities” and choose 'MEG' to invert only the 102 magnetometers. You can also select several sensor types and fuse EEG and MEG data. Note that we cannot invert the combined planar gradients, because we do not have a physical forward model for those.

The second type of inversion we will examine corresponds to a **L2-minimum norm** (MNM) solution, i.e, fitting the data at the same time as minimising the total energy
of the sources. In SPM, this is called “IID” because it corresponds to assuming that the prior probability of each source being active is independent and identically
distributed.

9.  Go back to the batch editor, add another “M/EEG - Source reconstruction – Source Inversion” module, and select the same input files as before (“PapMcbdspmeeg_run_01_sss.mat”), but this time set the inversion index to 2. We use the same forward model as for the “MSP” source reconstruction.
10. Set the inversion parameters to “custom” again, but this time with the inversion type “IID”. The remaining parameters should be made to match the Multiple Sparse Priors inversion approach.

#### Time-frequency contrasts

With the previous steps, we invert data of whole trials from -100 to +800ms across all frequencies. Next we want to localise the evoked activity around the N/M170 face component by averaging power across a suitable time-frequency window

1.  Select “M/EEG - Source reconstruction – Inversion Results”.
2.  Again, select “PapMcbdspmeeg_run_01_sss.mat” as input file; set the inversion index to 1. We will first investigate averaged source power across the time-frequency window of interest for the MSP solution.
3.  Set the time window of interest to “[100 250]” and the frequency window of interest to “[10 20]”.
4.  For the contrast type, please select “evoked” from the current item window, and the output space as “MNI”.
5.  We can now write the source power image as a surface-based GIFTI “Mesh” by high-lighting the option “Mesh”.
6.  Finally, we smooth across the cortical surface to render our data more suitable for RFT. Keep the default cortical smoothing of 8.
7.  Then replicate this module to produce a second “inversion results” module by right-clicking on the module and selecting “replicate”.
8.  Here, change the inversion index from “1” to “2” to write out the time-frequency contrast for the MNM (IID) distributed solution as well.

#### Generating batch scripts

You can use the batch framework to construct a processing pipeline across a group of subjects or across different source reconstruction approaches. A brief example

1.  Save the batch by going to “File” in the Batch editor and select “save Batch and Script“. As file name write 'batch_localise_inv'. This will result in two files: a batch file 'batch_localise_inv_job.m' and a Matlab script 'batch_localise_inv.m' which runs the batch file. Take a look at the job-file by entering “open batch_localise_inv_job.m” in the MATLAB command window.
2.  In batch_localise_inv.m replace nrun = X; with nrun = 1 and save the file. We could now run this Matlab script with the same results as if we had pressed the green “Run” button in the Batch Editor.
3.  To make things a bit more interesting, we go back to the batch and right-click on the M/EEG datasets field of the first source inversion module and select “Clear Value”. Do the same for “Time window of interest” and save batch and script under 'batch_localise_inv_subj.m'.
4.  In the MATLAB command window, type 'open batch_localise_inv_subj_job.m'. The cleared values have been replaced by '`<UNDEFINED>`'. We will provide these undefined values via the Matlab script.
5.  In batch_localise_inv_subj.m replace nrun = X; with nrun = 1 and as inputs specify “{'PapMcbdspmeeg_run_01_sss.mat'}” and [-100 800].
6.  Finally, save and run the batch_localise_inv_subj.m script.

#### Review inverse solutions

1.  Review the inverse results by pressing the “3D Source Reconstruction” button within the SPM window; re-load the “PapMcbdspmeeg_run_01_sss.mat” file.
2.  Press the “mip” (“Maximum intensity projection”) button below the “Invert” button. The top plot shows the evoked responses for the three conditions from the peak vertex, with the red line being the currently selected condition, here “1” for Famous faces (press the “condition” button to toggle through the other conditions). The bottom plot will show the maximal intensity projection at the time of the maximal activation.
3.  Take a look at the log model evidence and the percent variance explained.
4.  If you press “display” under the “Window” button, you can see a MIP for the time-frequency contrast limited to the 100-250ms, 10-20Hz window specified above; if you press the “display” under the “Image” button, you will see a rendered version.
5.  Press the “previous” button to select the previous inversion, which here corresponds to the MSP inversion. Press the “mip” button again. You can change the time of interest or the vertex by entering new values into the window below the “mip” button.
6.  Compare the model evidences and the percentage explained of the data variance of the MNM and the MSP solution. Which model explains the data better?
7.  Again, press "display" beneath the "Window" button and you should see results that are sparser and deeper inside the brain.
8.  You can further explore your inverse solutions by pressing the ”Render” button of the “3D Source Reconstruction” window. For example, you can play a movie of the source activity over time, look at the time courses of virtual electrodes (just first click on 'virtual electrodes' and then on the area of the cortical surface you are interested in) or compare the observed and predicted sensor signals at different time points. You can toggle between models (MSP and MMN) and the conditions (1-Famous, 2-Unfamilar, 3 Scrambled) by pressing the buttons at the top of the render window.

We are at the end of the demo now. You can use the forward model under index “3” and play around with the inversion models, take a look at the induced activity or try to invert MEG and EEG data together.

SPM offers many other options for source reconstruction. Here we used two different distributed source reconstruction methods, but you could also use a Bayesian version of an Equivalent Current Dipole algorithm by selecting VB-ECD after clicking the “Invert” button within the “3D Source Reconstruction” window.

#### Literature

- http://www.fil.ion.ucl.ac.uk/spm/doc/manual.pdf
- Henson, R.N., Mattout, J., Phillips, C. and Friston, K.J. (2009). Selecting forward models for MEG source reconstruction using model-evidence. Neuroimage, 46, 168-176.
- Henson, R.N., Wakeman, D.G., Litvak, V. and Friston, K.J. (2011). A Parametric Empirical Bayesian framework for the EEG/MEG inverse problem: generative models for multisubject and multimodal integration. Frontiers in Human Neuroscience, 5, 76, 1-16. <http://www.fil.ion.ucl.ac.uk/spm/doc/papers/HensonEtAl_FiHN_11_PEB_MEEG.pdf>
