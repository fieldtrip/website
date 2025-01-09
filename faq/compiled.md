---
title: Can I use FieldTrip without MATLAB license?
parent: MATLAB questions
category: faq
tags: [matlab, mex, compile]
---

# Can I use FieldTrip without MATLAB license?

Yes, if you have the MATLAB [compiler toolbox](https://www.mathworks.com/products/compiler.html) you can make a compiled version and use that to run your analysis pipelines. You compile FieldTrip with all its dependencies like this

    ft_compile_standalone

Subsequently you can run your analysis pipelines by providing them as script (not as a function) using the `fieldtrip.sh` Bash wrapper script (only provided for Linux and macOS). The compiled application and startup script can be found in the `fieldtrip/bin` directory

If you make a script like the following

    cfg = [];
    cfg.numtrl = 10;
    data = ft_freqsimulation(cfg);

    cfg = [];
    ft_databrowser(cfg, data);

    input('press a buton to exit');

you would execute

    fieldtrip.sh `<MATLABROOT>` yourscript.m

where MATLABROOT points to either your local MATLAB installation, or to the location of the redistributable [MATLAB Compiler Runtime](https://se.mathworks.com/products/compiler/matlab-runtime.html) environment (MCR).

Note that the "press a button to exit" statement is used to prevent the compiled application from closing as soon as the data browser appears, since that would also close the figure again. Most pipelines will not need this.

{% include markup/skyblue %}
This is the strategy we also used for running the Human Connectome Project [megconnectome](https://github.com/Washington-University/megconnectome) analysis pipelines on the WashU compute cluster.
{% include markup/end %}
