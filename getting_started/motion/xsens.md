---
title: Getting started with XSens motion capture data
parent: Motion capture
grand_parent: Getting started
category: getting_started
tags: [dataformat, xsens, motion]
redirect_from:
    - /getting_started/xsens/
---

# Getting started with XSens motion tracking data

[XSens](http://www.xsens.com) is a company that makes IMU-based motion capture systems that are used in the animation industry and in research. Their MVN Analyze system comprises full-body sensor systems and acquisition and analysis software. By default the software stores the data in the proprietary MVN file format, but it allows the data to be exported to open formats that are supported by FieldTrip

## C3D

The [C3D](https://www.c3d.org) format can be read in FieldTrip using the low-level [reading functions](/development/module/fileio) and using the high-level **[ft_preprpcessing](/reference/ft_preprocessing)** function.

    cfg = [];
    cfg.dataset = 'sub-03_rec-01_take-02_motion.c3d'
    data = ft_preprocessing(cfg)

This returns a data structure like this:

    data =
      struct with fields:

               hdr: [1x1 struct]
             label: {192x1 cell}
              time: {[1x26229 double]}
             trial: {[192x26229 double]}
           fsample: 60
        sampleinfo: [1 26229]
               cfg: [1x1 struct]

where the channels correspond to the time-varying positions of of the reconstructed stick-figure reference points. There are 64 reference points, represented as (x, y, z) in 192 channels:

    >> data.label
    ans =
      192x1 cell array
        {'pHipOrigin_x'             }
        {'pHipOrigin_y'             }
        {'pHipOrigin_z'             }
        ...
        {'pSacrum_x'                }
        {'pSacrum_y'                }
        {'pSacrum_z'                }
        ...
        {'pTopOfHead_x'             }
        {'pTopOfHead_y'             }
        {'pTopOfHead_z'             }
        ...
        {'pRightBallHand_x'         }
        {'pRightBallHand_y'         }
        {'pRightBallHand_z'         }
        ...
        {'pLeftToe_x'               }
        {'pLeftToe_y'               }
        {'pLeftToe_z'               }
        ...


## MVNX

The MVNX file format is an open XML file format that contains more information than the C3D files, including all of the segment information as well as joint angle data, center of mass and factory calibrated sensor data. It can be read using either the low-level [reading functions](/development/module/fileio) and using the high-level **[ft_preprpcessing](/reference/ft_preprocessing)** function.

Reading the MVNX file requires that you have the `load_mvnx.m` function on your MATLAB path. This function can be found within the MVN Studio Developer Toolkit or [here](https://github.com/Roger-Dai/motion-capture). We recommend that you put the file in `fieldtrip/external/xsens`, in which case that directory will automatically be added to the path when needed.


## Plotting stick figures

Using the following code you can plot a walking stick figure as a movie:

    xpoint = find(endsWith(data.label, '_x'));
    ypoint = find(endsWith(data.label, '_y'));
    zpoint = find(endsWith(data.label, '_z'));

    figure
    axis vis3d
    axis on
    grid on
    hold on
    view(40,20)

    clear M

    for i=1:numel(data.time{1})
      cla

      fprintf('%.1f seconds\n', data.time{1}(i))

      x = data.trial{1}(xpoint, i);
      y = data.trial{1}(ypoint, i);
      z = data.trial{1}(zpoint, i);

      plot3(x, y, z, '.');
      title(sprintf('%.1f seconds', data.time{1}(i)));

      drawnow % this forces a refresh at each frame, disable it to speed up the movie construction

      M(i) = getframe;
    end

    movie(M, 1, data.fsample)
