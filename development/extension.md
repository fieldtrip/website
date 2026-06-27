---
title: Preparing a FieldTrip extension
tags: [development]
---

FieldTrip extensions are externally maintained projects that build on, wrap, or
interact with FieldTrip without necessarily becoming part of the main FieldTrip
code repository. They can be useful for complete analysis methods, graphical
interfaces, research group workflows, or toolboxes with their own release cycle.

This page gives extension authors a practical checklist before asking for a
listing on the [extensions page](/extensions).

## Decide whether it should be an extension

An external extension can be a good fit when:

- the code has a clear purpose and user group, but is too specialized for the
  FieldTrip core;
- the original authors can maintain the code, answer questions, and make
  releases independently;
- the project has dependencies, data, examples, or licensing details that are
  easier to manage outside the FieldTrip release;
- users can install or download it without changing the main FieldTrip code
  base;
- the extension can still be discovered from the FieldTrip website.

A direct contribution to FieldTrip may be a better fit when the functionality
is broadly useful, follows the existing FieldTrip data structures, can be tested
with the FieldTrip test infrastructure, and can be maintained by the FieldTrip
team after it is merged.

## Prepare the extension repository

Before requesting a listing, please try to make the extension repository useful
for a new user who finds it through the FieldTrip website. A minimal repository
usually benefits from:

- a README that explains the analysis problem, installation, and first example;
- a short statement that the project is maintained outside FieldTrip;
- a license file, or a clear explanation of the terms under which the code can
  be used;
- a small example script or tutorial that starts from a FieldTrip data
  structure, when that is possible;
- enough version or release information for users to cite or reproduce the
  workflow;
- a contact route for bug reports and questions;
- notes about any required toolboxes, compiled code, large data files, or
  external programs.

If the extension includes MATLAB functions that accept or return FieldTrip data,
it helps to name the expected data type in the README, for example raw,
timelock, freq, comp, source, or volume data. Please also mention whether the
extension modifies FieldTrip data structures or only reads them.

## Request a listing on the website

Extension listings live in the website repository under `_data/extensions`.
Each listing is a small `.yml` file with fields such as:

```yaml
name: Example extension
authors: First Author and Second Author
description: A short description of what the extension does and who it is for.
url: https://github.com/example/example-extension
doi: 10.xxxx/example
pmid: 12345678
pmcid: PMC1234567
```

Only `name`, `authors`, `description`, and `url` are essential. Citation fields
such as `doi`, `pmid`, and `pmcid` can be added when they are available.

You can request a listing by opening a pull request against the
[FieldTrip website repository](https://github.com/fieldtrip/website). In the
pull request description, please include:

- a link to the extension repository;
- the main FieldTrip function or data structure that the extension interacts
  with, if there is one;
- who maintains the extension;
- whether the extension has a paper, preprint, tutorial, or example;
- any known limitations that FieldTrip users should understand before using it.

The FieldTrip maintainers may edit the wording, ask for a shorter description,
or decide that a listing is not appropriate yet. The goal is to help users find
relevant community work while keeping responsibility for the extension clear.

## See also

- [Extensions](/extensions)
- [Contribute](/development/contribute)
- [Git and GitHub tutorial](/development/git)
- [Code guidelines](/development/guideline/code)
- [Documentation guidelines](/development/guideline/documentation)
