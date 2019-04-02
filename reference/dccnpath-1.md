---
title: dccnpath
---
```
 DCCNPATH updates the path in the filename of a test file located on DCCN central
 storage. It helps to read test file from Linux, Windows or macOS computers in the
 DCCN.

 Use as
  filename = dccnpath(filename)

 The function assumes that on a Windows machine the DCCN home network drive is
 mapped to the H: drive on Windows, or that it is mounted on /Volume/home for macOS.

 Similar functionality as this function could be realized with an anonymous function
 like this:

 if ispc
   dccnpath = @(filename) strrep(strrep(filename,'/home','H:'),'/','\');
 else
   dccnpath = @(filename) strrep(strrep(filename,'H:','/home'),'\','/');
 end
```
