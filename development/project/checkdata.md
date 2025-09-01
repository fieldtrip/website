---
title: Clean up the code of sourceanalysis, sourcedescriptives, freqdescriptives using checkdata
---

{% include /shared/development/warning.md %}


- Ad sourceanalysis:

the bookkeeping of the data is quite complicated. Identify commonalities and differences between different inputs (time-domain data vs. frequency-domain data), and the different methods (pcc vs. dics initially, also lcmv eventually). For this, a more consistent representation of the data from the input side is required. Candidate function to take care of this will be checkdata. After calling checkdata, the input data will be converted into something containing a covariance/csd, and potentially trial-data (timelocked or fourier coefficients). This will make prepare_freq_matrices superfluous eventually.

- Ad sourceanalysis:

the output structure should become more fieldtrippish: i.e. contain a dimord. Get rid of the .avg and .trial fields (also for sourcedescriptives). Check the consequences with respect to avgA and avgB fields. If source is to describe a 3D-volume with inside voxels, allow for (sparse) cell-arrays; let dimensionality of cell-array prevail over dimensionality of the individual cells. If the source is to describe a list of positions (all insides) a matricial representation is more efficient.

- Ad sourcedescriptive

from previous changes the data representation will be much less complicated, allowing for a cleaner implementation.

- Ad sourcedescriptives/freqdescriptives:

identify commonalities in required functionality. With more consistent data representations sharing of common code will be the goal.

- Ad everything:

if necessary, sacrifice backward compatibility but try to limit this as much as possible.

Follow up Jan 29 2010

Detailed plan for tackling the cleaning up of the source-structure format will be as follows:

- Source structure will be defined as follow

  - source.pos [Nx3] (or [Nx(3*m)]) positions of dipole locations
  - source.dim (optional) if the positions represent a 3D volume
  - source.trial and source.avg (trialA, trialB, avgA, avgB) will not be supported anymore
  - all voxel-specific data will be stored as a field (not as a subfield), each with its own
    dimord, e.
    > source.pow [NxnFreqxnTime] / source.powdimord = 'pos_freq_time'
    > source.pow [nRptxNxnFreq] / source.powdimord = 'nrpt_pos_freq'
    > source.leadfield {N,1}[nChanx3] / source.leadfielddimord = '{pos}\_chan_ori'
    > source.csd {N,1}[3x3] / source.csddimord = '{pos}\_ori_ori'

- The following steps have to be taken in this order:

  - adjust checkdata to be able to make conversion between old-style source data an new-style source data
  - create new functions 'parallel' to the existing ones, starting from the back of the analysis pipeline to allow for a smooth transition and to enable us to commit code throughout the re-structuring
  - sourcestatistics (without using statistics_wrapper)
  - sourcedescriptives
  - sourcegrandaverage/parameterselection/source2full/source2sparse/volumeXXX)
  - sourceanalysis

- Grep all functions which call parameterselection/getsubfield, because they may lead to conflicts since these functions then possibly rely on the old-style source format.
