function download_data()

% DOWNLOAD_DATA downloads a version of fieldtrip and the data required to 
% run the tutorials for a toolkit. This function is for the 2026 edition
% of the MEG-OPM toolkit, which intends to run the following tutorials:
%
% test_tutorial_eventrelatedaveraging
% test_tutorial_clusterpermutationtimelock
% test_tutorial_beamformer
% test_tutorial_denoising_opm
% test_tutorial_preprocessing_opm
% test_tutorial_coregistration_opm
% test_tutorial_opm_helmet_design
%
% In its functional behavior it is expected that download_data() is called from
% within a .test folder, which resides in a folder that will then be the
% 'basedir' folder in which the fieldtrip and data folders will be created.
% After running this function, you should have a folder setup up that looks
% as follows:
%
% <toolkit2026> 
% |
% | _.test
% |   |_run_test()
% |   |_download_data()
% |_fieldtrip-<somedate>
% |_data
%     |_Subject01.ds
%     |_<etc>
%

filename  = mfilename('fullpath');
filename  = strrep(filename, '.test', 'somethingirrelevant'); %fileparts does not like the hidden directory
[p, f, e] = fileparts(filename);
basedir   = strrep(p, 'somethingirrelevant', '');
cd(basedir);

% download and unzip fieldtrip into the newly created folder
fprintf('downloading and unzipping fieldtrip\n');
url_fieldtrip = 'https://github.com/fieldtrip/fieldtrip/archive/refs/tags/20260904.zip';
unzip(url_fieldtrip);

% create a folder (within toolkit2026) that will contain the data, to keep a clean structure
fprintf('creating data folder\n');
mkdir('data');
cd('data');

% then download and unzip the Subject01 dataset
fprintf('downloading data\n');
url_subject01 = 'https://download.fieldtriptoolbox.org/tutorial/Subject01.zip';
unzip(url_subject01);

% we also need to download some other data for the respective hands on sessions:
mkdir('preprocessing_opm');
cd('preprocessing_opm');
url_tutorial = 'https://download.fieldtriptoolbox.org/tutorial/preprocessing_opm';
fnames = {'MedianNerve_StimBreakStim2min_Pos1.fif' 'MedianNerve_StimBreakStim2min_Pos2.fif' 'MedianNerve_StimBreakStim2min_Pos3.fif'};
for k = 1:numel(fnames)
  websave(fnames{k}, fullfile(url_tutorial, fnames{k}));
end
cd(fullfile(basedir, 'data'));

mkdir('denoising_opm');
cd('denoising_opm');
url_tutorial = 'https://download.fieldtriptoolbox.org/tutorial/denoising_opm/tutorialdata.zip';
unzip(url_tutorial);
cd(fullfile(basedir, 'data'));

mkdir('coregistration_opm');
cd('coregistration_opm');
url_tutorial = 'https://download.fieldtriptoolbox.org/tutorial/coregistration_opm';
fnames = {'example1_head_markers.pos' 'example2_magneticphantom_HPIplusdipoleset6_raw.fif' 'example3_anatomical.nii' 'example3_face_helmet.obj' 'example3_face_helmet_aligned.mat' 'example3_mri_realigned.mat' 'fieldlinebeta2_helmet_rim.mat'};
for k = 1:numel(fnames)
  websave(fnames{k}, fullfile(url_tutorial, fnames{k}));
end
cd(fullfile(basedir, 'data'));

mkdir('beamformer');
cd('beamformer');
url_tutorial = 'https://download.fieldtriptoolbox.org/tutorial/beamformer';
fnames = {'Subject01.mri' 'dataPost.mat' 'dataPre.mat' 'data_all.mat' 'freqPost.mat' 'freqPre.mat' 'headmodel.mat' 'segmentedmri.mat' 'sourcePost_con.mat' 'sourcePost_nocon.mat' 'sourcePre_con.mat' 'sourcemodel.mat'};
for k = 1:numel(fnames)
  websave(fnames{k}, fullfile(url_tutorial, fnames{k}));
end
cd(fullfile(basedir, 'data'));

mkdir('opm_helmet_design');
cd('opm_helmet_design');
url_tutorial = 'https://download.fieldtriptoolbox.org/tutorial/opm_helmet_design';
fnames = {'spherical-head.stl' 'spherical-helmet.stl' 'individual.nii' 'flattenedspherical-head.stl' 'flattenedspherical-helmet.stl' 'fieldline_sensor.stl' 'fieldline_padding.stl' 'fieldline_hole.stl' 'fieldline_holder.stl'};
for k = 1:numel(fnames)
  websave(fnames{k}, fullfile(url_tutorial, fnames{k}));
end
mkdir('population');
cd('population');
fnames = {};
for k = 1:10
  fnames{end+1} = sprintf('population/fiducial%03d.mat',k);
  fnames{end+1} = sprintf('population/subject%03d.nii',k);
end
for k = 1:numel(fnames)
  websave(strrep(fnames{k}, 'population/', ''), fullfile(url_tutorial, fnames{k}));
end
cd(fullfile(basedir, 'data'));


mkdir('cluster_permutation_timelock');
cd('cluster_permutation_timelock');
url_tutorial = 'https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_timelock';
fnames = {'ERF_orig.mat' 'GA_ERF_orig.mat' 'dataFC_LP.mat' 'dataFIC_LP.mat' 'stat_ERF_axial_FICvsFC.mat'             'stat_ERF_planar_FICvsFC.mat'};
for k = 1:numel(fnames)
  websave(fnames{k}, fullfile(url_tutorial, fnames{k}));
end
cd(basedir);
