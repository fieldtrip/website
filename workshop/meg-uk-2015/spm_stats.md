---
title: SPM Sensor-level stats demo
tags: [meg-uk-2015, glm]
---

# SPM Sensor-level stats demo

In this demo we will perform statistical analysis of sensor-level scalp x time images within subject. All classical statistical analyses in SPM are performed on either volumetric images in NIfTI format (can appear either as single files with .nii extension or pairs of files with .hdr and .img extensions) or data on meshes in GIfTI format (pairs of files with .gii and .dat extensions). Thus, any features derived from M/EEG must be converted into one of these formats first.

Then we will use the batch interface to specify a statistical model. There are many options in the batch tool, but they all eventually come down to specification of the GLM design matrix and covariance structure of the residuals. Therefore, any classical statistical analysis in SPM (time-frequency data, source images, group analysis etc.) will only differ from what you are about to do by the inputs you provide and the exact statistical design specification. You can see an example of group analysis of time-frequency data in the SPM12 manual chapter on [Multimodal, Multisubject data fusion](http://www.fil.ion.ucl.ac.uk/spm/doc/manual.pdf).

## Export to images

To create 3D scalp-time images for each trial, the 2D representation of the scalp is created by projecting the sensor locations onto a plane, and then interpolating linearly between them onto a 32x32 pixel grid. This grid is then tiled across each timepoint.

- Run MATLAB, make sure the root SPM folder is in your MATLAB path and write 'spm eeg' in the command line.

- Press the 'Batch' button and select the “SPM – M/EEG – Images – Convert2Images” option in the batch editor.

- For the input file, select the “PapMcbdspmeeg_run_01_sss.mat” file that contains every trial (i.e, before averaging), but with bad trials marked (owing to excessive EOG signals; see the manual chapter for more details).

- Next select Mode, and select “scalp x time”.

- Then, select “Conditions”, select “Specify” and enter the condition label “Famous”. Then repeat for the condition labels “Unfamiliar” and “Scrambled”.

- To select the channels that will create your image, highlight the “Channel selection”, select “Delete: All(1)” and then select “New: Select channels by type” and select “MEGMAG”.

- The final step in this tool is to name the Directory prefix “mag*img*” this can be done by highlighting “directory prefix”, selecting “Specify”, and the prefix can then be entered.

Random Field Theory, used to correct the statistics below, assumes a certain minimum smoothness of the data (at least three times the voxel size). We will add an additional step of Gaussian smoothing of the images to ensure this smoothness criterion is met.

- Select “SPM-Spatial-Smooth” from the batch tool menu. A “Smooth” module will be added below “Convert2images” module.

- Click on this module, highlight “Images to smooth” and press the “Dependency” button in the bottom right corner of the batch window. In the list that comes up select “Convert2Images:M/EEG exported images” and press “OK”. This specifies the exported images that have not yet been created as input to the smoothing step.

- Highlight “Implicit masking” and select “Yes”. This makes sure that smoothing doesn't go beyond the original head boundaries.

- If everything is specified correctly the 'run' button in the toolbar of the batch tool should turn green. Press it to run the batch.

## Reviewing images

Once you have run the batch, a new directory will be created called “mag_img_PapMcbdspmeeg_run_01_sss”. Within that directory will be three unsmoothed 4D NIfTI files, one per condition and three smoothed versions of the same files whose name starts with 's' prefix. It is very important to note that these 4D files contain multiple “frames” (i.e. 3D scalp-time images), one per trial (i.e. 296 in the case of unfamiliar faces).

- To view one of these, press “Display – Images” in the SPM Menu window, and select, say, the “condition_Unfamiliar.nii” file. But note that by default you will only see the first scalp-time image in each file (because the default setting of “Frames” within the Select Image window is “1”). To be able to select from all frames, change the “Frames” value from 1 to “Inf” (infinite) when opening the file, and now you will see all 296 frames (trials) that contained Unfamiliar faces. If you select one of them you can scroll will the cross-hair to see the changes in topography over time.

- You can use CheckReg button in the main SPM menu to display several images side by side and compare them. This is useful, for instance to compare the original and smoothed version of an image.

A useful trick is to use regular expressions to select only part of the available images in a folder. For instance writing ^condition_F.\* in the “Filter” box and pressing Enter will only leave images whose name starts with “condition_F” i.e. in this case unsmoothed images from the “Famous” condition. This trick will be useful when specifying the statistical model below.

## Model Specification

Now we have one image per trial (per condition), we can enter these into a GLM using SPM's statistical machinery (in the same was that we treat other data from other modalities such as PET or fMRI). If we ignore temporal autocorrelation across trials, we can assume that each trial is an independent observation, so our GLM corresponds to a one-way, non-repeated-measures ANOVA with 3 levels (conditions).

- To create this model, open a new batch, select “Factorial design specification” under “Stats” on the “SPM” toolbar at the top of the batch editor window. The first thing is to specify the output directory where the SPM stats files will be saved. So first create such a directory within the subject's sub-directory, calling it for example “Stats”. Then go back to the batch editor and select this directory.

- Highlight “Design” and from the current item window, select “One-way ANOVA”. Highlight “Cell”, select “New: Cell” and repeat until there are three cells.

- Select the option “Scans” beneath each “Cell” heading (identified by the presence of a “<-X”). Select “Specify”, and in the file selector window, remember to change the “Frames” value from 1 to “Inf” as previously to see all the trials. Select all of the smoothed image files for one condition. This can be done by writing ^scondition* F.\* for the “Famous” condition (and respectively ^scondition* U._ and ^scondition\_ S._ for “Unfamiliar” and “Scrambled”), pressing Enter and then right-clicking the file list and pressing “Select All” in the pop-up menu that appears. It is vital that the files are selected in the order in which the conditions will later appear within the Contrast Manager module (i.e., Famous, Unfamiliar, Scrambled).

- Next highlight “Independence” and select “Yes”, but set the variance to “Unequal”. Keep all the remaining defaults (see other SPM chapters for more information about these options).
  Finally, to make the GLM a bit more interesting, we will add 3 extra regressors that model the effect of time within each condition (e.g., to model practice or fatigue effects).

- Press “New: Covariate” under the “Covariates” menu, and for the “Name”, enter “Order”. For vector, enter “1:880” (880 is 295+296+289) and select “Interactions” “With Factor 1” and “Centering” “Factor 1 mean”. By doing so, we create three (mean-centered within each level) regressors that model linear effects of time within each trial type.

- For didactic purposes let us also define a random covariate that should not generate significant effects. Press “New: Covariate” under the “Covariates” menu, for the “Name”, enter “Random” and for the “Vector” enter `randn(1, 880)` (mean-centered by default). Before defining this covariate, we would recommend you type `rng('shuffle')` at the MATLAB prompt such that everyone will create a different covariate.

This now completes the GLM specification, but before running it, we will add one more module.

- Add a module for “Model estimation” from the Stats option on the SPM toolbar menu and define the file name as being dependent on the results of the factorial design specification output. For “write residuals”, keep “no”. Select classical statistics.

- Run the pipeline by pressing the green 'run' button.

## Setting up contrasts and reviewing results

The final step in the statistics pipeline is creating some planned comparisons of conditions by using the “Contrast Manager”. We will do this interactively using the GUI tool, but you can see in the manual chapter how this can also be done using batch.
The first contrast will be a generic one that tests whether significant variance is captured by the 7 regressors (3 for the main effect of each condition, 3 for the effects of time within each condition and 1 for the random regressor). This corresponds to an F-contrast based on a 7x7 identity matrix.

- Press the “Results” button in the main SPM window. In the file selector that comes up select the “SPM.mat” file in the “Stats” directory. In the window that comes up check the “F-contrast” radio button and press “Define new contrast” button. Name this contrast “All Effects”. Then define the weights matrix by typing in “eye(7)” (which is MATLAB for a 7x7 identity matrix). We will use this contrast later to plot the parameter estimates for these 7 regressors. Press “OK”
  More interestingly perhaps, we can also define a contrast that compares faces against scrambled faces (e.g., to test whether the N170 seen in the average over trials is reliable given the variability from trial to trial, and to also discover where else in space or time there might be reliable differences between faces and scrambled faces).

- So make another F-contrast, name this one “Faces (Fam+ Unf) `<>` Scrambled”, and type in the weights “0.5 0.5 -1 0 0 0 0” (which contrasts the main effect of faces vs scrambled faces, ignoring any time effects (though SPM will complete the final zeros if you omit)). Note that we use an F-test because we don't have strong interest in the polarity of the face-scrambled difference. But if we did want to look at just positive and negative differences, you could enter two T-contrasts instead, with opposite signs on their weights.

- To test for the differences between Familiar and Unfamiliar faces make an F-contrast named “Fam`<>`Unf”, and type in the weights “1 -1 0 0 0 0 0”.

- Just to see an example of a T-contrast, create a new T-contrast for the random regressor, by checking the “t-contrasts” button, naming the contrast “Random+” (as it will only test for positive correlation with the random values) and specifying the contrast vector as [0 0 0 0 0 0 1]. Press OK.

- Switch back to F-contrasts, highlight the “Faces (Fam+Unf)`<>`Scrambled” contrast and press “Done”. Within the “Stats: Results” bar window which will appear on the left hand side, select the following: Apply Masking: None, P value adjustment to control: FWE, keep the threshold at 0.05, extent threshold {voxels}: 0; Data Type: Scalp-Time.

- Move the cursor to the earliest local maximum –the first local peak in the first cluster - this corresponds to x=+26mm, y=-84mms and t=160ms (i.e. right posterior scalp). If you then press “Plot – Contrast Estimates – All Effects”, you will get 7 bars. The first three reflect the three main conditions (the red bar is the standard error from the model fit). You can see that Famous and Unfamiliar faces produce a more positive amplitude at this space-time point than Scrambled faces (the “N170”. Note that the 'N' notation comes from EEG whereas in MEG the polarity can be different depending on the sensor). The next three bars show the parameter estimates for the modulation of the evoked response by time. These effects are much smaller relative to their error bars (i.e., less significant) as is the random regressor effect.

- Now in the interactive SPM window go to “Contrasts” menu, select “Change Contrast” and “F: Fam`<>`Unf”. You will see that nothing comes out as significant at the FWE p<0.05 level. To try a different way of significance testing go to “Contrasts-Significance level – Change”. Press 'none' and select 0.01 as uncorrected (a.k.a. cluster-forming) threshold. You will see several clusters of different sizes. Their significance can be assessed by looking at the third from the left column in the stats table. You can see that only the largest cluster has a p-value of less than 0.05. You can now only display that cluster by changing the significance level again and repeating the steps but this time choosing an extent threshold value somewhere between the significant and the largest insignificant cluster size (e.g., 1500).

- Now try to do the same for the random regressor contrast. Is there any way you can get “significant” results with it?

There are many further options you can try. For example, within the bottom left window, there will be a section named “Display”, in the second drop-down box, select “Overlay – Sections” and from the browser, select the “mask” file in the analysis directory. You will then get a clearer image of suprathreshold voxels within the scalp-time-volume.
