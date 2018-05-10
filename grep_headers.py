#!/usr/bin/env python
# -*- coding: utf-8 -*-
#grep_headers.py
#04/2018

'''grep_species -s species_folder -i headers_file -r refprot_folder
this program finds all sequences of a given protein in refseq for all species in a list 
'''
__author__ = 'Igor Rodrigues da Costa'
__contact__ = 'igor.bioinfo@gmail.com'

import os
import argparse
from subprocess import Popen

def argument_parser(hlp = False):
    '''grep_headers.py'''

    parser = argparse.ArgumentParser(description = 'grep_headers.py',\
                                     argument_default = None, fromfile_prefix_chars = '@')
    parser.add_argument('-s', '--species', nargs = '?', type = str, required = True,\
                        dest = 'species', help = 'Path to the species folder.')
    parser.add_argument('-i', '--headers', nargs = '?', type = str, required = True,\
                        dest = 'headers', help = 'Path to the headers file.')
    parser.add_argument('-r', '--refprot', nargs = '?', type = str, required = True,\
                        dest = 'refprot', help = 'Path to the refprot folder.')
    parser.add_argument('-o', '--outpath', nargs = '?', type = str, default = os.getcwd(),\
                        dest = 'outpath', help = 'Path where the aligned results will be saved. (default: %(default)s)')
    if hlp:
        args = parser.parse_args(['-h'])
    else:
        args = parser.parse_args().__dict__
    return args

def get_species(species_folder = '/home/igor/ancestral/species/'):
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

def main(args):
    '''this should get the species, order by kingdom, then search headers of this species in
     the header file, assuring there is one seq for sp. Find the sequence in the refprot file, concatenate and align.'''
    species = get_species(args['species'])
    for k in species:
        with open(k+'_headers2', 'w') as k_header: #headers of each kingdom
            headers = run_grep(args['headers'], species[k])
            k_header.write(headers)

if __name__ == '__main__':
    args = argument_parser()
    main(args)   
