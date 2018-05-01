#!/usr/bin/env python
# -*- coding: utf-8 -*-
#grep_headers.py
#04/2018


__author__ = 'Igor Rodrigues da Costa'
__contact__ = 'igor.bioinfo@gmail.com'

import os
from subprocess import Popen

def get_species():
    species_folder = '/home/igor/ancestral/species/'
    files = os.listdir(species_folder)
    species = {}
    for f in files:
        if not f.endswith('.txt'):
            continue
        with open(species_folder + f, 'r') as sp_file:
            reino = f.split('_')[0] #eucarioto, bacteria, archea
            species[reino] = []
            for l in sp_file:
                species[reino].append(l.strip())
    return species

def run_grep(species, header_file = '/home/igor/ancestral/L3_headers2'):
    found = []
    with open(header_file, 'r') as header_f:
        for l in header_f:
            sp = l.split('[')[-1].split(']')[0] 
            if sp in species:
                print sp 
                found.append(l.strip())
    return '\n'.join(found)

def main():
    '''this should get the species, order by kingdom, then search headers of this species in
     the header file, assuring there is one seq for sp. Find the sequence in the refprot file, concatenate and align.'''
    species = get_species()
    for k in species:
        with open(k+'_headers2', 'w') as k_header: #headers of each kingdom
            headers = run_grep(species[k])
            k_header.write(headers)
main()
