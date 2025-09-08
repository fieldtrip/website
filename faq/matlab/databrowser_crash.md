---
title: The databrowser crashes and destroys the whole MATLAB session, how can I resolve this?
tags: [ica, data, crash, databrowser, surf, topoplot, topo]
category: faq
redirect_from:
    - /faq/the_databrowser_crashes_and_destroys_the_whole_matlab_session_how_can_i_resolve_this/
    - /faq/databrowser_crash/
---

FieldTrip relies on MATLABs plotting routines, which uses specific renderers. Unfortunately, specific combinations of graphics card, operating system and MATLAB version can cause MATLAB to crash using specific renderer. This can happen when using the databrowser, and if this happens for you, it will always happen unless you change something. The easiest change can be made to the renderer, as it entails only a simple MATLAB command. In most FieldTrip functions, you can set the renderer via the cfg. As such, for the databrowser you can simply add

    cfg.renderer = 'painters'

prior to the call to ft_databrowser.

{% include markup/skyblue %}
This error and solution has been confirmed by the MathWorks. Thanks to Martine van Schouwenburg for contacting MathWorks and forwarding their response.
{% include markup/end %}

EMAIL SUPPORT TEAM MATHWORKS

"I have a feeling that the crash might be because of the renderer being
chosen by MATLAB to plot the surface plot.

MATLAB has three renderers- OpenGL, Painters and Z-Buffer. Each of these
renderers has its own merits and limitations. MATLAB chooses the correct
renderer based on the type of figure that you are plotting.

Here is a documentation page that talks more about the three renderers in MATLAB:
<http://www.mathworks.com/help/matlab/creating_plots/changing-a-figures-settings.html#f3-102410>

Of the three renderers OpenGL has the ability to use the graphics hardware
on your system to help render the graphics. This can occasionally cause
incompatibilities due to the many different graphics cards out there and
also the many different driver versions that exist for each of these cards.

So, you can try and switch to the software implementation of OpenGL by
executing the following command in the command window:

    >> opengl software

This setting is retained for the current session of MATLAB. If you want
MATLAB to remember this setting across settings, then I would suggest that
you add this command to your "startup.m".

Please use the above command and then run your code to see if the crash
still occurs.

IF THE ABOVE PROCEDURE DOES NOT WOR
We can try and change the renderer to one of the other two and see if this
helps. You can change the renderer by using the "set" command:

    >> set(gcf,'renderer','painters');
    >> OR
    >> set(gcf,'renderer','zbuffer');
    >> OR
    >> set(gcf,'renderer','opengl');

Here "gcf" refers to the currently active figure window.

I would suggest that you try changing the renderer just before the "surf"
command is executed and see if the crash stops happening when using a
particular renderer."
{# FIXME the following might be displayed incorrectly #}
