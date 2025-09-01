---
title: Data structures
tags: [development]
---

High-level FieldTrip functions expect input data as a MATLAB structure, and produce output data as a MATLAB structure. The input and output data structures are documented in the following helper functions:

- **[ft_datatype_comp](/reference/utilities/ft_datatype_comp)**
- **[ft_datatype_dip](/reference/utilities/ft_datatype_dip)**
- **[ft_datatype_freq](/reference/utilities/ft_datatype_freq)**
- **[ft_datatype_headmodel](/reference/utilities/ft_datatype_headmodel)**
- **[ft_datatype_mvar](/reference/utilities/ft_datatype_mvar)**
- **[ft_datatype_parcellation](/reference/utilities/ft_datatype_parcellation)**
- **[ft_datatype_raw](/reference/utilities/ft_datatype_raw)**
- **[ft_datatype_segmentation](/reference/utilities/ft_datatype_segmentation)**
- **[ft_datatype_sens](/reference/utilities/ft_datatype_sens)**
- **[ft_datatype_source](/reference/utilities/ft_datatype_source)**
- **[ft_datatype_spike](/reference/utilities/ft_datatype_spike)**
- **[ft_datatype_timelock](/reference/utilities/ft_datatype_timelock)**
- **[ft_datatype_volume](/reference/utilities/ft_datatype_volume)**

## Checking and converting

Besides documenting the data structures, these `ft_datatype_xxx` functions also check the internal consistency of the structures and - where needed - update the data structures to the latest standard. So if a user loads a data structure from an old `.mat` file on disk and feeds it into a newer version of a FieldTrip function, the structure is updated to the expected format prior to the function starting to work on it. This works by each FieldTrip function calling **[ft_checkdata](/reference/utilities/ft_checkdata)** at the start of the function, and `ft_checkdata` calling the corresponding `ft_datatype_xxx` function.

## Dimord

FieldTrip data structures have "data" fields and "metadata" fields. The metadata fields make the data interpretable.

Some of the "data" fields are for example:

- avg
- trial
- powspctrm
- cohspctrm
- prob
- stat

Some of the "metadata" fields that describe the data are:

- label
- labelcmb
- time
- freq
- pos

To document the data fields unambiguously, the structure can include a `dimord` field that specifies the order of the dimensions, and that links each of the dimensions to the corresponding metadata field.

1. A data structure can have a single `dimord` field; in that case the dimord refers to the most important data field in the structure.
2. A data structure can have a one or multiple `xxxdimord` fields, where xxx refers to the data parameter. For example `powspctrmdimord` to document `powspctrm`, and `cohspctrmdimord` to document `cohspctrm`.
3. It is also allowed that a data structure does _not_ have an explicit dimord. In that case FieldTrip will - where needed - use heuristics to determine how the data field is to be interpreted.

To determine what the dimensions of a data field represent, FieldTrip functions use the private **[getdimord](/reference/private/getdimord)** function. To determine their size, they use the private **[getdimsiz](/reference/private/getdimsiz)** function. Another private function that plays a role for managing the dimord field is **[fixdimord](/reference/private/fixdimord)**.

Most of the elements of the dimord match a corresponding metadata field.

| dimord element | corresponding metadata field |
| -------------- | ----------------------------- |
| `time`         | `time`                        |
| `freq`         | `freq`                        |
| `chan`         | `label`                       |
| `chancmb`      | `labelcmb`                    |
| `refchan`      | `label`                       |
| `pos`          | `pos`                         |
| `ori`          | n/a, dipole orientations      |
| `subj`         | n/a, subjects                 |
| `rpt`          | n/a, repetitions/trials       |
| `rpttap`       | n/a, repetitions and tapers   |
| `comp`         | n/a, components               |

Some elements of the dimord do not have a corresponding metadata field, such as `rpt` (for repetitions, i.e. trials) or `comp` for components. These dimensions in general correspond to a numbered list from 1 to N.

### Data as a N-dimensional array

Most data fields are represented as a N-dimensional numeric array; the dimord is in that case a simple concatenation of the corresponding strings like `xxx_yyy_zzz`. For example `chan_time` or `rpttap_chan_freq_time`.

### Data as a cell-array

Some data fields are represented as a cell-array to represent matrices of different size (e.g., trials prior to averaging, or spike timings). Cell-arrays are also used when the data is sparse and partially empty (e.g., leadfields and beamformer filters). For these type of data structures the cell-array is always the outer-most (first) dimension and the corresponding dimension is described as `{xxx}`, i.e. with curly brackets. For a multi-dimensional cell-array this could be `{xxx_yyy_zzz}`.

The subsequent dimensions of the arrays that are contained in each cell are described as before, subsequently the dimord can be for example `{pos}_chan_ori` (for leadfields) or `{pos_pos}_freq` for a frequency-resolved source-level connectivity metric.
