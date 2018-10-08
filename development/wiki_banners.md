---
layout: default
---

# How to make Wiki banners

As you will have noticed, there is a nice photo rotator at the top of the Fieldtrip website. This page explains how to create them using Adobe Photoshop, and how to add them to the wiki.

## Making the file

 1.  Open the photo in Photoshop.
 2.  Go to Image -> Adjustments -> Black & White, to convert into black & white.
 3.  Apply some toning to make it look good: Image -> Adjustments -> Brightness/Contrast, or -> Curves, or just Image -> Auto Tone, -> Auto Contrast; whichever is your favourite.
 4.  Select the crop tool, constrain to 980x250 px.
 5.  Select the area of the photo you want to use as the banner and press Enter. You now have the correct dimensions.
 6.  Add some grain for that 'vintage' look: Filter -> Noise -> Add Noise; use 2%, Gaussian, Monochromatic, and press OK.
 7.  Copy the FieldTrip logo to the new image by opening the PSD file contained in {{:development:fieldtrip-wiki-banner.zip|this ZIP file}} (select 'No' when Photoshop asks you if you want to update text layers) and dragging the logo layer to the new file.
 8.  Save the photo: File -> Save for Web & Devices; save as JPEG with a decent quality (>~85; or anything that yields ~150kB file size)

## Adding to the website

 1.  Copy the file you just generated to `<dokuwiki root>`/lib/tpl/FieldtripV2/images/ and rename it "header-photo-N.jpg", where N should be replaced by an integer number, following the maximum M of the "header-photo-M.jpg" files already present in that folder.
 2.  Edit `<dokuwiki root>`/lib/tpl/FieldtripV2/main.php, replace the Q in "; i < Q;" below the line that says "add slideshow slides" (currently this code is at lines 61-62) with one higher than the total number of slides.
 3.  Done!

