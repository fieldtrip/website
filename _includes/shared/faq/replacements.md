To avoid unnecessary dependencies on functions from non-standard MathWorks toolboxes, FieldTrip includes a number of drop-in replacement functions that have the same functionality as their MATLAB counterparts. Have a look at [this FAQ](/faq/can_i_prevent_external_toolboxes_from_being_added_to_my_matlab_path) how you can control whether these are added to your path.

Alternatives are provided for the following functions from the MathWorks [Statistics Toolbox](https://www.mathworks.com/products/statistics.html) (stats)

- nansum, nanstd, etc.
- betacdf
- betainv
- betapdf
- binocdf
- binopdf
- mvnrnd
- tcdf
- tinv
- range

Alternatives are provided for the following functions from the MathWorks [Signal Processing Toolbox](https://www.mathworks.com/products/signal.html) (signal)

- barthannwin
- bilinear
- blackmanharris
- bohmanwin
- boxcar
- butter
- downsample
- filtfilt
- fir1
- fir2
- firls
- flattopwin
- gausswin
- hann
- hanning
- hilbert
- kaiser
- nuttallwin
- parzenwin
- rectwin
- resample
- triang
- tukeywin
- upfirdn
- upsample
- window

Alternatives are provided for the following functions from the MathWorks [Image Processing Toolbox](https://www.mathworks.com/products/image.html) (images)

- rgb2hsv
