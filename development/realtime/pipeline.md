---
title: Pipeline architecture
---

At the moment, this is a collection of ideas about how to implement an easy-to-use and flexible pipeline architecture for online processing of data. It's also quite fMRI-centric so far.

## General layout of a pipeline

A pipeline needs to handle a stream of data and consists of multiple elements. Usually those elements will act
sequentially on the data, that is, the original data stream is fed into the first pipeline element (PE) in small blocks,
processed there, and the output of the first element is fed as input to the second element and so on.

    input -> [PE 1] -> [PE 2] -> ... -> [PE N] -> output

In some situations it might be desirable to split the pipeline and be able to run some PEs in parallel,
but we will ignore this for now.

## Examples of (fMRI) pipeline elements

### Motion correction

This PE needs to be initialised with a reference volume and some optional flags such as the degree of smoothing or the type of interpolation for re-slicing.
Given a volume Vs as an input, the output of this PE is the aligned (re-sliced) volume Va plus the estimated motion. Also, typically the user will want to
keep track of a mask of voxels that are valid in all processed volumes.

Often the reference volume will be identical to the first volume in the series that is to be processed. In this way, parts of the initialisation actually
happen during processing of the first data block.

### Slice time correction

This PE needs to be initialised with a vector of slice timings and possibly a "0th scan" for interpolating the first proper scan. Both input and output are volumes,
but in addition, this PE always needs to remember the last volume to be able to process the next.

### Smoothing

Both the input and the output is a single volume. Fully described by smoothing kernel, no state to be kept.

### Online GLM

Can be seen as a PE with input consisting of a volume and a row of the design matrix. Could output the residual variance not explained by the regressors up to that point. Will need to update and keep track of various statistics (inverse Hessian, regression coefficients, ...).

### Quality assurance display

Can be seen as a PE that turns the input (volume + motion estimate) into a MATLAB figure, but does not output anything (but it can output the unmodified input volume, or maybe a mosaic representation with re-ordered slices). Needs to keep track of older motion estimates, and possibly statistics about signal-to-noise, variation in the scans, or other things.

## Common properties

All PEs need an **init** and a **process** routine. The type of inputs and outputs varies between PEs, but it seems we could pass around a MATLAB "struct" with a "data" field that is always present. On top of that, each PE can add further output fields, but it should always pass on the fields it received from the previous PE, because succeeding PEs might need those fields (e.g., consider the pipeline [motion correction] -> [slice time correction] -> [quality display] where the motion estimates need to
be passed on, although they are not used by the slice time correction PE).

Further to that, most PEs need an internal state representation that can be updated during **process**.

Optionally, it might be useful to have a **finalize** method for all PEs, in which their internal state can be written to a file (e.g., for saving the estimated head movement after an experiment).

## Possible implementations

We'd like the flexibility to compose pipelines in any order and with any number of elements, and then run the pipeline like this

**init** phase

    PE{1} = init X
    PE{2} = init Y
    ...

**process** phase

    tmp = PE{1}(input)
    for k=2:N
      tmp = PE{k}(tmp)
    end
    output = tmp;

In order to avoid a clash of fieldnames for the "tmp" structure passed from one PE to the next, output fields other than the data itself
should be written to uniquely names subfields, e.g., the motion correction PE could write its output as

  tmp_out.data = aligned_volume;
  tmp_out.motion_correction.rotation; % estimated rotation parameters
  tmp_out.motion_correction.translation; % estimated translation parameters

We could add a pre-flight run similar to BCI2000 where each PE does some pseudo-processing and then writes its output fields,
so that the pipeline can check itself for consistency: For example, the quality display PE needs to be placed behind the motion correction PE,
and thus it should check for the existence of the "motion_correction" sub-structure. Or we just keep it simple and leave a sensible
composition of pipelines to the user ;-)

### OOP solution

It seems natural to represent each PE by an object of a specific class, where all classes inherit from a common superclass (describing only the **init** and **process** interface). If we go for OOP, we need to decide on whether to use a) old style classes, b) new style classes, or c) new style handle classes. This has consequences for the organization of the code, the way PEs are invoked, and last but not least on the compatibility with different MATLAB versions.

#### Old style classes

Each type of PE would get its own directory, e.g., @MotionCorrection, with separate files for the constructor (~**init**), the **process** routine, and possible getter/setter methods and helper routines. Invoking this pipeline would be like this

    MCPE{k} = MotionCorrection(refVolume, flags);
    ...
    [MCPE{k}, tmp_out] = MCPE{k}.process(tmp_in);

Here, out.data contains aligned scan, out.someFieldOrSubStruct contains motion estimates, and MCPE gets updated by copying.

#### New style classes (call by value)

Each type of PE would get one class definition file, containing all code. Invoking this pipeline would be like this

    MCPE = MotionCorrection(refVolume, flags);
    ...
    in.data = rawScan;
    ...
    [MCPE, out] = MCPE.process(in);

#### New style handle classes (call by reference)

Each type of PE would get one class definition file, containing all code. Invoking this pipeline would be like this

    MCPE = MotionCorrection(refVolume, flags);
    ...
    in.data = rawScan;
    ...
    out = MCPE.process(in);

Here, MCPE does not need to be copied.

### Pseudo-OOP solution

We could also write normal imperative code with different processing functions such as **motion_correction_process**, and then, during initialisation,
set a function handle to the right function.

    MCPE = motion_correction_init(refVolume, flags);
    MCPE.process = @motion_correction_process; % will usually happen within the *_init call
    ...
    [MCPE, out] = MCPE.process(MCPE, in);

### Plain function table solution

As long as we only have one **process** functions, we can also build a simple table like this:

    PE{1} = motion_correction_init(refVolume, flags);
    procFunc{1} = @motion_correction_process;
    PE{2} = slice_time_corr_init(deltaT);
    procFunc{2} = @slice_time_corr_process;
    ...
    for k=1:N
      [PE{k}, tmp_out] = feval(procFunc{k}, PE{k}, tmp_in);
    end

If you like tables, please consider [brainstream](/development/realtime/brainstream).
