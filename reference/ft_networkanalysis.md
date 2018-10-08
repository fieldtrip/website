---
layout: default
---

##  FT_NETWORKANALYSIS

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_networkanalysis".

`<html>``<pre>`
    `<a href=/reference/ft_networkanalysis>``<font color=green>`FT_NETWORKANALYSIS`</font>``</a>` computes various network graph measures from
    between-channel or between source-level EEG/MEG signals. This function
    acts as a wrapper aroun the network metrics implemented in the brain
    connectivity toolbox developed by Olaf Sporns and colleagues.
 
    Use as
    stat = ft_networkanalysis(cfg, data)
 
    where the first input argument is a configuration structure (see below)
    and the second argument is the output of `<a href=/reference/ft_connectivityanalysis>``<font color=green>`FT_CONNECTIVITYANALYSIS`</font>``</a>`.
 
    At present the input data should be channel-level data with dimord
    'chan_chan(_freq)(_time)' or source data with dimord
    'pos_pos(_freq)(_time)'.
 
    The configuration structure has to contain
    cfg.method    = string, specifying the graph measure that will be
                    computed. See below for the list of supported measures.
    cfg.parameter = string specifying the bivariate parameter in the data
                    for which the graph measure will be computed.
 
    Supported methods are
    assortativity
    betweenness,      betweenness centrality (nodes)
    charpath,         characteristic path length, needs distance matrix as
                      input
    clustering_coef,  clustering coefficient
    degrees
    density
    distance
    edge_betweenness, betweenness centrality (edges)
    transitivity
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    	cfg.outputfile  =  ...
    If you specify one of these (or both) the input data will be read from a

* .mat file on disk and/or the output data will be written to a *.mat
    file. These mat files should contain only a single variable,
    corresponding with the input/output structure.
 
    See also `<a href=/reference/ft_connectivityanalysis>``<font color=green>`FT_CONNECTIVITYANALYSIS`</font>``</a>`, `<a href=/reference/ft_connectivityplot>``<font color=green>`FT_CONNECTIVITYPLOT`</font>``</a>`
`</pre>``</html>`

