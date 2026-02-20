---
title: SR4 - Source reconstruction
tags: [neuroimaging2-2425]
---

## 7 Modelling EEG/MEG activity using distributed sources

This document contains the MATLAB exercises that form part of the course “Neuroimaging
II” relating to the minimum norm inverse methods for underdetermined systems.

The best way to approach the exercises is to create a MATLAB-script that can
be used to copy-and-paste the MATLAB-code in the instructions, and allows you
to play around with various parameter settings etc. You can open a new script
in the MATLAB-editor by typing edit on the command line, or by going to File->New->Script.
Next, you can save each script as a separate file in your course folder.

Set up the MATLAB path

    ni2_startup
    ft_version

_If we have measured data and a pre-computed leadfield (based on known sensor
positions and a volume conductor model), then we would like to compute an estimate
of the sources. Many methods use a linear matrix to compute this 'inverse solution’,
as a linear weighting of the senors to compute activity at a source location.
Throughout this homework, the equation representing the data and model is `y=L*s+N`.
Here, `y` is the sensor data, `L` is the known leadfield, `s` is the source
amplitude or dipole moment and N is the sensor noise._

_With distributed source models and the minimum norm solution the observed
data is assumed to be determined by a mixing of many active sources, where the
number of active sources is much higher than the number of observed channels.
This leads to an underdetermined problem, and one way to solve this is to assume
that a good guess of the distribution of the source amplitudes has the lowest
possible norm. One important feature of distributed source models is the fact
that the amplitudes of the individual sources are estimated in a single inversion
step._

### 7.1 Underdetermined linear systems of equations

For non-unique solutions (underdetermined systems) we can use the minimum
norm of the overall source strength as additional constraint.

After this section, you will

- Understand that multiple solutions exist for an underdetermined system
- Understand that the pseudo-inverse of the leadfield matrix gives the solution
with the minimum-norm of the source power

First begin with a 'toy’ composite leadfield matrix. It represents 3 source
locations and 2 sensors.

    L = [1 0 1;
         0 1 1];

Although it is an unrealistic example, it is useful to gain some intuition.
Let’s assume the data `y` we measured at a single time point is

    y = [2 1]';

Now we want to solve for what the source amplitude `s` is, given this data
`y` and given the known leadfield `L`.

Assume no noise `N` for now, so the equation is `y = L*s`.

This matrix multiplication essentially is a linear system of equations, where
the number of equations is 2 (in general: the number of rows in the leadfield
matrix), and the number of unknowns is 3 (in general: the number of columns
in the leadfield matrix. This never has an unique solution; there are many solutions
that satisfy this equation. Let’s first explicitly rewrite the matrix multiplication.
Refresh your understanding of matrix multiplication if needed.

    y(1) = L(1, 1)*s(1) + L(1, 2)*s(2) + L(1, 3)*s(3); % equation 1
    y(2) = L(2, 1)*s(1) + L(2, 2)*s(2) + L(2, 3)*s(3); % equation 2

Filling in the numbers, we get:

    y(1) = 1*s(1) + 0*s(2) + 1*s(3) = 2
    y(2) = 0*s(1) + 1*s(2) + 1*s(3) = 1

where s(1), s(2) and s(3) are the unknowns.

Note that equation 1 represents a matrix multiplication of the first row of
the leadfield matrix with the source vector, and that equation 2 represents
the matrix multiplication of the second row of the leadfield matrix with the
source vector. Note, also, that we have more unknowns (3) than equations (2).
In other words, we could take an arbitrary value for, say, s(3), and we will
still be able to find a valid solution to the linear system of equations.

By analogy, you may remember from high school geometry, that equations with
3 unknowns describe a plane in 3-dimensional space, and that 2 planes (if they
are not parallel) intersect in a line. This line represents all valid solutions
to the linear system of equations.

In this toy example, it is very straightforward to parameterize the solution.
Let’s call the value that we take for s(3) the value `a`. Using this substitution,
and applying it to the equations above, we get:

the variable a can be anything, so let's give it a random value
    a = rand(1)

note that vector s should be a column-vector, not a row-vector
    s(1,1) = 2-a;
    s(2,1) = 1-a;
    s(3,1) = a;

**_Q7.1.1 - Show that this solution for `s` satisfies the linear system of
equations when a=0._**

**_Q7.1.1 - Show that this solution for `s` satisfies the linear system of
equations when a=100._**

We will use this parameterization in the next section.

### 7.2 The 'best’ solution based on additional constraints: minimize norm.

In the example presented above, mathematically it is equally valid to take
a value of 1 for a, as it is to take a value of 100. The former will yield source
amplitudes of (1, 0, 1), whereas the latter will yield source amplitudes of
(-98,-99, 100).

It may be realistic to assume that the source activity measured at any given
instant by MEG/EEG is primarily due to active sources that are moderately active
(a=1). The alternative would be that all sources would be highly active (a=100).
A mathematically convenient and biologically plausible constraint is to minimize
the total power of the sources across the brain (rather than taking the amplitude,
we minimize for the amplitude squared). The sum of the power of the sources
across the brain is also called the L2-norm; the sum of the amplitudes of the
sources across the brain is represented by the so-called L1-norm.

To compute the L2-norm, we take the square root of the sum of the squares
of each element in the vector. Here’s an example of source amplitude over 3
source locations:

    s = [0 -1 2]';

The source power (L2 norm) can be computed in a variety of ways in MATLAB:

    snorm1 = sqrt(s(1)^2+s(2)^2+s(3)^2)
    snorm2 = sqrt(sum(s.^2))
    snorm3 = sqrt(s'*s)
    snorm4 = norm(s)

**_Q7.2.1 - Compute and write down the L2-norm_**

Rather than trying out random values for `a` to find the solution that yields
the lowest source norm, we can use the parameterization that we defined in the
previous section:

    snorm = sqrt(s(1)^2+s(2)^2+s(3)^2)

Filling in the parameterization we obtained in section 2.1, we get:

    snorm = sqrt((2-a)^2+(1-a)^2+a^2);

Rearranging the terms, we get:

    snorm = sqrt((4-4*a+a^2)+(1-2*a+a^2)+a^2);
    snorm = sqrt(3*a^2-6*a+5);

**_Q7.2.2 - Compute and write down the L2-norm for a=1 and for a=100._**

Ignoring the square root, we need to minimize `(3*a^2-6*a+5)` which can be
done in a variety of ways, e.g. using the ABC-formula (https://en.wikipedia.org/wiki/Quadratic_formula)
to find the minimum of a parabolic equation, or by taking the derivative of
this equation and finding the point along the x-axis where the derivative of
the parabolic function is 0.

**_Q7.2.3 - Take the function `f(a)=3*a^2-6*a+5` and compute its values for
the variable "a" ranging from -100 to +100 in small steps. Make a plot of f(a)
versus a._**

**_Q7.2.4 - What is the smallest value of f(a), and for which value of a is
that value observed?_**

### 7.3 Inverting leadfield matrices

For situations with more than just a few sensors and a few sources, it is
too tedious to solve the system of equations for the unknown values by hand.
Fortunately, we can use matrix algebra to solve large systems of equations,
and let the computer do the work.

First, by mean of a detour, let’s have a look at the following equation:

    y = 3*s

If we want to solve this (very simple system of linear equations) for `s`
(the source amplitude), assuming that we know `y`, we simply divide each side
of the equation by 3, so we get:

    1/3 * y = s

Instead of dividing each side of the equation by 3, we can also say that we
are multiplying each side of the equation by 1/3. 1/3 is also known as the 'inverse’
of 3, which can also be written as 3^-1. When we are dealing with matrices,
the same logic applies:

           Y =      L * S
    L^-1 * Y = L^-1 L * S  
    L^-1 * Y =          S

Here `L^-1*L = I`, where the matrix `I` is the identity matrix, all zeros
off the main diagonal and  all ones on the diagonal; this is the matrix equivalent
of the number "1".

The above equation however only works in a very limited number of cases. The
reason is that a matrix inverse is only defined for square matrices (i.e., in
our case we would need an equal number of channels and sources), where moreover
the leadfield matrix must fulfill the mathematical property that it is actually
invertible.

We can use the so-called pseudo-inverse of a matrix to get a solution to the
linear system of equations. The term 'pseudo’ refers to the fact that the matrix
you get after taking the pseudo-inverse behaves a bit like an inverse matrix,
but not exactly.

The pseudo-inverse in this case can be computed in math formulation as:

     Lpinv = L' * (L*L')^-1

The MATLAB pinv function achieves the same:

    help pinv
    Lpinv = pinv(L)

In contrast to a proper inverse matrix, where both `A*A^-1 = I` and `A^-1*A
= I`, the pseudoinverse exists in only one direction. This can be easily seen
when inspecting `Lpinv*L` and `L*Lpinv`.

**_Q7.3.1 - Compute and write down both `Lpinv*L` and `L*Lpinv`._**

The first one does not result in an identity matrix. The second equation results
in an identity, because it is equivalent to `(L*L')^-1 * (L*L')`. The matrix
products between the brackets are the same, both form a square matrices and
they happen to be in general invertible, thus the product between the inverse
of that product with itself will yield `I`.

**_Q7.3.2 - What happens if you try to compute the normal inverse (using the
inv function) of matrix L?_**

### 7.4 Pseudo-inverse of the leadfield gives minimum norm

The pseudo-inverse is not only a clever mathematical way of computing a new
matrix that, when multiplied with the original in the correct order, gives back
the identity matrix. It happens to be a solution to the underdetermined linear
system of equations that yields the minimum norm.

The proof for this can be derived by first showing that it is a particular
solution; subsequently we show that there is no other solution that has a norm
smaller than the one derived using the pseudoinverse.

We know that there are many possible solutions for the equation `y = L*s`.
Let us use a capital `S` from now on to facilitate formatting; we will use `Sx`
to indicate S with the subscript `x`. If we just take two possible solutions,
`Sm` and `Sx`, where `Sm` happens to be `L'*(L*L')^-1 * y` and `Sx` being any
random other solution, we know that both `L*Sm` and `L*Sx` yield `y`.

Thus, `L*Sm = L*Sx`, or equivalently `L*(Sm-Sx) = 0`.

Remember from section 2.2 that the norm of the solution can be computed from
`s'*s`. This latter equation computes for each of the sources the square of
the amplitude, and sums across sources. To actually get the norm, we would also
have to take the square root of the result, but let’s not do this for now, and
look at the squared norm. Likewise, we can do `(Sx-Sm)'*Sm`, where we compute
for each of the sources the product between the amplitude modeled in `Sm` and
the amplitude difference between `Sx` and `Sm`, and sum this across sources.
Substituting `L'*(L*L')^-1 * y` for the second `Sm` in the equation, we get:

    (Sx-Sm)' * Sm                   =
    (Sx-Sm)' * L'   * (L*L')^-1 * y =
    ( (Sx-Sm)' * L')  * (L*L')^-1 * y =
    (  L * (Sx-Sm) )' * (L*L')^-1 * y =   
    0            * (L*L')^-1 * y =  0

Shuffling the brackets, we focus on the first 2 terms, where we can use the
general matrix property that `A'B'=(BA)`.

Above we already concluded that `L*(Sx-Sm)` is 0, so we can also conclude
that `(Sx-Sm)'*Sm` is 0. This is because we can fill in a 0 in the last equation,
and 0 times something else will be 0.

Now considering the squared norm of `Sx`, which is `Sx'*Sx`, we can apply
a little trick: instead of using `Sx`, we use `((Sx-Sm)+Sm)`. The latter is
of course exactly the same as `Sx`.

    Sx'             *   Sx                                  =
    ((Sx-Sm)+Sm)'   * ((Sx-Sm)+Sm)                          =
    (Sx-Sm)'*(Sx-Sm) + (Sx-Sm)'*Sm + Sm'*(Sx-Sm) + Sm'*Sm

Using our previous result `(Sx-Sm)'*Sm=0`, we get

    (Sx-Sm)'*(Sx-Sm) + (s-Sm)'*Sm + Sm'*(Sx-Sm) + Sm'*Sm    =
    (Sx-Sm)'*(Sx-Sm) + 0          + 0           + Sm'*Sm    =
    (Sx-Sm)'*(Sx-Sm) +                            Sm'*Sm

or

    Sx'*Sx = Sm'*Sm + (Sx-Sm)'*(Sx-Sm)

The last equation tells us that the squared norm of `Sx` is always the sum
of the squared norm of `Sm` _plus_ the squared norm of the difference between
`Sx` and `Sm`.

Since squared numbers are greater than or equal to zero, we can conclude that
the norm of `Sx` is always larger than or equal to to the norm of `Sm`. Hence,
`Sm` must represent the solution with the minimum norm.

### 7.5 The real deal - start simple with simulated data without noise

After this section you will

- Have a basic understanding of how the minimum norm reconstruction works in practice.
- Understand why the minimum norm reconstruction tends to overemphasize activity from superficial sources.
- Know how to counteract the tendency for overemphasizing the superficial sources.
- Understand that noise in the data projects onto the estimated sources.
- Know how to counteract the contamination of the estimated source activity by the noise.

We start by simulating some MEG data that contains two active sources.

    [activity1, time1] = ni2_activation;
    [activity2, time2] = ni2_activation('frequency', 11, 'latency', 0.48);

    sensors = ni2_sensors('type', 'meg');
    headmodel = ni2_headmodel('type', 'spherical', 'nshell', 1);

    leadfield1 = ni2_leadfield(sensors, headmodel, [ 4.9 0 6.2 0 1 0]); % close to position 2352 in grid
    leadfield2 = ni2_leadfield(sensors, headmodel, [-5.3 0 5.9 1 0 0]);

    sensordata = leadfield1*activity1 + leadfield2*activity2;

Try and understand the steps above. Pay particular attention to the parameters
of the simulated dipoles.

We now proceed to generate a MATLAB data-structure that FieldTrip understands.
This "structure" is a collection of MATLAB-variables, organized in so-called
fields, that belong together. An important aspect of these FieldTrip data structures
is that the numeric data that is represented (in our case in the 'avg’ field)
is accompanied by all information necessary to interpret this numeric data.
For example, there is a field called 'time’, that indicates each time sample
in seconds (i.e., it maps the columns of the 'avg’ field on a physical time
axis). The 'label’ field specifies the name of each channel (and tells us which
row in the 'avg’ field belongs to which channel).

    data        = [];
    data.avg    = sensordata;
    data.time   = time1;
    data.label  = sensors.label;
    data.grad   = sensors;
    data.cov    = eye(numel(sensors.label));
    data.dimord = 'chan_time';

Next we will make a source reconstruction using the 'mne’ method of FieldTrip’s
ft_sourceanalysis function. Before we can do this, we need to define our source
model, i.e., the set of locations that we assume to be active. For now we assume
that the active dipoles are distributed on a regular 3D grid, with a spacing
of 1 cm between the dipoles:

    sourcemodel = ni2_sourcemodel('type', 'grid', 'resolution', 1);

    cfg                    = [];
    cfg.sourcemodel        = sourcemodel;
    cfg.headmodel          = headmodel;
    cfg.method             = 'mne';
    cfg.mne.prewhiten      = 'yes';
    cfg.mne.scalesourcecov = 'yes';
    cfg.mne.lambda         = 0;
    cfg.keepleadfield      = 'yes';
    source = ft_sourceanalysis(cfg, data);

Let’s now have a look at the reconstructed source activity.

**_Q7.5.1 - What is the position of grid point 2352?_**

For each dipole location in the distributed source model, the estimated activity
is represented in the source.avg.mom field. We can easily use the MATLAB plot
command to visualize this:

    figure; plot(source.time, source.avg.mom{2352}); legend({'Sx' 'Sy' 'Sz'});

**_Q7.5.2 - In which direction is the dipole moment of this source at grid
location 2352 the largest?  Is that consistent with the model that generated
the data?_**

**_Q7.5.3 - What is the index of the grid point that is the closest to the
other dipole that we used in the model to generate the data?_**

Ignoring the dipole orientation and time course of the activity, we can plot
the spatial distribution of the dipole strength that is represented in `source.avg.pow`,
which represents the squared amplitude for each time point.

    cfg = [];
    cfg.funparameter = 'pow';
    cfg.location = sourcemodel.pos(2352,:);
    cfg.funcolorlim = 'maxabs';
    figure; ft_sourceplot(cfg, source);

The initial time point of which the spatial topography is plotted is t=0,
and at that moment there is no activity at all, hence the completely green distribution.
Click on the source time course in the lower right to select a time point at
which the activity in grid location 2352 peaks.

**_Q7.5.4 - What happens with the spatial distribution of the source power
in-between two peaks at location 2352? Explain._**

This simple noise-less example illustrates two important things. First, activity
is 'smeared’ out over various dipole locations and orientations. Second, the
estimated activity at a location closer to the sensors than the location at
which activity was simulated has a higher amplitude than the activity estimated
at the location where activity was simulated. We will return to this feature
of the minimum norm reconstruction in a later section.

### 7.6 Simulated data with noise

Let’s now simulate MEG sensor data with added noise:

    [activity1, time1] = ni2_activation;
    [activity2, time2] = ni2_activation('frequency', 11, 'latency', 0.48);

    sensors = ni2_sensors('type', 'meg');
    headmodel = ni2_headmodel('type', 'spherical', 'nshell', 1);

    leadfield1 = ni2_leadfield(sensors, headmodel, [ 4.9 0 6.2 0 1 0]); % close to position 2352 in grid
    leadfield2 = ni2_leadfield(sensors, headmodel, [-5.3 0 5.9 1 0 0]); % close to position 2342 in grid

    sensordata = leadfield1*activity1 + leadfield2*activity2 + randn(301, 1000)*.7e-10;

Create a FieldTrip data structure:

    data        = [];
    data.avg    = sensordata;
    data.time   = time1;
    data.label  = sensors.label;
    data.grad   = sensors;
    data.cov    = cov(randn(301, 1000)'*.7e-10);
    data.dimord = 'chan_time';

In the field 'cov’ we create a covariance matrix that was designed to represent
the covariance of the noise in the data. This will be a relevant item when we
will discuss noise regularisation.

    sourcemodel = ni2_sourcemodel('type', 'grid', 'resolution', 1);

Do the source reconstruction:

    cfg                    = [];
    cfg.sourcemodel        = sourcemodel;
    cfg.headmodel          = headmodel;
    cfg.method             = 'mne';
    cfg.mne.prewhiten      = 'yes';
    cfg.mne.scalesourcecov = 'yes';
    cfg.mne.lambda         = 0;
    cfg.keepleadfield      = 'yes';
    source_noise = ft_sourceanalysis(cfg, data);

The `cfg.mne.lambda` option was set to 0. This means that the inverse solution
fits all data perfectly, where the data not only includes the activity from
the sources of interest, but also contains noise.

We can again make a plot of the spatial distribution of power in the brain
for each time point.

    cfg = [];
    cfg.funparameter ='pow';
    cfg.location = sourcemodel.pos(2352,:);
    cfg.funcolorlim = [-2 2]*1e-3;  % set the color limits manually
    figure; ft_sourceplot(cfg, source_noise);

**_Q7.6.1 - Select a good latency and click around in the volume; can you find
a location that shows the expected temporal pattern of activity?_**

We can use a non-zero lambda to compute a regularized minimum norm estimate,
where this lambda parameter is used to quantify the contribution of the noise
to the measured signals.

The larger the value for lambda, the stronger the assumed noise. In combination
with the regularization parameter, a regularized minimum-norm estimate also
requires an estimate of the noise covariance matrix. This matrix represents
the spatial structure in the noise. The noise covariance matrix can be estimated
from the data, but experimenters sometimes also use an identity matrix. The
latter strategy assumes implicitly that each channel in the data gets the same
amount of uncorrelated noise.

Do the source reconstruction with regularisation:

    cfg                    = [];
    cfg.sourcemodel        = sourcemodel;
    cfg.headmodel          = headmodel;
    cfg.method             = 'mne';
    cfg.mne.prewhiten      = 'yes';
    cfg.mne.scalesourcecov = 'yes';
    cfg.mne.lambda         = 0.5;
    cfg.keepleadfield      = 'yes';
    source_noise_reg = ft_sourceanalysis(cfg, data);

    cfg = [];
    cfg.funparameter = 'pow';
    cfg.location = sourcemodel.pos(2352,:);
    cfg.funcolorlim = 'maxabs';
    figure; ft_sourceplot(cfg, source_noise_reg)

Another way to explore the effect of regularisation is to look at the residuals
of the model. This can be obtained in the following way:

    L = cat(2, source_noise_reg.leadfield{source_noise_reg.inside});
    S = cat(1, source_noise_reg.avg.mom{source_noise_reg.inside});
    model = L*S;
    residual = sensordata-model;

**_Q7.6.2 - Show that the residual for the source_noise condition without regularization
is zero and share your figure here. Note the limited numerical precision of
the computer that might cause some numerical inaccuracy to remain._**

### 7.7 Minimum-norm estimates 'overestimate’ the amplitude of superficial sources

As we have seen in the previous sections, the minimum-norm estimate has a
tendency to over-estimate the amplitude of dipoles that are close to the surface.
This feature is a direct consequence of the minimum-norm constraint. In order
to explain all measured data with a source model that has the lowest possible
norm, the deep sources will be penalized more because these need to have a strong
activation in order to be picked up by the MEG sensors in the first place.

    cfg                    = [];
    cfg.sourcemodel        = sourcemodel;
    cfg.headmodel          = headmodel;
    cfg.method             = 'mne';
    cfg.mne.prewhiten      = 'yes';
    cfg.mne.scalesourcecov = 'yes';
    cfg.mne.lambda         = 0.5;
    cfg.keepleadfield      = 'yes';
    cfg.normalize          = 'yes';
    cfg.normalizeparam     = 1;
    source_noise_lfnorm    = ft_sourceanalysis(cfg, data);

    cfg = [];
    cfg.funparameter = 'pow';
    cfg.location = sourcemodel.pos(2352,:);
    cfg.funcolorlim = 'maxabs';
    figure; ft_sourceplot(cfg, source_noise_lfnorm)

**_Q7.7.1 - Explain the effect that is achieved by the leadfield normalization
(cfg.normalize='yes')._**

**_Q7.7.2 - Is the resulting spatial distribution an accurate representation
of the (in this case known) underlying source activity?_**
