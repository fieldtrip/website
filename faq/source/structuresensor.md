---
title: Should I use a Polhemus or a Structure Sensor to record electrode positions?
category: faq
tags: [electrode, polhemus, structure-sensor]
redirect_from:
    - /faq/structuresensor/
---

# Should I use a Polhemus or a Structure Sensor to record electrode positions?

This is a quick note with opinions regarding the [Structure Sensor](http://structure.io/) to record the head shape and/or electrode locations, as described in detail in [this tutorial](/tutorial/electrode).

- The Polhemus Fastrack is more accurate, but also more time-consuming.
- The Polhemus Fastrack is more expensive.
- The Structure sensor has problems if wires are sticking out of the cap -> this is IMPORTANT as it depends on your cap design.
- The Structure sensor has problems if the subject moves his head during the (approximate 2-minute) scan.
- A quick quality check of the results is easier with the Structure sensor, which means that it is easier to detect and repeat a poor scan.
- Errors in the order of electrode scanned with the Fastrack that are not detected at time of scanning are more difficult to fix afterward.
- The Structure sensor cannot be used to scan the head (scalp) surface without the subject wearing a cap to press the hair down.
- The Structure sensor (with ipad) is so cheap that buying it and subsequently not using it so often is not too much of a loss. This is different for the Polhemus.
- With the Polhemus it is possible to scan a subset of electrodes (which is faster than the whole set) and use those to warp a template of the complete electrode set to the measured subset. But you should not make errors in scanning the subset. And it requires a good template and some software steps afterward (FieldTrip can do it).

The overall experience in our EEG lab (with many researchers and studies) is that the researchers consider the Polhemus too time consuming and therefore skip the recording of the electrode positions. Our hope is that the Structure sensor is sufficiently fast and easy to use to have electrode (and scalp) recordings of more of the EEG subjects.
