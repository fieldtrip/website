---
title: Plotting of channel-level, source-level and other geometrical data related to EEG/MEG
tags: [development, plotting]
redirect_from:
  - /development/plotting/
---

# Plotting of channel-level, source-level and other geometrical data related to EEG/MEG

FieldTrip supports plotting of channel-level and source-level data using functions that are described in the [plotting tutorial](/tutorial/plotting). These functions allow the user to specify a configuration and to work with all standard [data structures](/faq/development/datatype). Under the hood, these functions make use of a collection of shared lower-level functions which are still at a higher level than the standard MATLAB plotting tools.

The goal of the shared plotting functions (compared to MATLAB) is to reuse the same functionality in different functions and be able to improve the functionality everywhere.

Furthermore, the shared plotting functions allow a power-user to construct more detailed data visualizations.

## Module layout

The plotting module contains functions that are publicly available for the end-user. The functionality of the functions within this module depends on low-level functions that for example handle triangulated surfaces, etc. These low-level functions are not available to the end-user and combined in a private directory.

The remainder of this page mainly describes the core features for plotting channel- and source-level EEG and MEG data and all related geometrical information.

## Definition of the function-calls (API)

These are the low-level functions that are be called by the higher-level FieldTrip functions. These functions usually take matrices or vectors as input, as opposed to FieldTrip data structures.

For data objects with a 2D representation, i.e. for a flat screen or paper:

- ft_plot_vector - visualizes a vector as a line, similar to PLOT
- ft_plot_matrix - visualizes a matrix as an image, similar to IMAGESC
- ft_plot_line - helper function for plotting a line, which can also be used in
- ft_plot_text - helper function for plotting text, which can also be used in
- ft_plot_topo - interpolates and plots the 2-D spatial topography of the
- ft_plot_layout - plots a two-dimensional layout
- ft_plot_box - plots the outline of a box that is specified by its lower

For data objects with a 3D geometrical representation:

- ft_plot_cloud - visualizes 3-D data as spherical clouds of points
- ft_plot_crosshair - plots a crosshair in two or three dimensions
- ft_plot_dipole - makes a 3-D representation of a dipole using a sphere and a stick
- ft_plot_headshape - visualizes the shape of a head from a variety of
- ft_plot_mesh - visualizes the information of a mesh contained in the first
- ft_plot_montage - makes a montage of a 3-D array by selecting slices at
- ft_plot_ortho - plots a 3 orthographic cuts through a 3-D volume
- ft_plot_sens - plots the position of the channels in the EEG or MEG sensor array
- ft_plot_slice - cuts a 2-D slice from a 3-D volume and interpolates if needed
- ft_plot_topo3d - makes a 3-D topographic representation of the electric
- ft_plot_headmodel - visualizes the boundaries in the volume conduction model of the head as

A number of functions serves to construct interactive graphical user interfaces:

- ft_select_box - helper function for selecting a rectangular region
- ft_select_channel - is a helper function that can be used as callback function
- ft_select_point - helper function for selecting a one or multiple points in the
- ft_select_point3d - helper function for selecting one or multiple points on a 3D mesh
- ft_select_range - is a helper function that can be used as callback function
- ft_select_voxel - is a helper function that can be used as callback function
- ft_uilayout - is a helper function to facilitate the layout of multiple

All functions take some required fixed input arguments, followed by a variable number of key-value pairs.
