---
layout: default
---

`<note warning>`
The purpose of this page is just to serve as todo or scratch pad for the development project and to list and share some ideas. 

After making changes to the code and/or documentation, this page should remain on the wiki as a reminder of what was done and how it was done. However, there is no guarantee that this page is updated in the end to reflect the final state of the project

So chances are that this page is considerably outdated and irrelevant. The notes here might not reflect the current state of the code, and you should **not use this as serious documentation**.
`</note>`

Goal: to consistently deal with spatial units.
 
Plan: investigate at which locations knowledge about the units is assumed/needed/appended to the data. at some places there could be even hard coded conversions. Build in explicit check-and-error, or correction when two objects are combined with different units.

 1. gradiometer/sensor definition
 2. volume-conductor specification  
 3. grid computation
 4. gradiometer/sensor definition
 5. volume-conductor specification
 6. grid computation
 7. leadfield computation e.g. meg_ini
 8. mri related functions: transformation matrix!
 9. sourceinterpolate

This project has been taken up in 

*  http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=953

*  http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=963

*  http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=686
and work is underway.

