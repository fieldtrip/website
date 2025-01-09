---
title: How does the CTF higher-order gradiometer work?
parent: Specific data formats
category: faq
tags: [ctf]
redirect_from:
    - /faq/how_does_the_ctf_higher-order_gradiometer_work/
---

# How does the CTF higher-order gradiometer work?

The following is taken from the CTF documentation "MEG File Formats - release 5.2.1" appendix C.

\_Higher-order gradiometer formation is a noise-cancellation technique exclusive to the CTF MEG System. It permits the MEG detectors to be sensitive to the weak signals of the brain, yet impervious to the much stronger sources from the environment. This process, which is carried out in real time, allows the system to be run without the expense of magnetic shielding, or in combination with a standard shielded room for enhanced noise reduction.

In order to calculate the forward solution, the same procedure must be performed on any field data calculated from a simulated dipole. The procedure consists of calculating the field at each coil in the sensor as well as each coil in a set of reference channels. The field values at the reference channels are then multiplied by the appropriate weight and subtracted from the MEG sensor channels.\_

The data set on disk contains in the header the parameters that are used to convert the data between the original (raw) representation and the higher-order gradiometer representation ("balancing"). This conversion can be done in real-time during acquisition, but can also be done (and undone) afterwards using CTF DataEditor, or using **[ft_denoise_synthetic](/reference/ft_denoise_synthetic)**.

To get an intuition about what "balancing" means in terms of computation, let's run the following code. First, download the example CTF data set [Subject01.zip](https://download.fieldtriptoolbox.org/tutorial/Subject01.zip) and use **[ft_read_sens](/reference/fileio/ft_read_sens)** to access the sensor position information of the MEG data, in this case CTF151:

    grad = ft_read_sens('Subject01.ds', 'senstype', 'meg')

The grad structure included in the FieldTrip representation (i.e. hdr.grad or data.grad) should be consistent with the data, hence it contain

    grad.balance

    ans =

         G1BR: [1x1 struct]
         G2BR: [1x1 struct]
         G3BR: [1x1 struct]
      current: 'none'

and potentially other "balancing" schemes. The grad.balance.current describes which balancing was applied to the data and to the specification of the sensor array (grad.tra) for the forward computation. See [How are electrodes, magnetometers or gradiometers described?](/faq/how_are_electrodes_magnetometers_or_gradiometers_described) for more information.

We can explore the different higher order synthetic gradiometer forward solution as follow

    figure;
    subplot(2,2,[1 3]);imagesc(grad.balance.G1BR.tra);
    title('First order gradiometer forward solution');
    xlim([0 175]);colorbar;

    %example forward solution for the second MEG sensor
    colorcode = (grad.balance.G1BR.tra(2,:)~=0)+1;
    subplot(2,2,[2 4]);scatter(1:size(grad.balance.G1BR.tra,2),grad.balance.G1BR.tra(2,:),9,colorcode,'filled');
    title(['First order gradiometer forward solution for sensor ' grad.balance.G1BR.labelnew{2}]);
    xlim([0 175]);ylim([-1.2 1.2]);

{% include image src="/assets/img/faq/ctf_syntheticgradient/g1brv.png" %}

The left part of the figure shows how the first order gradiometer forward solution is computed. The X and the Y axes are the MEG sensors inside grad.balance.G1BR.labelnew and grad.balance.G1BR.labelold. The right plot shows how to compute the first order gradiometer for a specific MEG sensor, in this case sensor MLC12, which is the second sensor of the CTF151 system. You can notice that on the x axes the second sensor, the MLC12 scores one, and the rest of the 150 MEG sensors scored zero (blue dots). This is important because the forward computation of the first order gradient is basically constituted by the field contribution of each MEG sensor. However, colored in red, there are some MEG sensors (the environment sensors) that slightly deviated from zero, which means that they're also contribution to the field of sensor MLC12 but with a negligible degree.

If we explore the second and the third synthetic gradiometers, things become very interesting

    figure;
    subplot(2,2,[1 3]);imagesc(grad.balance.G2BR.tra);
    title('Second order gradiometer forward solution');
    xlim([0 175]);colorbar;

    %example forward solution for the second MEG sensor
    colorcode = (grad.balance.G2BR.tra(2,:)~=0)+1;
    subplot(2,2,[2 4]);scatter(1:size(grad.balance.G2BR.tra,2),grad.balance.G2BR.tra(2,:),9,colorcode,'filled');
    title(['Second order gradiometer forward solution for sensor ' grad.balance.G2BR.labelnew{2}]);
    xlim([0 175]);ylim([-1.2 1.2]);

{% include image src="/assets/img/faq/ctf_syntheticgradient/g2brv.png" %}

    figure;
    subplot(2,2,[1 3]);imagesc(grad.balance.G3BR.tra);
    title('Third order gradiometer forward solution');
    xlim([0 175]);colorbar;

    %example forward solution for the second MEG sensor
    colorcode = (grad.balance.G3BR.tra(2,:)~=0)+1;
    subplot(2,2,[2 4]);scatter(1:size(grad.balance.G3BR.tra,2),grad.balance.G3BR.tra(2,:),9,colorcode,'filled');
    title(['Third order gradiometer forward solution for sensor ' grad.balance.G3BR.labelnew{2}]);
    xlim([0 175]);ylim([-1.2 1.2]);

{% include image src="/assets/img/faq/ctf_syntheticgradient/g3brv.png" %}

Now is more evident that the higher the synthetic gradiometer, the higher the contribution of other MEG sensors to the Nth-order gradiometer forward solution.

In you are interested in an extended explanation regarding MEG signal acquisition and processing in general, not only for CTF systems, please take a look to this reference

Vrba, J., & Robinson, S. E. (2001). Signal Processing in Magnetoencephalography. Methods, 25(2), 249-271. doi: http://dx.doi.org/10.1006/meth.2001.1238
