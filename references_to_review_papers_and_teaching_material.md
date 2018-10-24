---
layout: default
tags: references
---

# References to review papers and teaching material

Here we try to compile a list of background reading/studying material. If you know of good papers or other material, please add it by clicking on the edit button.

## EEG and MEG

Sylvain Baillet wrote a recent review manuscript on [Magnetoencephalography for brain electrophysiology and imaging](http://www.nature.com/neuro/journal/v20/n3/full/nn.4504.html) in Nature Neuroscience (2017).

A comprehensive introduction in the neurophysiology and biophysics of EEG (also relevant for MEG) is given in [Electric Fields of the Brain: The Neurophysics of EEG, 2nd Edition](http://www.amazon.com/Electric-Fields-Brain-Neurophysics-EEG/dp/019505038X/ref=sr_1_1?s=books&ie=UTF8&qid=1375859032&sr=1-1) by Paul L. Nunez and Ramesh Srinivasan.

Steven J Luck, [An Introduction to the Event-Related Potential Technique](http://www.amazon.com/Introduction-Event-Related-Potential-Technique-Neuroscience/dp/0262621967), MIT Press: 2005, ISBN 0262621967. This book is reviewed here: Peter Hagoort (2006) [Event-related potentials from the user's perspective](http://www.nature.com/neuro/journal/v9/n4/full/nn0406-463.html); Nature Neuroscience 9, 463.

 [The brain in time: insights from neuromagnetic recordings](http://onlinelibrary.wiley.com/doi/10.1111/j.1749-6632.2010.05438.x/abstract) by Riitta Hari, Lauri Parkkonen and Cathy Nangini gives a comprehensive introduction to MEG.

MEG: An Introduction to Methods. by Peter Hansen, Morten Kringelbach, Riitta Salmelin. [Pdf](http://brainmaster.com/software/pubs/brain/MEG%20-%20An%20Intro.pdf), [Amazon](http://www.amazon.com/MEG-Introduction-Methods-Peter-Hansen/dp/0195307232/ref=sr_1_2?s=books&ie=UTF8&qid=1375859237&sr=1-2&keywords=magnetoencephalography).

## Guidelines for acquisition, analysis and publication

Specifically for MEG we recommend the [Good practice for conducting and reporting MEG research](http://www.sciencedirect.com/science/article/pii/S1053811912009895) paper by Joachim Gross et al. that was published in 2012 in NeuroImage.

When doing clinical MEG, please check [IFCN-endorsed practical guidelines for clinical magnetoencephalography (MEG)](https://doi.org/10.1016/j.clinph.2018.03.042) in Clinical Neurophysiology, 2018.

Terry Picton et al. published the [Guidelines for using human event-related potentials to study cognition: recording standards and publication criteria](http://onlinelibrary.wiley.com/doi/10.1111/1469-8986.3720127/abstract) in 2000.

The Society for Psychophysiological Research published this [Committee report: publication guidelines and recommendations for studies using electroencephalography and magnetoencephalography](http://onlinelibrary.wiley.com/doi/10.1111/psyp.12147/full) in 2013.

The OHBM Committee on Best Practice in Data Analysis and Sharing (COBIDAS) wrote a report on [Best Practices in Data Analysis and Sharing in Neuroimaging using MRI](http://www.humanbrainmapping.org/files/2016/COBIDASreport.pdf). Although this is on (f)MRI, the parts on subjects, tasks and data analysis are also relevant for EEG and MEG. The report was published in [Nature neuroscience](http://www.nature.com/neuro/journal/v20/n3/full/nn.4500.html) in 2017.

The International Pharmaco-EEG Society (IPEG) published their [Guidelines for the Recording and Evaluation of Pharmaco-EEG Data in Man](http://www.karger.com/Article/FullText/343478) in 2012.

If you are doing clinical EEG or MEG, you should check out the [Guidelines and Consensus Statements](https://www.acns.org/practice/guidelines) of the American Clinical Neurophysiology Society (ACNS) and the [guidelines](http://www.ifcn.info/guidelines.aspx?MenuID=1169) of the International Federation of Clinical Neurophysiology (IFCN). The IFCN also refers to the published [Recommendations for the Practice of Clinical Neurophysiology](http://www.clinph-journal.com/content/guidelinesIFCN).

Nature has a [Reporting Checklist For Life Sciences Articles](http://www.nature.com/authors/policies/checklist.pdf) that is helpful to consider when you write your manuscript, also when you don't plan to submit it to Nature.

## Programming

MathWorks provides [online tutorials](https://www.mathworks.com/help/matlab/getting-started-with-matlab.html) to help you get started with the desktop and programming environment.

For an introduction to MATLAB have a look at the excellent tutorial and exercises in [MATLAB for Psychologists](http://www.antoniahamilton.com/matlab.html).

Mike X. Cohen, [MATLAB for Brain and Cognitive Scientists](https://www.amazon.com/MATLAB-Brain-Cognitive-Scientists-Press/dp/0262035820/ref=la_B00EWB0HO2_1_1?s=books&ie=UTF8&qid=1496819058&sr=1-1), MIT Press, 2017.

Wilson G, Aruliah DA, Brown CT, Chue Hong NP, Davis M, Guy RT, et al. (2014) [Best Practices for Scientific Computing](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745). PLoS Biol 12(1): e1001745. https://doi.org/10.1371/journal.pbio.1001745

## Data Sharing

For data sharing we recommend that you consider organizing your data along the lines of the [BIDS standard](http://bids.neuroimaging.io). See [The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments](http://www.nature.com/articles/sdata201644) for an introduction and [MEG-BIDS, the brain imaging data structure extended to magnetoencephalography](https://www.nature.com/articles/sdata2018110). The ** [data2bids](/reference/data2bids)** function helps to organize your data in the BIDS structure.

A good example for a data publication is given in [A multi-subject, multi-modal human neuroimaging dataset](http://dx.doi.org/10.1038/sdata.2015.1), which includes MEG, EEG and fMRI. The dataset itself is available from [OpenfMRI](https://openfmri.org/dataset/ds000117).

The Human Connectome Project (HCP) also provides good examples for data sharing and documentation. In [Adding dynamics to the Human Connectome Project with MEG](https://dx.doi.org/10.1016/j.neuroimage.2013.05.056) the MEG component of the HCP is described, which is available for download from the [HCP website](https://www.humanconnectome.org).

## Signal processing

 [Analyzing Neural Time Series Data: Theory and Practice](http://www.amazon.com/Analyzing-Neural-Time-Data-Neuropsychology/dp/0262019876/ref=la_B00EWB0HO2_1_1?s=books&ie=UTF8&qid=1436709055&sr=1-1). by Mike X. Cohen.

 [Spectral Analysis for Physical Applications: Multitaper and Conventional Univariate Techniques](http://faculty.washington.edu/dbp/sapabook.html) Donald B. Percival and Andrew T. Walden, 1993.

Bruns A. [Fourier-, Hilbert- and wavelet-based signal analysis: are they really different approaches?](http://www.sciencedirect.com/science/article/pii/S0165027004001098) J Neurosci Methods. 2004 Aug 30;137(2):321-32.

The [Brief History of the EEG Surface Laplacian](http://ssltool.sourceforge.net/history.html) by Paul L. Nunez explains how the surface Laplacian and SCD relate. The surface laplacian is further explained on the [EGI website](ftp://ftp.egi.com/pub/documentation/technotes/SurfaceLaplacian.pdf).

## Statistics

The following paper illustrates several problems associated with the lack of robustness and gives recommendations: Rousselet, G.A. & Pernet, C.R. (2012) [Improving standards in brain-behavior correlation analyses](https://www.frontiersin.org/articles/10.3389/fnhum.2012.00119/full). Frontiers in human neuroscience, 6, 119.

The blog post [Correlations in neuroscience: are small n, interaction fallacies, lack of illustrations and confidence intervals the norm?](https://garstats.wordpress.com/2018/06/11/ejn2017) by Guillaume Rousselet has some interesting observations and recommendations.

## Source estimation

Michel, C.M. et al. [EEG source imaging.](http://www.ncbi.nlm.nih.gov/pubmed/15351361) Clin Neurophysiol, 2004; 115(10):2195-222.

Baillet, S and Mosher, J.C. [Electomagnetic Brain Mapping](http://cogimage.dsi.cnrs.fr/hmtc/references/files/BailletMosherLeahy_IEEESPMAG_No.pdf) IEEE Signal Processing Magazine, 2001; November:14-30.

The following paper is a review and gentle introduction into beamformin
Hillebrand A, Singh KD, Holliday IE, Furlong PL, Barnes GR.
 [A new approach to neuroimaging with magnetoencephalography.](http://dx.doi.org/10.1002/hbm.20102) Hum Brain Mapp. 2005 Jun;25(2):199-211.

## Connectivity

Schoffelen JM, Gross J. [Source connectivity analysis with MEG and EEG.](http://onlinelibrary.wiley.com/doi/10.1002/hbm.20745/full) Hum Brain Mapp. 2009 Jun;30(6):1857-65.

O’Neill GC, Barratt EL, Hunt BAE, Tewarie PK, Brookes, MJ. [Measuring electrophysiological connectivity by power envelope correlation: a technical review on MEG methods](https://doi.org/10.1088/0031-9155/60/21/R271). Physics in Medicine and Biology, 2015 60(21), R271–R295.
