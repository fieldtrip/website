---
title: Data structures used by FieldTrip
tags: [development]
---

# Data structures used by FieldTrip

High-level FieldTrip functions expect input data as a MATLAB structure in a specific format, and produce output data as a structure in a specific format. These structures are documented in the following functions:

- **[ft_datatype_comp](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_comp.m)**
- **[ft_datatype_dip](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_dip.m)**
- **[ft_datatype_freq](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_freq.m)**
- **[ft_datatype_headmodel](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_headmodel.m)**
- **[ft_datatype_mvar](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_mvar.m)**
- **[ft_datatype_parcellation](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_parcellation.m)**
- **[ft_datatype_raw](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_raw.m)**
- **[ft_datatype_segmentation](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_segmentation.m)**
- **[ft_datatype_sens](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_sens.m)**
- **[ft_datatype_source](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_source.m)**
- **[ft_datatype_spike](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_spike.m)**
- **[ft_datatype_timelock](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_timelock.m)**
- **[ft_datatype_volume](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_volume.m)**

## Checking and converting

Besides documenting the data structures, these ft_datatype_xxx functions also check the internal consistency of the structures and - where needed - update the data structures to the latest standard. This means that if a user loads a data structure from an old .mat file on disk and feeds it into a newer version of a FieldTrip function, the data structure is updated to the expected format prior to the function doing its work. This works by each FieldTrip function calling **[ft_checkdata](https://github.com/fieldtrip/fieldtrip/blob/release/ft_checkdata.m)** at the start of the function, and ft_checkdata calling the corresponding ft_datatype_xxx function.

## Dimord

FieldTrip data structures have "data" fields and "metadata" fields. The metadata fields make the data interpretable.

Some of the data fields are for example:

- avg
- trial
- powspctrm
- cohspctrm
- prob
- stat

Some of the metadata fields that describe the data are:

- label
- labelcmb
- time
- freq
- pos

To document the data fields unambiguously, the data structure can include  a "dimord" field that specifies the order of the dimensions, and that links each of the dimensions to the corresponding metadata field.

1. A data structure can have a single `dimord` field; in that case the dimord refers to the most important data field in the structure.
2. A data structure can have a one or multiple `xxxdimord` fields, where xxx refers to the data parameter. For example `powspctrmdimord` to document `powspctrm`, and `cohspctrmdimord` to document `cohspctrm`.
3. It is also allowed that a data structure does _not_ have an explicit dimord. In that case FieldTrip will - where needed - use heuristics to determine how the data field is to be interpreted.

To determine what the dimensions of a data field represent, FIeldTrip functions use the private **[getdimord](https://github.com/fieldtrip/fieldtrip/blob/master/private/getdimord.m.m)** function. To determine their size, they use the private **[getdimsiz](https://github.com/fieldtrip/fieldtrip/blob/master/private/getdimsiz.m.m)** function. Another private function that plays a role for managing the dimord field is **[fixdimord](https://github.com/fieldtrip/fieldtrip/blob/master/private/fixdimord.m.m)**.

Most of the pieces of the dimord matches a corresponding metadata field.

| element   | field                       |
| --------- | --------------------------- |
| `time`    | `time`                      |
| `freq`    | `freq`                      |
| `chan`    | `label`                     |
| `chancmb` | `labelcmb`                  |
| `refchan` | `label`                     |
| `pos`     | `pos`                       |
| `ori`     | n/a, dipole orientations    |
| `subj`    | n/a, subjects               |
| `rpt`     | n/a, repetitions/trials     |
| `rpttap`  | n/a, repetitions and tapers |
| `comp`    | n/a, components             |

Some pieces of the dimord do not have a corresponding metadata field, such as `rpt` (for repetitions, i.e. trials) or `comp` for components. These dimensions correspond in general to a numbered list from 1 to N.

### Data as a N-dimensional array

Most data fields are represented as a N-dimensional numeric array; the dimord is in that case a simple concatenation of the corresponding strings like `xxx_yyy_zzz`. For example `chan_time` or `rpttap_chan_freq_time`.

### Data as a cell-array

Some data fields are represented as a cell-array. This is sometimes used to represent data elements of different size (e.g., spike timings). This is also used to to represent data that is sparse and partially empty (e.g., leadfields and beamformer filters). For these type of data structures the cell-array is always the outer-most (first) dimension and the corresponding dimension is described as `{xxx}`, i.e. with curly brackets. For a multi-dimensional cell-array this could be `{xxx_yyy_zzz}`.

The subsequent dimensions of the arrays that are contained in each cell are described as before, subsequently the dimord can be for example `{pos}_chan_ori` (for leadfields) or `{pos_pos}_freq` for a source-level connectivity metric that is frequency resolved.
