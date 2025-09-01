---
title: Improve integration with other toolboxes
---

{% include /shared/development/warning.md %}


FieldTrip uses and is used by other toolboxes, like EEGLAB, LIMO, and SPM. Sometimes this happens "under the hood", but at other times the researcher explicitly wants to mix and match tools. To support that better, the conversion of data representations needs to be improved and better documented.

There is now some documentation on the [getting started](/getting_started/#getting-started-with-data-from-other-software) page, but that is not complete, nor consistent between the different toolboxes. Each of the pages should describe "how to get from X to FieldTrip" and "how to get from FieldTrip to X".

## MATLAB for Neurosciece summer projects

Improving the integration and documentation is part of the MATLAB for Neurosciece summer projects [#1](https://github.com/fieldtrip/fieldtrip/issues?q=is%3Aissue+project%3Afieldtrip/fieldtrip/3) and [#2](https://github.com/fieldtrip/fieldtrip/issues?q=is%3Aissue+project%3Afieldtrip/fieldtrip/4).
