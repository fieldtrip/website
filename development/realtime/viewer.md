---
title: Realtime visualization of data from the FieldTrip buffer
---

We provide a C++ GUI application (based on the [FLTK](http://www.fltk.org) library, that can be used to visualize any kind of signals online from the FieldTrip buffer. The source code and pre-compiled binaries (for Windows, Linux & macOS) can be found in the `realtime/utilities/viewer` directory. After starting up the application, you need to type in the address of the FieldTrip buffer server and press the "Connect" button (which on success will toggle to "Disconnect"). You have the option of applying a fixed highpass filter (2nd order Butterworth, 5Hz cutoff) to remove DC bias and slow drifts.
The display is fixed to show 4 seconds of data, independently of the sampling frequency, and will wrap around.

{% include image src="/assets/img/development/realtime/viewer/bufferviewer.png" %}

The two sliders and scrollbars can be used to browse through the various channels, as well as to change the distance between successive channels ("space") and the magnification of the signals ("scale"). The number that is displayed between the two sliders prints corresponds to the distance between two zero lines: For the example screenshot below, this means that the magnitude of the HLC0017 signal (red) is a bit less than 2.1e+2 (that is, about 200). You can select which channels to view, and their color, by selecting the names in the panel to the right, and pressing any of the following key

- <space> to clear the selection
- 'n' (no) or 'h' (hide) to hide the selected channels
- 'r' to display the selected channels in red
- 'g' to display the selected channels in green
- 'b' ... blue
- 'k' ... black
- 'y' ... yellow
- 'l' ... lime
- 'p' ... purple
- 'a' ... gray
- 'o' ... orange
- 'c' ... cyan
- 'm' ... magenta
- 't' ... turquoise

## Compilation

We provide a simple "Makefile" for the MinGW compiler on Windows or GCC on other platforms. Please go to the `realtime/src/utilities/viewer` directory and type `make` or `mingw32-make`. You will need to have the [FLTK](http://www.fltk.org) library installed for your platform. Note that you also might need to compile the buffer library first.
