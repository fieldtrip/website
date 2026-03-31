#!/usr/bin/env python3
#
# This script updates the citations to the FieldTrip reference paper. It downloads new 
# citations from Pubmed and saves their details in YAML files. It can be used to keep 
# the list of citations on the website up to date.
#
# Installation:
#   conda create -n website python==3.10
#   conda activate website
#   pip install requests pyyaml
#
# Use as:
#   python _scripts/update-citations.py

import os
import json
import yaml # this corresponds to PyYAML
import time
import requests
from itertools import compress

# The FieldTrip reference paper has the following identifiers
# PMID  = 21253357
# PMCID = PMC3021840
# DOI   = 10.1155/2011/156869

# download the list of papers by which it is cited
url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&linkname=pubmed_pmc_refs&retmode=json&id=21253357"
r = requests.get(url)
d = json.loads(r.text)

# the list that it returns does not contain PMIDs but rather PMCIDs
citedby = d['linksets'][0]['linksetdbs'][0]['links']

# only keep the IDs that do not have a file
keep = []
for pmcid in citedby:
    filename = '_data/citedby/' + pmcid + '.yml'
    keep.append(not os.path.isfile(filename))
remaining = list(compress(citedby, keep))

while len(remaining):
    
    # go through the list in small batches
    if len(remaining)>10:
        subset = remaining[0:10]
        remaining = remaining[11:]
    else:
        subset = remaining
        remaining = []
    
    if len(subset):
        time.sleep(1)

        # download the publication details
        url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pmc&retmode=json&id=' + ','.join(subset)
        r = requests.get(url)
        d = json.loads(r.text)
        
        for pmcid in d['result']['uids']:
            print(pmcid)
            publication = d['result'][pmcid]
            filename = '_data/citedby/' + pmcid + '.yml'
            f = open(filename, "w")
            n = f.write(yaml.dump(publication, allow_unicode=True))
            f.close()
