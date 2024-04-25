---
title: Converting the combined MEG/fMRI MOUS dataset for sharing in BIDS
tags: [example, bids, sharing, anonymize]
---

# Converting the combined MEG/fMRI MOUS dataset for sharing in BIDS

The [BIDS standard](https://bids.neuroimaging.io) describes a simple and easy to adopt way of organizing neuroimaging and behavioral data. This example describes how we prepared a combined MEG/fMRI dataset in BIDS format for sharing. The project involved 204 subjects, which participated in either a auditory or a visual version of a language experiment. For every subject resting-state and task MEG and fMRI was recorded. The data and the experiment are described in more details in the references that you find at the end of this page.

{% include markup/green %}
The data is shared on the Donders Repository with the digital object identifier [10.34973/37n0-yc51](https://doi.org/10.34973/37n0-yc51) and the corresponding publication "A 204-subject multimodal neuroimaging dataset to study language processing" has been published as [10.1038/s41597-019-0020-y](https://doi.org/10.1038/s41597-019-0020-y).
{% include markup/end %}

Although we acquired slightly more data than published, the part that we share for these 204 subjects consists of

- anatomical MRI
- diffusion weighted MRI
- functional MRI
  - resting state
  - functional task
- MEG
  - resting state
  - functional task

MEG was acquired with a 275 channel CTF system. MRI was acquired with a 3T Siemens scanner. For the coregistration of the MEG with the anatomical MRI, the head shape was recorded using a Polhemus electromagnetic tracker. Digital photo's of the anatomical landmark at both ears were taken. Furthermore, head localizer coils were used for MEG coregistration as usual.

Stimulus presentation was done using using [NBS Presentation](https://www.neurobs.com). For MEG the events are coded as triggers in the data set. Both for MEG and MRI the presentation log files are shared and used to create/extend the _events.tsv_ sidecar files for the task data.

The shared data is organized according to [BIDS](http://bids.neuroimaging.io), the Brain Imaging Data Structure. This not only gives structure to the organization of the data files, but also helps to ensure that appropriate metadata and documentation are shared. We believe that this will facilitate reuse and increase the value of the shared data.

## Procedure

Prior to conversion, the total dataset contains some 2000 files per subject (many of them are DICOMs), which totals to around 400.000 files. After conversion the total dataset consists of approximately 10.000 files. The dataset is about 1 TB in volume.

The organization of the original raw data is like this

```text
raw/README.txt
raw/A2001
raw/A2002
raw/A2003
...
raw/V1001
raw/V1002
raw/V1003
...
```

with this underlying directory structure

```text
raw/A2001/behaviour
raw/A2001/genetics
raw/A2001/meg
raw/A2001/mri_anatomy
raw/A2001/mri_dti
raw/A2001/mri_other
raw/A2001/mri_restingstate
raw/A2001/mri_spectroscopy
raw/A2001/mri_task
```

for each subject. The actual data files (CTF, DICOM, Presentation log files, Polhemus, etc.) are located in these directories.

{% include markup/yellow %}
Since preparing the data for publication and creating this page, the **[data2bids](/reference/data2bids)** function has been greatly improved. Nowadays Bash and Python are not needed any more, but (almost) the whole dataset conversion and reorganization can be done with a MATLAB script. The only part where the Linux command line is still needed is for renaming and anonimizing the CTF datasets, which requires the `newDs` command line application.

We keep the documentation here for reference, but suggest that you look at more recent examples to learn how to [convert your data to BIDS](/tag/bids).
{% include markup/end %}

The procedure for converting the original data consists of a number of steps

1.  Create empty directory structure according to BIDS
2.  Collect and convert MRI data from DICOM to NIFTI
3.  Collect and rename the CTF MEG datasets
4.  Collect the NBS Presentation log files
5.  Collect the MEG coregistered anatomical MRIs
6.  Create the sidecar files for each dataset
7.  Create the general sidecar files
8.  Finalize

Step 1-5 and step 7 are implemented using [Bash](<https://en.wikipedia.org/wiki/Bash_(Unix_shell)>) scripts. The construction of the sidecar files in step 6 is implemented using the **[data2bids](/reference/data2bids)** function that is part of FieldTrip. The final step is not automated, but consists of some manual work.

After each of the automated steps the results should be checked. For that I have been using the command line applications like `find DIR -name PATTERN | wc -l` to count the number of files, but also a graphical databrowser to check the directory structure and a text editor to check the content of the JSON and TSV sidecar files.

It is important that you use appropriate tools. Command line utilities are very handy, but also a good graphical (code) editor that allows you to navigate through the full directory structure and check the file content. I have been using the Atom editor with the network directory mounted on my desktop computer. There are good [alternatives](https://alternativeto.net/software/atom/).

{% include markup/blue %}
The scripts are included on this page for completeness. You can also download them from our [download server](https://download.fieldtriptoolbox.org/example/bids_mous/).
{% include markup/end %}

### Step 1: create empty directory structure

```bash
RAW=/project/3011020.13/raw
BIDS=/project/3011020.13/bids

for SUB in A2002 A2003 A2004 A2005 A2006 A2007 A2008 A2009 A2010 A2011 A2013 A2014 A2015 A2016 A2017 A2019 A2020 A2021 A2024 A2025 A2027 A2028 A2029 A2030 A2031 A2032 A2033 A2034 A2035 A2036 A2037 A2038 A2039 A2040 A2041 A2042 A2046 A2047 A2049 A2050 A2051 A2052 A2053 A2055 A2056 A2057 A2058 A2059 A2061 A2062 A2063 A2064 A2065 A2066 A2067 A2068 A2069 A2070 A2071 A2072 A2073 A2075 A2076 A2077 A2078 A2079 A2080 A2083 A2084 A2085 A2086 A2088 A2089 A2090 A2091 A2092 A2094 A2095 A2096 A2097 A2098 A2099 A2101 A2102 A2103 A2104 A2105 A2106 A2108 A2109 A2110 A2111 A2113 A2114 A2116 A2117 A2119 A2120 A2121 A2122 A2124 A2125 V1001 V1002 V1003 V1004 V1005 V1006 V1007 V1008 V1009 V1010 V1011 V1012 V1013 V1015 V1016 V1017 V1019 V1020 V1022 V1024 V1025 V1026 V1027 V1028 V1029 V1030 V1031 V1032 V1033 V1034 V1035 V1036 V1037 V1038 V1039 V1040 V1042 V1044 V1045 V1046 V1048 V1049 V1050 V1052 V1053 V1054 V1055 V1057 V1058 V1059 V1061 V1062 V1063 V1064 V1065 V1066 V1068 V1069 V1070 V1071 V1072 V1073 V1074 V1075 V1076 V1077 V1078 V1079 V1080 V1081 V1083 V1084 V1085 V1086 V1087 V1088 V1089 V1090 V1092 V1093 V1094 V1095 V1097 V1098 V1099 V1100 V1101 V1102 V1103 V1104 V1105 V1106 V1107 V1108 V1109 V1110 V1111 V1113 V1114 V1115 V1116 V1117 ; do
mkdir -p $BIDS/sub-$SUB/meg
mkdir -p $BIDS/sub-$SUB/func
mkdir -p $BIDS/sub-$SUB/anat
mkdir -p $BIDS/sub-$SUB/dwi
done

mkdir -p $BIDS/code
mkdir -p $BIDS/stimuli
mkdir -p $BIDS/source
```

### Step 2: collect and convert MRI data from DICOM to NIFTI

In this section we are using [dcm2niix](https://github.com/rordenlab/dcm2niix) not only to convert the DICOMs to nifti, but also to create the initial json sidecar files with the information about the MR scan parameters. In step 6 we will update the sidecar files with information that is not available in the DICOMs, such as the task instructions.

```bash
RAW=/project/3011020.13/raw
BIDS=/project/3011020.13/bids

for SUB in A2002 A2003 A2004 A2005 A2006 A2007 A2008 A2009 A2010 A2011 A2013 A2014 A2015 A2016 A2017 A2019 A2020 A2021 A2024 A2025 A2027 A2028 A2029 A2030 A2031 A2032 A2033 A2034 A2035 A2036 A2037 A2038 A2039 A2040 A2041 A2042 A2046 A2047 A2049 A2050 A2051 A2052 A2053 A2055 A2056 A2057 A2058 A2059 A2061 A2062 A2063 A2064 A2065 A2066 A2067 A2068 A2069 A2070 A2071 A2072 A2073 A2075 A2076 A2077 A2078 A2079 A2080 A2083 A2084 A2085 A2086 A2088 A2089 A2090 A2091 A2092 A2094 A2095 A2096 A2097 A2098 A2099 A2101 A2102 A2103 A2104 A2105 A2106 A2108 A2109 A2110 A2111 A2113 A2114 A2116 A2117 A2119 A2120 A2121 A2122 A2124 A2125 V1001 V1002 V1003 V1004 V1005 V1006 V1007 V1008 V1009 V1010 V1011 V1012 V1013 V1015 V1016 V1017 V1019 V1020 V1022 V1024 V1025 V1026 V1027 V1028 V1029 V1030 V1031 V1032 V1033 V1034 V1035 V1036 V1037 V1038 V1039 V1040 V1042 V1044 V1045 V1046 V1048 V1049 V1050 V1052 V1053 V1054 V1055 V1057 V1058 V1059 V1061 V1062 V1063 V1064 V1065 V1066 V1068 V1069 V1070 V1071 V1072 V1073 V1074 V1075 V1076 V1077 V1078 V1079 V1080 V1081 V1083 V1084 V1085 V1086 V1087 V1088 V1089 V1090 V1092 V1093 V1094 V1095 V1097 V1098 V1099 V1100 V1101 V1102 V1103 V1104 V1105 V1106 V1107 V1108 V1109 V1110 V1111 V1113 V1114 V1115 V1116 V1117 ; do

echo ============ $SUB ============

dcm2niix -i y -b y -ba y -o ${BIDS}/sub-${SUB}/anat -f sub-${SUB}_T1w ${RAW}/${SUB}/mri_anatomy
dcm2niix -i y -b y -ba y -o ${BIDS}/sub-${SUB}/dwi  -f sub-${SUB}_dwi ${RAW}/${SUB}/mri_dti
dcm2niix -i y -b y -ba y -o ${BIDS}/sub-${SUB}/func -f sub-${SUB}_task-rest_bold ${RAW}/${SUB}/mri_restingstate

if [[ $SUB == A* ]]; then
dcm2niix -i y -b y -ba y -o ${BIDS}/sub-${SUB}/func -f sub-${SUB}_task-auditory_bold ${RAW}/${SUB}/mri_task
fi

if [[ $SUB == V* ]]; then
dcm2niix -i y -b y -ba y -o ${BIDS}/sub-${SUB}/func -f sub-${SUB}_task-visual_bold ${RAW}/${SUB}/mri_task
fi

done
```

### Step 3: collect and rename the CTF MEG datasets

In this step we are copying and renaming the CTF datasets to the target location using a CTF command line utility. During this process, the identifying information about the subject (i.e name) is removed from the dataset. Since the "newDs -anon" option does not remove the time and date of the recording from the dataset, at the end we do another step to remove the date of acquisition from the res4 header file. We keep the time, as it is not unique enough to identify which recording goes with which participant. See also this [frequently asked question](/faq/how_can_i_anonymize_a_ctf_dataset).

```bash
RAW=/project/3011020.13/raw
BIDS=/project/3011020.13/bids

function contains() {
  local n=$#
  local value=${!n}
  for ((i=1;i < $#;i++)) {
      if [ "${!i}" == "${value}" ]; then
          echo "y"
          return 0
      fi
  }
  echo "n"
  return 1

}

TASKLIST=(A2002_301102009_03.ds A2003_301102009_02.ds A2004_301102009_02.ds A2005_301102009_02.ds A2006_301102009_02.ds A2007_301102009_02.ds A2008_301102009_02.ds A2009_301102009_02.ds A2010_301102009_02.ds A2011_301102009_02.ds A2011_301102009_03.ds A2013_301102009_02.ds A2014_301102009_02.ds A2015_301102009_02.ds A2016_301102009_02.ds A2017_301102009_02.ds A2019_301102009_02.ds A2020_301102009_02.ds A2021_301102009_02.ds A2024_301102009_02.ds A2025_301102009_02.ds A2027_301102009_02.ds A2028_301102009_02.ds A2029_301102009_02.ds A2030_301102009_02.ds A2031_301102009_02.ds A2032_301102009_02.ds A2033_301102009_02.ds A2034_301102009_02.ds A2035_301102009_03.ds A2036_301102009_02.ds A2036_301102009_03.ds A2037_301102009_02.ds A2038_301102009_02.ds A2039_301102009_02.ds A2040_301102009_02.ds A2041_301102009_02.ds A2042_301102009_02.ds A2046_301102009_02.ds A2047_301102009_02.ds A2049_301102009_02.ds A2050_301102009_02.ds A2051_301102009_02.ds A2052_301102009_03.ds A2053_301102009_02.ds A2055_301102009_02.ds A2056_301102009_02.ds A2057_301102009_02.ds A2058_301102009_02.ds A2059_301102009_02.ds A2061_301102009_03.ds A2062_301102009_02.ds A2062_301102009_03.ds A2063_301102009_02.ds A2063_301102009_03.ds A2064_301102009_02.ds A2065_301102009_02.ds A2066_301102009_02.ds A2067_301102009_02.ds A2068_301102009_02.ds A2069_301102009_02.ds A2070_301102009_02.ds A2071_301102009_02.ds A2072_301102009_02.ds A2073_301102009_02.ds A2075_301102009_02.ds A2076_301102009_02.ds A2076_301102009_03.ds A2077_301102009_02.ds A2078_301102009_02.ds A2079_301102009_02.ds A2080_301102009_02.ds A2083_301102009_02.ds A2084_301102009_02.ds A2084_301102009_03.ds A2085_301102009_02.ds A2086_301102009_02.ds A2088_301102009_02.ds A2089_301102009_02.ds A2090_301102009_02.ds A2091_301102009_02.ds A2092_301102009_02.ds A2094_301102009_02.ds A2095_301102009_02.ds A2096_301102009_02.ds A2097_301102009_02.ds A2098_301102009_02.ds A2099_301102009_02.ds A2101_301102009_02.ds A2102_301102009_02.ds A2103_301102009_03.ds A2104_301102009_02.ds A2105_301102009_03.ds A2106_301102009_02.ds A2108_301102009_02.ds A2109_301102009_02.ds A2110_301102009_02.ds A2111_301102009_02.ds A2113_301102009_02.ds A2114_301102009_02.ds A2116_301102009_02.ds A2117_301102009_02.ds A2119_301102009_02.ds A2120_301102009_02.ds A2121_301102009_02.ds A2122_301102009_02.ds A2124_301102009_02.ds A2125_301102009_02.ds V1001_301102009_01.ds V1002_301102009_01.ds V1003_301102009_01.ds V1004_301102009_02.ds V1005_301102009_01.ds V1006_301102009_03.ds V1006_301102009_04.ds V1007_301102009_02.ds V1008_301102009_02.ds V1009_301102009_02.ds V1010_301102009_02.ds V1011_301102009_02.ds V1012_301102009_03.ds V1013_301102009_02.ds V1015_301102009_03.ds V1016_301102009_02.ds V1017_301102009_02.ds V1019_301102009_02.ds V1020_301102009_02.ds V1022_301102009_02.ds V1024_301102009_02.ds V1025_301102009_02.ds V1026_301102009_02.ds V1027_301102009_02.ds V1028_301102009_02.ds V1029_301102009_02.ds V1030_301102009_02.ds V1031_301102009_03.ds V1032_301102009_02.ds V1033_301102009_02.ds V1034_301102009_02.ds V1035_301102009_02.ds V1036_301102009_02.ds V1037_301102009_02.ds V1038_301102009_02.ds V1039_301102009_02.ds V1040_301102009_02.ds V1042_301102009_02.ds V1044_301102009_02.ds V1045_301102009_02.ds V1046_301102009_02.ds V1048_301102009_02.ds V1049_301102009_02.ds V1050_301102009_02.ds V1052_301102009_02.ds V1053_301102009_02.ds V1054_301102009_02.ds V1055_301102009_02.ds V1057_301102009_02.ds V1058_301102009_02.ds V1059_301102009_02.ds V1061_301102009_02.ds V1062_301102009_02.ds V1063_301102009_02.ds V1064_301102009_02.ds V1065_301102009_02.ds V1066_301102009_02.ds V1068_301102009_02.ds V1069_301102009_02.ds V1070_301102009_02.ds V1071_301102009_02.ds V1072_301102009_02.ds V1073_301102009_02.ds V1074_301102009_02.ds V1075_301102009_02.ds V1076_301102009_02.ds V1077_301102009_02.ds V1078_301102009_02.ds V1079_301102009_02.ds V1080_301102009_02.ds V1081_301102009_02.ds V1083_301102009_03.ds V1084_301102009_02.ds V1085_301102009_02.ds V1086_301102009_02.ds V1087_301102009_02.ds V1088_301102009_02.ds V1089_301102009_03.ds V1090_301102009_02.ds V1090_301102009_03.ds V1092_301102009_02.ds V1093_301102009_02.ds V1094_301102009_02.ds V1095_301102009_02.ds V1097_301102009_02.ds V1098_301102009_02.ds V1099_301102009_02.ds V1100_301102009_02.ds V1101_301102009_02.ds V1102_301102009_02.ds V1103_301102009_02.ds V1104_301102009_02.ds V1105_301102009_03.ds V1106_301102009_02.ds V1107_301102009_02.ds V1108_301102009_02.ds V1109_301102009_03.ds V1110_301102009_02.ds V1111_301102009_02.ds V1113_301102009_02.ds V1114_301102009_02.ds V1115_301102009_02.ds V1116_301102009_02.ds V1117_301102009_02.ds)
RESTLIST=(A2002_301102009_01.ds A2003_301102009_01.ds A2004_301102009_01.ds A2005_301102009_01.ds A2006_301102009_01.ds A2007_301102009_01.ds A2008_301102009_01.ds A2009_301102009_01.ds A2010_301102009_01.ds A2011_301102009_01.ds A2013_301102009_01.ds A2014_301102009_01.ds A2015_301102009_01.ds A2016_301102009_01.ds A2017_301102009_01.ds A2019_301102009_01.ds A2020_301102009_01.ds A2021_301102009_01.ds A2024_301102009_01.ds A2025_301102009_01.ds A2027_301102009_01.ds A2028_301102009_01.ds A2029_301102009_01.ds A2030_301102009_01.ds A2031_301102009_01.ds A2032_301102009_01.ds A2033_301102009_01.ds A2034_301102009_01.ds A2035_301102009_02.ds A2036_301102009_01.ds A2037_301102009_01.ds A2038_301102009_01.ds A2039_301102009_01.ds A2040_301102009_01.ds A2041_301102009_01.ds A2042_301102009_01.ds A2046_301102009_01.ds A2047_301102009_01.ds A2049_301102009_01.ds A2050_301102009_01.ds A2051_301102009_01.ds A2052_301102009_01.ds A2053_301102009_01.ds A2055_301102009_01.ds A2056_301102009_01.ds A2057_301102009_01.ds A2058_301102009_01.ds A2059_301102009_01.ds A2061_301102009_02.ds A2062_301102009_01.ds A2062_301102009_02.ds A2063_301102009_01.ds A2063_301102009_03.ds A2064_301102009_01.ds A2065_301102009_01.ds A2066_301102009_01.ds A2067_301102009_01.ds A2068_301102009_01.ds A2069_301102009_01.ds A2070_301102009_01.ds A2071_301102009_01.ds A2072_301102009_01.ds A2073_301102009_01.ds A2075_301102009_01.ds A2076_301102009_01.ds A2077_301102009_01.ds A2078_301102009_01.ds A2079_301102009_01.ds A2080_301102009_01.ds A2083_301102009_01.ds A2084_301102009_01.ds A2085_301102009_01.ds A2086_301102009_01.ds A2088_301102009_01.ds A2089_301102009_01.ds A2090_301102009_01.ds A2091_301102009_01.ds A2092_301102009_01.ds A2094_301102009_01.ds A2095_301102009_01.ds A2096_301102009_01.ds A2097_301102009_01.ds A2098_301102009_01.ds A2099_301102009_01.ds A2101_301102009_01.ds A2102_301102009_01.ds A2103_301102009_02.ds A2104_301102009_01.ds A2105_301102009_02.ds A2106_301102009_01.ds A2108_301102009_01.ds A2109_301102009_01.ds A2110_301102009_01.ds A2111_301102009_01.ds A2113_301102009_01.ds A2114_301102009_01.ds A2116_301102009_01.ds A2117_301102009_01.ds A2120_301102009_01.ds A2121_301102009_01.ds A2122_301102009_01.ds A2124_301102009_01.ds A2125_301102009_01.ds V1004_301102009_01.ds V1006_301102009_02.ds V1007_301102009_01.ds V1008_301102009_01.ds V1009_301102009_01.ds V1010_301102009_01.ds V1011_301102009_01.ds V1012_301102009_02.ds V1013_301102009_01.ds V1015_301102009_02.ds V1016_301102009_01.ds V1017_301102009_01.ds V1019_301102009_01.ds V1020_301102009_01.ds V1022_301102009_01.ds V1024_301102009_01.ds V1026_301102009_01.ds V1027_301102009_01.ds V1028_301102009_01.ds V1029_301102009_01.ds V1030_301102009_01.ds V1031_301102009_01.ds V1032_301102009_01.ds V1033_301102009_01.ds V1034_301102009_01.ds V1035_301102009_01.ds V1036_301102009_01.ds V1037_301102009_01.ds V1038_301102009_01.ds V1039_301102009_01.ds V1040_301102009_01.ds V1042_301102009_01.ds V1044_301102009_01.ds V1045_301102009_01.ds V1046_301102009_01.ds V1048_301102009_01.ds V1049_301102009_01.ds V1050_301102009_01.ds V1052_301102009_01.ds V1053_301102009_01.ds V1054_301102009_01.ds V1055_301102009_01.ds V1057_301102009_01.ds V1058_301102009_01.ds V1059_301102009_01.ds V1061_301102009_01.ds V1062_301102009_01.ds V1063_301102009_01.ds V1064_301102009_01.ds V1065_301102009_01.ds V1066_301102009_01.ds V1068_301102009_01.ds V1069_301102009_01.ds V1070_301102009_01.ds V1071_301102009_01.ds V1072_301102009_01.ds V1073_301102009_01.ds V1074_301102009_01.ds V1075_301102009_01.ds V1076_301102009_01.ds V1077_301102009_01.ds V1078_301102009_01.ds V1079_301102009_01.ds V1080_301102009_01.ds V1081_301102009_01.ds V1083_301102009_02.ds V1084_301102009_01.ds V1085_301102009_01.ds V1086_301102009_01.ds V1087_301102009_01.ds V1088_301102009_01.ds V1089_301102009_01.ds V1090_301102009_01.ds V1092_301102009_01.ds V1093_301102009_01.ds V1094_301102009_01.ds V1095_301102009_01.ds V1097_301102009_01.ds V1098_301102009_01.ds V1099_301102009_01.ds V1100_301102009_01.ds V1101_301102009_01.ds V1102_301102009_01.ds V1103_301102009_01.ds V1104_301102009_01.ds V1105_301102009_02.ds V1106_301102009_01.ds V1107_301102009_01.ds V1108_301102009_01.ds V1109_301102009_02.ds V1110_301102009_01.ds V1111_301102009_01.ds V1113_301102009_01.ds V1114_301102009_01.ds V1115_301102009_01.ds V1116_301102009_01.ds V1117_301102009_01.ds)

module load 32bit/ctf/6.15

for SUB in A2002 A2003 A2004 A2005 A2006 A2007 A2008 A2009 A2010 A2011 A2013 A2014 A2015 A2016 A2017 A2019 A2020 A2021 A2024 A2025 A2027 A2028 A2029 A2030 A2031 A2032 A2033 A2034 A2035 A2036 A2037 A2038 A2039 A2040 A2041 A2042 A2046 A2047 A2049 A2050 A2051 A2052 A2053 A2055 A2056 A2057 A2058 A2059 A2061 A2062 A2063 A2064 A2065 A2066 A2067 A2068 A2069 A2070 A2071 A2072 A2073 A2075 A2076 A2077 A2078 A2079 A2080 A2083 A2084 A2085 A2086 A2088 A2089 A2090 A2091 A2092 A2094 A2095 A2096 A2097 A2098 A2099 A2101 A2102 A2103 A2104 A2105 A2106 A2108 A2109 A2110 A2111 A2113 A2114 A2116 A2117 A2119 A2120 A2121 A2122 A2124 A2125 V1001 V1002 V1003 V1004 V1005 V1006 V1007 V1008 V1009 V1010 V1011 V1012 V1013 V1015 V1016 V1017 V1019 V1020 V1022 V1024 V1025 V1026 V1027 V1028 V1029 V1030 V1031 V1032 V1033 V1034 V1035 V1036 V1037 V1038 V1039 V1040 V1042 V1044 V1045 V1046 V1048 V1049 V1050 V1052 V1053 V1054 V1055 V1057 V1058 V1059 V1061 V1062 V1063 V1064 V1065 V1066 V1068 V1069 V1070 V1071 V1072 V1073 V1074 V1075 V1076 V1077 V1078 V1079 V1080 V1081 V1083 V1084 V1085 V1086 V1087 V1088 V1089 V1090 V1092 V1093 V1094 V1095 V1097 V1098 V1099 V1100 V1101 V1102 V1103 V1104 V1105 V1106 V1107 V1108 V1109 V1110 V1111 V1113 V1114 V1115 V1116 V1117 ; do

if [[ $SUB == A* ]]; then
TASK=auditory
else
TASK=visual
fi

for NUM in 01 02 03 04; do
DATASET=${SUB}_301102009_${NUM}.ds

if [ $(contains "${TASKLIST[@]}" "${DATASET}") == "y" ]; then
newDs -anon $RAW/$SUB/meg/${DATASET} $BIDS/sub-${SUB}/meg/sub-${SUB}_task-${TASK}_meg.ds
chmod -R u+rwX,g+rX-w,o+rX-w            $BIDS/sub-${SUB}/meg/sub-${SUB}_task-${TASK}_meg.ds

elif [ $(contains "${RESTLIST[@]}" "${DATASET}") == "y" ]; then
newDs -anon $RAW/$SUB/meg/${DATASET} $BIDS/sub-${SUB}/meg/sub-${SUB}_task-rest_meg.ds
chmod -R u+rwX,g+rX-w,o+rX-w            $BIDS/sub-${SUB}/meg/sub-${SUB}_task-rest_meg.ds

else
echo WARNING: dataset ${DATASET} is neither task, nor rest
fi

done # for NUM in 01 02 03 04

cp $RAW/$SUB/meg/${SUB}.pos      $BIDS/sub-${SUB}/meg/sub-${SUB}_headshape.pos
chmod -R u+rw-x,g+r-wx,o+r-wx    $BIDS/sub-${SUB}/meg/sub-${SUB}_headshape.pos

done # for SUB in ...

##################################################

# the following section deals with the exceptions.

# these are task datasets that consist of 2 ds

# directories upon acquisition, caused by DSQ problems

newDs -anon $RAW/A2011/meg/A2011_301102009_02.ds  $BIDS/sub-A2011/meg/sub-A2011_task-auditory_run-1_meg.ds
newDs -anon $RAW/A2011/meg/A2011_301102009_03.ds  $BIDS/sub-A2011/meg/sub-A2011_task-auditory_run-2_meg.ds
newDs -anon $RAW/A2062/meg/A2062_301102009_02.ds  $BIDS/sub-A2062/meg/sub-A2062_task-auditory_run-1_meg.ds
newDs -anon $RAW/A2062/meg/A2062_301102009_03.ds  $BIDS/sub-A2062/meg/sub-A2062_task-auditory_run-2_meg.ds
newDs -anon $RAW/A2063/meg/A2063_301102009_02.ds  $BIDS/sub-A2063/meg/sub-A2063_task-auditory_run-1_meg.ds
newDs -anon $RAW/A2063/meg/A2063_301102009_03.ds  $BIDS/sub-A2063/meg/sub-A2063_task-auditory_run-2_meg.ds
newDs -anon $RAW/A2076/meg/A2076_301102009_02.ds  $BIDS/sub-A2076/meg/sub-A2076_task-auditory_run-1_meg.ds
newDs -anon $RAW/A2076/meg/A2076_301102009_03.ds  $BIDS/sub-A2076/meg/sub-A2076_task-auditory_run-2_meg.ds
newDs -anon $RAW/A2084/meg/A2084_301102009_02.ds  $BIDS/sub-A2084/meg/sub-A2084_task-auditory_run-1_meg.ds
newDs -anon $RAW/A2084/meg/A2084_301102009_03.ds  $BIDS/sub-A2084/meg/sub-A2084_task-auditory_run-2_meg.ds
newDs -anon $RAW/V1006/meg/V1006_301102009_03.ds  $BIDS/sub-V1006/meg/sub-V1006_task-visual_run-1_meg.ds
newDs -anon $RAW/V1006/meg/V1006_301102009_04.ds  $BIDS/sub-V1006/meg/sub-V1006_task-visual_run-2_meg.ds
newDs -anon $RAW/V1090/meg/V1090_301102009_02.ds  $BIDS/sub-V1090/meg/sub-V1090_task-visual_run-1_meg.ds
newDs -anon $RAW/V1090/meg/V1090_301102009_03.ds  $BIDS/sub-V1090/meg/sub-V1090_task-visual_run-2_meg.ds

####################################################################################################

# the anon option of newDs does not remove the date and/or time of the recording

####################################################################################################
find $BIDS -name \*.res4 -exec $HOME/bids-tools/bin/remove_ctf_datetime -d {} \;
```

{% include markup/blue %}
You can see a few exceptions, which reflect datasets that did not convert well automatically. The reason for this is the fact that during data acquisition, the data ended up in two different .ds datasets. According to BIDS, these are supposed to be represented by different 'runs'.
{% include markup/end %}

### Step 4: collect the NBS Presentation log files

All Presentation log files are copied from their original location to the sourcedata folder. Although in step 6 the events in the log files will be used to construct the events.tsv files, we want to keep (and share) the Presentation log files, as those contain slightly more information than what can be represented in the events.tsv.

One issue is that the Presentation log files contains the exact date and time of the experiment. To avoid possible identification of participants, we are using [sed](https://www.gnu.org/software/sed/manual/sed.html) to replace the time and date in the files.

```bash
RAW=/project/3011020.13/raw
BIDS=/project/3011020.13/bids

for SUB in A2002 A2003 A2004 A2005 A2006 A2007 A2008 A2009 A2010 A2011 A2013 A2014 A2015 A2016 A2017 A2019 A2020 A2021 A2024 A2025 A2027 A2028 A2029 A2030 A2031 A2032 A2033 A2034 A2035 A2036 A2037 A2038 A2039 A2040 A2041 A2042 A2046 A2047 A2049 A2050 A2051 A2052 A2053 A2055 A2056 A2057 A2058 A2059 A2061 A2062 A2063 A2064 A2065 A2066 A2067 A2068 A2069 A2070 A2071 A2072 A2073 A2075 A2076 A2077 A2078 A2079 A2080 A2083 A2084 A2085 A2086 A2088 A2089 A2090 A2091 A2092 A2094 A2095 A2096 A2097 A2098 A2099 A2101 A2102 A2103 A2104 A2105 A2106 A2108 A2109 A2110 A2111 A2113 A2114 A2116 A2117 A2119 A2120 A2121 A2122 A2124 A2125 V1001 V1002 V1003 V1004 V1005 V1006 V1007 V1008 V1009 V1010 V1011 V1012 V1013 V1015 V1016 V1017 V1019 V1020 V1022 V1024 V1025 V1026 V1027 V1028 V1029 V1030 V1031 V1032 V1033 V1034 V1035 V1036 V1037 V1038 V1039 V1040 V1042 V1044 V1045 V1046 V1048 V1049 V1050 V1052 V1053 V1054 V1055 V1057 V1058 V1059 V1061 V1062 V1063 V1064 V1065 V1066 V1068 V1069 V1070 V1071 V1072 V1073 V1074 V1075 V1076 V1077 V1078 V1079 V1080 V1081 V1083 V1084 V1085 V1086 V1087 V1088 V1089 V1090 V1092 V1093 V1094 V1095 V1097 V1098 V1099 V1100 V1101 V1102 V1103 V1104 V1105 V1106 V1107 V1108 V1109 V1110 V1111 V1113 V1114 V1115 V1116 V1117 ; do
for TYP in meg mri_task ; do

INPUT=`ls $RAW/$SUB/$TYP/*.log`
OUTPUT=$BIDS/source/$TYP/$(basename $INPUT)
echo copying presentation log and scrubbing date from $OUTPUT

cat $INPUT | sed s/'Logfile written.*'/'Logfile written - 01\/01\/1970 00:00:00\r'/g > $OUTPUT

done
done
```

### Step 5: collect the MEG coregistered anatomical MRIs

The coregistration of the MEG recording with the anatomical MRI has been done on basis of the head localizer coils (placed at Nasion and on two [ear molds](/faq/how_are_the_lpa_and_rpa_points_defined) on either side), the anatomical landmarks (Nasion, LPA, RPA) and using the scalp surface that was recorded with the Polhemus. This coregistration was done using **[ft_volumerealign](/reference/ft_volumerealign)** and the resulting anatomical MRI was saved back to disk in NIFTI format.

Since the orientation of the CTF coregistered MRI has been flipped relative to the NIFTI file that was generated by dcm2niix, we are sharing both. The native one is most convenient for processing the functional MRI and DWI data, whereas the one in CTF space is most convenient for processing the MEG data.

The CTF coregistered MRI gets the same json sidecar file as the one converted by dcm2niix, which will be updated in step 6 regarding the coordinate system.

```bash
PROCESSED=/project/3011020.09/processed
BIDS=/project/3011020.13/bids

for SUB in A2002 A2003 A2004 A2005 A2006 A2007 A2008 A2009 A2010 A2011 A2013 A2014 A2015 A2016 A2017 A2019 A2020 A2021 A2024 A2025 A2027 A2028 A2029 A2030 A2031 A2032 A2033 A2034 A2035 A2036 A2037 A2038 A2039 A2040 A2041 A2042 A2046 A2047 A2049 A2050 A2051 A2052 A2053 A2055 A2056 A2057 A2058 A2059 A2061 A2062 A2063 A2064 A2065 A2066 A2067 A2068 A2069 A2070 A2071 A2072 A2073 A2075 A2076 A2077 A2078 A2079 A2080 A2083 A2084 A2085 A2086 A2088 A2089 A2090 A2091 A2092 A2094 A2095 A2096 A2097 A2098 A2099 A2101 A2102 A2103 A2104 A2105 A2106 A2108 A2109 A2110 A2111 A2113 A2114 A2116 A2117 A2119 A2120 A2121 A2122 A2124 A2125 V1001 V1002 V1003 V1004 V1005 V1006 V1007 V1008 V1009 V1010 V1011 V1012 V1013 V1015 V1016 V1017 V1019 V1020 V1022 V1024 V1025 V1026 V1027 V1028 V1029 V1030 V1031 V1032 V1033 V1034 V1035 V1036 V1037 V1038 V1039 V1040 V1042 V1044 V1045 V1046 V1048 V1049 V1050 V1052 V1053 V1054 V1055 V1057 V1058 V1059 V1061 V1062 V1063 V1064 V1065 V1066 V1068 V1069 V1070 V1071 V1072 V1073 V1074 V1075 V1076 V1077 V1078 V1079 V1080 V1081 V1083 V1084 V1085 V1086 V1087 V1088 V1089 V1090 V1092 V1093 V1094 V1095 V1097 V1098 V1099 V1100 V1101 V1102 V1103 V1104 V1105 V1106 V1107 V1108 V1109 V1110 V1111 V1113 V1114 V1115 V1116 V1117 ; do

# The <space-xxx> label is not defined in BIDS 1.1.1, but it is planned
# in BEP010 (iEEG) to deal with coregistration and coordinate systems.

cp $PROCESSED/${SUB}/meg/anatomy/${SUB}coregCTF.nii    $BIDS/sub-${SUB}/anat/sub-${SUB}_space-CTF_T1w.nii

# The original T1w data is the same, but the NIFTI is slightly different
# due to being processed for coregistration with the CTF coordinate system.
# Hence the json of the original T1w can be copied over.

cp $BIDS/sub-${SUB}/anat/sub-${SUB}_T1w.json           $BIDS/sub-${SUB}/anat/sub-${SUB}_space-CTF_T1w.json

done
```

### Step 6: create the sidecar files for each dataset in MATLAB

```matlab
bidsroot = '/project/3011020.13/bids';
subject  = dir(fullfile(bidsroot, 'sub-*'));
subject  = {subject.name};

% exception

% trigger issue, causes mismatch in the alignment when using the default
exceptions_meg(1).subject   = {'sub-V1077'};
exceptions_meg(1).pres_type = 'Picture';
exceptions_meg(1).pres_val  = '8*';
exceptions_meg(1).trig_val  = 8;
exceptions_meg(1).skip      = 'none';

% trigger issue, causes mismatch in the alignment when using the default
exceptions_meg(2).subject   = {'sub-A2009';'sub-A2014';'sub-A2029';...
                             'sub-A2031';'sub-A2033';'sub-A2035';...
                             'sub-A2037';'sub-A2040';'sub-A2041';...
                             'sub-A2042';'sub-A2046';'sub-A2047';...
                             'sub-A2051';'sub-A2053';'sub-A2056';...
                             'sub-A2057';'sub-A2059';'sub-A2064';...
                             'sub-A2066'};
exceptions_meg(2).pres_type = 'Nothing';
exceptions_meg(2).pres_val  = '6 t*';
exceptions_meg(2).trig_val  = 6;
exceptions_meg(2).skip      = 'none';

% level-mode trigger issue, requires events to be fixed
exceptions_meg(3).subject   = {'sub-A2039' 'sub-A2050'};
exceptions_meg(3).extra     = 'fix_events';
exceptions_meg(3).pres_type = 'Nothing';
exceptions_meg(3).pres_val  = '8 t*';
exceptions_meg(3).trig_val  = 8;

passed = true(numel(subject),6);
for i=1:numel(subject)

anat = dir(fullfile(bidsroot, subject{i}, 'anat', '*.nii'));
func = dir(fullfile(bidsroot, subject{i}, 'func', '*.nii'));
dwi  = dir(fullfile(bidsroot, subject{i}, 'dwi',  '*.nii'));
meg  = dir(fullfile(bidsroot, subject{i}, 'meg',  '*.ds'));

catfile = @(p, f) fullfile(p, f);

anat = cellfun(catfile, {anat.folder}, {anat.name}, 'UniformOutput', 0);
func = cellfun(catfile, {func.folder}, {func.name}, 'UniformOutput', 0);
dwi  = cellfun(catfile, {dwi.folder},  {dwi.name},  'UniformOutput', 0);
meg  = cellfun(catfile, {meg.folder},  {meg.name},  'UniformOutput', 0);

dataset = cat(1, anat(:), func(:), dwi(:), meg(:));

for j=1:numel(dataset)
  cfg = [];
  cfg.dataset                     = dataset{j};

  cfg.mri.writesidecar            = 'merge';
  cfg.meg.writesidecar            = 'replace';
  cfg.channels.writesidecar       = 'replace';
  cfg.events.writesidecar         = 'replace';
  cfg.coordsystem.writesidecar    = 'replace';

  cfg.InstitutionName             = 'Radboud University';
  cfg.InstitutionalDepartmentName = 'Donders Institute for Brain, Cognition and Behaviour';
  cfg.InstitutionAddress          = 'Kapittelweg 29, 6525 EN, Nijmegen, The Netherlands';

  if contains(cfg.dataset, 'task-rest')
    cfg.TaskName = 'Resting state';
  elseif contains(cfg.dataset, 'task-visual')
    cfg.TaskName = 'Visual language task';
  elseif  contains(cfg.dataset, 'task-auditory')
    cfg.TaskName = 'Auditory language task';
  end

  if endsWith(cfg.dataset, '.ds')
    % these are task-dependent
    pres_type = [];
    pres_val  = [];
    trig_val  = [];
    skip      = [];

    % these settings work most of the time
    if contains(cfg.dataset, 'task-auditory')
      pres_type = 'Nothing';
      pres_val  = '3 Audi*';
      trig_val  = 3;
    elseif contains(cfg.dataset, 'task-visual')
      pres_type = 'Picture';
      pres_val  = '6*';
      trig_val  = 6;
    end

    % this aims to deal with the exceptions
    for k = 1:numel(exceptions_meg)
      if ismember(subject{i}, exceptions_meg(k).subject)
        pres_type = ft_getopt(exceptions_meg(k), 'pres_type', pres_type);
        pres_val  = ft_getopt(exceptions_meg(k), 'pres_val',  pres_val);
        trig_val  = ft_getopt(exceptions_meg(k), 'trig_val',  trig_val);
        skip      = ft_getopt(exceptions_meg(k), 'skip',      skip);

        if ~isempty(exceptions_meg(k).extra)
          switch exceptions_meg(k).extra
            case 'fix_events'
              % this requires you to have the mous github repository on your path
              if contains(cfg.dataset, 'auditory')
                event = mous_read_event_audio(cfg.dataset);
                for kk = 1:numel(event)
                  event(kk).duration = [];
                end
                cfg.trigger.event = event;
              end
            otherwise
          end
        end
      end
    end

    if contains(cfg.dataset, 'task-auditory') || contains(cfg.dataset, 'task-visual')
      if isempty(skip)
        if contains(cfg.dataset, 'run-1')
          skip = 'last';
        elseif contains(cfg.dataset, 'run-2')
          skip = 'first';
        else
          skip = 'none';
        end
      end

      % this only applies to MEG task data
      pfile = dir(fullfile(bidsroot, 'sourcedata', 'meg', [subject{i}(5:end) '*.log']));
      cfg.presentationfile   = fullfile(pfile.folder, pfile.name);
      cfg.trigger.eventtype  = 'UPPT001';
      cfg.presentation.skip  = skip;
      cfg.trigger.eventvalue = trig_val;
      cfg.presentation.eventtype  = pres_type;
      cfg.presentation.eventvalue = pres_val;
    end

    cfg.meg.DigitizedLandmarks      = true;
    cfg.meg.DigitizedHeadPoints     = true;
    cfg.meg.PowerLineFrequency      = 50;
    cfg.meg.DewarPosition           = 'upright';
    cfg.meg.SoftwareFilters         = 'n/a';

    % this will be specified on basis of the CTF dataset header
    % cfg.coordsystem.MEGCoordinateSystem
    % cfg.coordsystem.MEGCoordinateUnits
    cfg.coordsystem.MEGCoordinateSystemDescription = 'CTF coordinates relative to the localizer coils, with the localizer coils at nasion and left and right ear canal';

    % this will be specified on basis of the CTF dataset header
    % cfg.coordsystem.HeadCoilCoordinates
    % cfg.coordsystem.HeadCoilCoordinateSystem
    % cfg.coordsystem.HeadCoilCoordinateUnits
    cfg.coordsystem.HeadCoilCoordinateSystemDescription = 'CTF coordinates relative to the localizer coils, with the localizer coils at nasion and left and right ear canal';
    cfg.coordsystem.IntendedFor = sprintf('anat/%s_space-CTF_T1w.nii', subject{i});

    cfg.coordsystem.DigitizedHeadPoints = sprintf('%s_headshape.pos', subject{i});
    cfg.coordsystem.DigitizedHeadPointsCoordinateSystem = 'CTF';
    cfg.coordsystem.DigitizedHeadPointsCoordinateUnits = 'cm';
    cfg.coordsystem.DigitizedHeadPointsCoordinateSystemDescription = 'CTF coordinates relative to the nasion and left and right pre-auricular points';

    % cfg.coordsystem.AnatomicalLandmarkCoordinates
    % cfg.coordsystem.AnatomicalLandmarkCoordinateSystem
    % cfg.coordsystem.AnatomicalLandmarkCoordinateUnits
    % cfg.coordsystem.AnatomicalLandmarkCoordinateSystemDescription

    cfg.coordsystem.FiducialsDescription = [ ...
      'Coregistration was initially done using the approximate position of the '...
      'head localizer coils in the anatomical MRI and subsequently refined using the full '...
      'headshape measured with the Polhemus. The positions of the head localizer coils at '...
      'the ear canals (relative to the Polhemus coordinates) is included in the headshape file. '...
      'CTF coordinates in the MEG data and in the coregistered anatomical MRI are specified '...
      'relative to the localizer coils at nasion and left and right ear canal.'...
      ];

  elseif endsWith(cfg.dataset, '.nii')
    % this only applies to anatomical MR data
    if contains(cfg.dataset, 'anat')
      cfg.mri.deface = 'yes';
    end

    if contains(cfg.dataset, 'space-CTF')
      % these are added by dcm2niix to the original MRI, but differ for the coregistered anatomical MRI
      cfg.mri.ConversionSoftware = 'FieldTrip';
      cfg.mri.ConversionSoftwareVersion = ft_version;
    end

    if contains(cfg.dataset, 'task-auditory') || contains(cfg.dataset, 'task-visual')
      % this only applies to fMRI task data
      pfile = dir(fullfile(bidsroot, 'sourcedata', 'mri_task', [subject{i}(5:end) '*.log']));
      cfg.presentationfile = fullfile(pfile.folder, pfile.name);
      cfg.presentation.eventtype = 'Pulse';
      cfg.presentation.eventvalue = [];
    end

  end % if MEG or MRI

  data2bids(cfg)

  save_all_figures('/project_ext/3011020.13/bids/code');
  close all % figures

end % for each dataset
end % for each subject
```

<br>

{% include markup/blue %}
This script here deals with some dataset specific exceptions. Indeed, given the fact that we are working with real data here, due to various reasons, automatic conversions (one-size-fits-all) are likely to occasionally fail.

In the current context, the tricky part happened to be the creation of the events.tsv files for the MEG task data. In order to create these files, **[data2bids](/reference/data2bids)** attempts to align the experimental events, as extracted from the presentation software logfile, with the experimental events, as extracted from the digital trigger channel in the MEG data files. This only works well and unambiguously, if there's a one-to-one-mapping of the events (or a specific type of event) in the two representations.

In the current example, there were occasional issues with the digital trigger channel, which precluded fully automatic processing of all files. The resulting example script above is therefore the result of several iterations to deal with the exceptions.
{% include markup/end %}

### Step 7: create the general sidecar files

This step is again done on the Linux command line, using some tools that are shared [here](https://github.com/robertoostenveld/bids-tools). Some of the other tools might be useful in creating scripts to gather and/or reorganize your EEG, MEG, Presentation or DICOM data.

```bash
BIDS=/project/3011020.13/bids

$HOME/bids-tools/bin/create_sidecar_files  --description  $BIDS # create the dataset_description.json file
$HOME/bids-tools/bin/create_sidecar_files  --participants $BIDS # create the participants.tsv file
$HOME/bids-tools/bin/create_sidecar_files  --scans        $BIDS # create the scans.tsv files (per subject and session)
```

### Finalize

There are some things which are not implemented as a script, for example filling out the details in the top-level _dataset_description.json_ file, adding a _README_ file, updating the _CHANGES_ file.

I also manually renamed the subdirectories with the presentation log files in the _sourcedata_ directory, and added the presentation source code and stimulus material in the _stimuli_ directory.

Throughout the development of the scripts and and after having completed the conversion I used the [bids-validator](https://github.com/INCF/bids-validator/) to check compliance with BIDS. During script development it revealed errors and inconsistencies, which I fixed in the scripts (which I then reran). After the final conversion there were still some warnings printed, but the dataset passed the validator.

## Issues

Although the scripts are presented in a linear fashion, the actual conversion of the whole dataset took some effort, especially in dealing with unexpected features or with exceptions in few subjects. This section describes some of the issues that we encountered.

Due to CTF hardware problems, some subjects' task MEG data was not recorded in a single CTF dataset, but in two datasets. We dealt with this by copying them explicitly (not in the for-loop) in step 3.

Due to misconfiguration of the Bitsi box ("level mode"), some subjects' task MEG data have the trigger codes represented incorrectly. The consequence is that the individual bits of the triggers overlap in time, causing the default trigger detection to fail. This is dealt with in step 6 by using the mous_read_event_audio function from the MOUS github repository.

In some of the MEG recordings the default settings for event detection from the digital trigger channel resulted in a limited number of events being undetected, causing occasional failure of the alignment procedure between shared events. This was mostly caused by 2 events being too closely spaced in time, either or not in combination with a too wide trigger pulse, resulting in "staircase-shaped" pulses. In case of such a mismatch between the number of trigger-channel-extracted events versus Presentation-log-file-extracted events, we defined another shared event for alignment. This is dealt with in step 6.

The Presentation log files for the visual stimuli had an \<enter\> after the period \<.\> at the end of each sentence. This caused the line in the log file to be broken in two, resulting in incorrect parsing of the log file in step 6. We dealt this by removing the \<enter\> in the log files prior to step 6, i.e. in step 4.

## References

- Schoffelen JM, Oostenveld R, Lam NHL, Uddén J, Hultén A & Hagoort P. [A 204-subject multimodal neuroimaging dataset to study language processing](https://doi.org/10.1038/s41597-019-0020-y) Scientific Data 2019 Apr 3;6(17). doi: 10.1038/s41597-019-0020-y.

- Schoffelen JM, Hultén A, Lam N, Marquand AF, Uddén J, Hagoort P. [Frequency-specific directed interactions in the human brain network for language.](https://doi.org/10.1073/pnas.1703155114) Proc Natl Acad Sci U S A. 2017 Jul 25;114(30):8083-8088. doi: 10.1073/pnas.1703155114.

- Lam NHL, Schoffelen JM, Uddén J, Hultén A, Hagoort P. [Neural activity during sentence processing as reflected in theta, alpha, beta, and gamma oscillations.](https://doi.org/10.1016/j.neuroimage.2016.03.007) Neuroimage. 2016 Nov 15;142:43-54. doi: 10.1016/j.neuroimage.2016.03.007.

- Lam NHL, Hultén A, Hagoort P & Schoffelen JM. [Robust neuronal oscillatory entrainment to speech displays individual variation in lateralisation](https://doi.org/10.1080/23273798.2018.1437456) Language, Cognition and Neuroscience, 33:8, 943-954. doi: 10.1080/23273798.2018.1437456.
