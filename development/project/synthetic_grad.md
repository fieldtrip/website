---
title: Implement support for CTF synthetic gradiometers
---

{% include /shared/development/warning.md %}

# Implement support for CTF synthetic gradiometers

## Objectives

1.  Improve accuracy of source reconstructions for synthetic gradient data
2.  Be able to convert the data to and from synthetic gradients

## Step 1: read the coefficients

The coefficients are stored in a site specific .coef file (e.g., /opt/ctf/hardware/M016/M017_1706.coef). Those should **not** be used, instead they should be read from the res4 file (see CTF comments in the appendix).

The coefficients should be put into a Nchan X Nchan matrix, where Nchan = Nref+Nmeg. Assuming that the uncorrected data has been read in for all channels, the conversion of 0th order to 3rd order only requires a multiplication with this matrix.

TODO: This requires looking through the low-level code (ctf_read_res4.m).

## Step 2: apply the coefficients to the data

There should be a matrix for
0th -> 1st (T01)
0th -> 2st (T02)
0th -> 3st (T03)
From those, each matrix can be made by combining the matrices, i.e.
data1 = T01 _ data0;
data2 = T02 _ data0;
data3 = T03 _ data0;
and hence
data0 = inv(T01) _ data1;
data0 = inv(T02) _ data2;
data0 = inv(T03) _ data3;
so for example
data1 = T01 _ inv(T03) _ data3;

TODO: This requires testing on real data using the CTF software as gold standard, i.e. use the newDs command to construct a 1st, 2nd and 3rd order dataset from an original 0th order dataset (only one trial required, e.g., average). Regarding MATLAB code, fieldtrip/syntheticgradient.m performs the conversions of the data.

## Step 3: apply the coefficients to the gradiometer array

The gradiometer array is described by all coil (positions and orientations) and the weights (+1 or -1) to combine the coils into hardware channels. From the FAQ:

_The gradiometer definition generally consists of multiple coils per channel, e.g., two coils for a 1st order gradiometer in which the orientation of the coils is opposite. Each coil is described separately and one large matrix (can be sparse) has to be given that defines how the forward computed field is combined over the coils to generate the output of each channel. The gradiometer definition consists of the following fields_

    grad.pnt   % Mx3 matrix with the position of each coil
    grad.ori   % Mx3 matrix with the orientation of each coil
    grad.tra   % NxM matrix with the weight of each coil into each channel
    grad.label % cell-array of length N with the label of each of the channels (magnetometers or gradiometers)

The low-level forward computation code computes the field on each coil for a dipole in the x, y, and z-direction. That field (Ncoils x 3) is multiplied with the grad.tra matrix. Hence, to compute the forward model for synthetic gradients, it is sufficient to multiply this with the T03 matrix, i.e.

    grad.tra0 =       grad.tra;
    grad.tra1 = T01 * grad.tra;
    grad.tra2 = T02 * grad.tra;
    grad.tra3 = T03 * grad.tra;

gives the linear combination of the simulated field at all coils to form the synthetic gradients at the channels.

TODO: This requires a smarter implementation for linking the local spheres (one per channel) to the single channels (each channel combines 2 coils in the original 0th order data, but much more coils in the synthetic 3rd order data). The meg_leadfield1() function requires one sphere per coil, i.e. the coils and spheres have to be linked. Currently that gives an (intentional) error when it detects a higher order synthetic gradiometer array (fieldtrip/private/prepare_vol_sens.m, line 248).

## Step 4: ensure that the gradiometer order is defined in the data

The res4 file should specify somewhere how the raw data has been written (i.e. with 0th, 1st, 2nd or 3rd order balancing). That information should be added to the dataset in MATLAB memory, and the gradiometer structure (grad.tra) should be consistent.

When changing the balancing (e.g., using the fieldtrip/ft_denoise_synthetic.m function), the data structure should remain internally consistent and should describe the balancing.

TODO: think of a way of adding this information to the output of fieldtrip/preprocessing and related functions (e.g., have a field data.grad.order='G1BR').

## Appendix: description from CTF

The sensor and coefficient information should ALWAYS be read from
the dataset (i.e., '.res4' file). This will guarantee that the sensor and
coefficient information are the corrected ones at the time the data was
collected (or modified).

To iterate, never use the '.sens' and/or '.coef' files. There is no
guarantee that the current '.sens' and/or '.coef' files are appropriate for
existing dataset.

The sensor positions in the '.sens' file is ALWAYS relative to the dewar
coordinates. The sensor positions in the dataset's '.res4' file are
specified in both dewar coordinates and head coordinates. You should use the
one in head coordinates. (As noted above, DON'T USE THE '.sens' FILE).
Our coils are 1st order gradiometers. Synthetic 2nd and 3rd order
gradiometers are formed using information >from the references. See below for
details on synthetic gradiometers.
To simulate (forward compute) the 1st gradiometer, the order of summing over
each coil doesn't matter (if you follow the steps prescribed below).

## Simulating data / forward solution computation

Each sensor is described by:

- one or more coils
- zero or more baselines
- signed gain

Each coil is described by:

- position of centre of coil (use the position relative to head coordinate system)
- number of turns (N)
- coil area (A)
- unit normal vector (p) (use the position relative to head coordinate system)
- baseline from previous coil (for coils other than the first)

To compute the "field" picked up by a sensor

1. Compute and sum the flux picked up by each coil.
2. To convert from flux to "field", divide the total flux by the effective
   area (N \* A) of the sensing coil (i.e., the first coil).
3. Here is the confusing part.... Our internal polarity definition is
   opposite of the general convention, thus to get the polarity of the
   simulated data consistent with the measured data, you have to apply the
   opposite polarity (of the signed gain) to the simulated data. Therefore if
   the sensor's gain is positive, you have to invert the simulated data; if the
   sensor's gain is negative, leave the simulated data alone.

Note: If you are working with data with 'Tesla', you don't need to use the
gain value, just it's sign (as per step 3 above).
To compute the flux picked up by a coil, take the projection of the field
vector onto the coil's unit normal vector. That is,
Flux(at coil i) = N[i] _ A[i] _ Dot(B,p[i]),
where B is the field vector of your simulated signal source at the center of
coil i.
N[i] = number of turns of coil i
A[i] = area of coil i
p[i] = unit vector normal to area of coil i.
Total flux(of sensor) = Sum{ flux[coil i], i = 1 to number of coils}.
If you are integrating over the coil area, the procedure is similar.

## Reading and using coefficients

If directly reading the coefficients from the dataset's '.res4'
file (or from the '.coef' file too), then the coefficients are Phi0 data.
Thus if the data is in Tesla, then you will have to convert the coefficients
to be relevant to Tesla as well. To do this, use the formula
CoefOfRefInTesla = CoefOfRefInPhi0 _ gainOfRef / gainOfSensor
For example, if the 3rd gradient coefficients for sensor MLC11 are (for Phi0
data
BG1: cBG1
BG2: cBG2
BG3: cBG3
G11: cG11
...
and the gains of the references and sensors ar
BG1: gBG1
BG2: gBG2
...
MLC11: gMLC11
...
Then the coefficients for MLC11 corresponding to Tesla data ar
BG1: cBG1 _ gBG1 / gMLC11
BG2: cBG2 _ gBG2 / gMLC11
BG3: cBG3 _ gBG3 / gMLC11
G11: cG11 \* gG11 / gMLC11
...
Example
G3OI coefficient for data in phi0 for MLC1
G11 (G11-1105): 0.143393
G12 (G12-1105): -0.00166001
G13 (G13-1105): -0.129106
G22 (G22-1105): -0.136122
G23 (G23-1105): 0.0653427
P11 (P11-1105): 0.00202835
Q11 (Q11-1105): -0.00211531
Q13 (Q13-1105): 0.265981
R11 (R11-1105): -0.127228
R12 (R12-1105): -0.00188768
R13 (R13-1105): 0.13007
R22 (R22-1105): 0.0777415
R23 (R23-1105): 0.330706

G3OI coefficient for data in Tesla for MLC1
G11 (G11-1105): -0.285225
G12 (G12-1105): 0.00313698
G13 (G13-1105): -0.241933
G22 (G22-1105): -0.270226
G23 (G23-1105): -0.125866
P11 (P11-1105): 0.00393464
Q11 (Q11-1105): -0.0039391
Q13 (Q13-1105): 0.477763
R11 (R11-1105): -0.238921
R12 (R12-1105): -0.00330739
R13 (R13-1105): -0.234992
R22 (R22-1105): -0.145796
R23 (R23-1105): 0.602411

The coefficients are applied by SUBTRACTING the linear combination of
reference signals from the sensor signal. E.g.,
MLC11(3rd) = MLC11(raw) - Sum{ ref[i] \* coef[i], i=1 to num of references}

## Ideal vs Real coefficients (G3OI vs G3BR).

The ideal coefficients are based on geometry of the sensor configuration.
The real coefficients accounts for geometrical and common mode errors; these
are determined experimentally.

## For DipoleFit AND dfit VERSION 4.12 and up

We use the real coefficients for both processing real data and forward solution
computation. Recent studies at CTF showed that using the real coefficients for the
forward solution computation gave a more accurate match with the real data compared
to the using the ideal coefficients.
