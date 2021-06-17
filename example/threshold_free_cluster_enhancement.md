---
title: Using threshold-free cluster enhancement for cluster statistics
tags: [example, statistics]
---

# Using threshold-free cluster enhancement for cluster statistics

This example explains how the threshold-free cluster enhancement method works for cluster statistics.

## Why is it useful?
While running cluster-statistics, we need to define the threshold for clustering (recall the `cfg.clusteralpha` option for cluster-based permutation test). Different clusteralpha values lead to clusters of very different extends, and potentially different results in the subsequent permutation test. The threshold-free cluster enhancement method is introduced to overcome this arbitrary clusteralpha.

## How does it work?
Each voxel’s TFCE score is given by the sum of the scores of all “supporting sections” underneath it; as the height h is incrementally raised from zero up to the height (signal intensity) _𝒉<sub>p</sub>_ of a given point 𝒑, the image is thresholded at 𝒉, and the single contiguous cluster containing p is used to define the score for that height 𝒉. This score is simply the height 𝒉 (raised to some power 𝑯, which is by default set to 2 in fieldtrip and can be adjusted via `cfg.tfce_H`) multiplied by the cluster extent 𝒆 (raised to some power 𝑬, which is by default set to 0.5 in fieldtrip and can be adjusted via `cfg.tfce_E`). For detailed information, see Smith & Nichols, 2009.

{% include image src="/assets/img/example/threshold_free_cluster_enhancement/schematic.png" width="300" %}




## Example code
The following matlab code gives an example of using the method. Moreover, we will compare the statistical output of the TFCE method with the conventional "clusteralpha-dependent" method.

```
load ERF_orig;


Nsubj       = 10;
design      = zeros(2, Nsubj*2);
design(1,:) = [1:Nsubj 1:Nsubj];
design(2,:) = [ones(1,Nsubj) ones(1,Nsubj)*2];


cfg          = [];
cfg.method   = 'template';
cfg.template = 'CTF151_neighb.mat';
nb           = ft_prepare_neighbours( cfg, allsubjFIC{1} );

%% Conventional cluster-based permutation test
cfg                  = [];
cfg.design           = design;
cfg.uvar             = 1;
cfg.ivar             = 2;
cfg.channel          = {'MLT12'};
cfg.neighbours       = nb;
cfg.latency          = [0 1];
cfg.method           = 'montecarlo';
cfg.numrandomization = 500;
cfg.statistic        = 'depsamplesT';
cfg.correctm         = 'cluster';
cfg.clusterthreshold = 'nonparametric_individual';
cfg.clusteralpha     = 0.01;
cfg.clusterstatistic = 'maxsum';
cfg.clustertail      = 0;
cfg.tail             = 0;
cfg.alpha            = 0.025;
stat01 = ft_timelockstatistics(cfg, allsubjFIC{:}, allsubjFC{:});


cfg.clusteralpha     = 0.05;
cfg.clusterstatistic = 'maxsum';
cfg.clustertail      = 0;
cfg.tail             = 0;
cfg.alpha            = 0.025;
stat05 = ft_timelockstatistics(cfg, allsubjFIC{:}, allsubjFC{:});



%% Cluster-based permutation test with TFCE method
cfg                  = [];
cfg.design           = design;
cfg.uvar             = 1;
cfg.ivar             = 2;
cfg.channel          = {'MLT12'};
cfg.latency          = [0 1];
cfg.method           = 'montecarlo';
cfg.statistic        = 'depsamplesT';
cfg.correctm         = 'tfce';
cfg.tfce_H           = 2; %default setting
cfg.tfce_E           = 0.5; %default setting
cfg.tail             = 0;
cfg.alpha            = 0.025;
cfg.numrandomization = 500;
statA = ft_timelockstatistics(cfg, allsubjFIC{:}, allsubjFC{:});

cfg.correctm         = 'tfce';
cfg.tfce_H           = 2;
cfg.tfce_E           = 0.25;
statB = ft_timelockstatistics(cfg, allsubjFIC{:}, allsubjFC{:});
```

Note the TFCE method may take slightly longer than the conventional method. We can visualize and compare the slightly different statistical outputs given by these methods.

```
%% Visualize the results
figure(1), clf, hold on,
set(gcf, 'units','centimeters','position',[0 0 18 10] );
subplot(2,2,1), hold on, grid on,
title( 'TFCE: H=2, E=0.5' );
plot( statA.time, stat.stat_tfce, 'r');
plot( statA.time(statA.mask), 400*ones(sum(statA.mask),1), 'r', 'linewidth',2 );
ylabel( 'TFCE' );
ylim( [-20, 420] );
xticks( 0:0.2:1 );
set(gca, 'TickDir','out' );

subplot(2,2,3), hold on, grid on,
title( 'TFCE: H=2, E=0.25' );
plot( statB.time, statB.stat_tfce, 'r');
plot( statB.time(statB.mask), 400*ones(sum(statB.mask),1), 'r', 'linewidth',2 );
ylabel( 'TFCE' );
ylim( [-20, 420] );
xticks( 0:0.2:1 );
set(gca, 'TickDir','out' );

subplot(2,2,2), hold on, grid on,
title( 'clusteralpha = .01' );
plot( stat01.time, stat01.stat, 'k');
plot( stat01.time(stat01.mask), 7.5*ones(sum(stat01.mask),1), 'k', 'linewidth',2 );
ylabel( 't-value' );
ylim( [-3, 8] );
xticks( 0:0.2:1 );
set(gca, 'TickDir','out' );

subplot(2,2,4), hold on, grid on,
title( 'clusteralpha = .05' );
plot( stat05.time, stat05.stat, 'k');
plot( stat05.time(stat05.mask), 7.5*ones(sum(stat05.mask),1), 'k', 'linewidth',2 );
ylabel( 't-value' );
ylim( [-3, 8] );
xticks( 0:0.2:1 );
set(gca, 'TickDir','out' );
```

## Output of the example code
Here is the expected output of the example code.
{% include image src="/assets/img/example/threshold_free_cluster_enhancement/matlab_output_figure.png" width="300" %}
