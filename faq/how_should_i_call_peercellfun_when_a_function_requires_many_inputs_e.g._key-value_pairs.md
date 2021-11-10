---
title: How should I call peercellfun when a function requires many inputs (e.g., key-value pairs)?
tags: [faq, peer]
---

# How should I call peercellfun when a function requires many inputs (e.g., key-value pairs)?

If you want to call a function n times, there should a cell-array of size(n,1) for each input argument you want to give. Peercellfun will then call the function n times (distributed over peers) with all input arguments sitting in the n-th position of each input cell-array.

Example for n = 4:

    % normal function cal
    [output1 output2] = functionname(matrix,number,key1,val1,key2,val2)

    in-matrix  = repmat({matrix}, [4 1]); % 4x1 cell-array with a matrix in each cell
    in-number  = repmat({number}, [4 1]); % 4x1 cell-array with a number in each cell
    in-key1    = repmat({key1}  , [4 1]); % 4x1 cell-array with a string in each cell
    in-val1    = repmat({val1}  , [4 1]); % 4x1 cell-array with a string in each cell
    in-key2    = repmat({key2}  , [4 1]); % 4x1 cell-array with a string in each cell
    in-val2    = repmat({val2}  , [4 1]); % 4x1 cell-array with a string in each cell

    % peercellfun cal
    [output1 output2] = peercellfun('functionname',in-matrix,in-number,in-key1,in-val1,in-key2,in-val2);
    % output1 = 4x1 cell-array with output 1 in each cell
    % output2 = 4x1 cell-array with output 2 in each cell
