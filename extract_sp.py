import os
from random import sample

def ensembl():
    os.chdir('C://Users/igor.costa/Desktop/')
    print(os.listdir())
    sp_list = []
    with open('species.txt', 'r') as sp_file:
        for line in sp_file:
            sp = line.split()[1]
            sp = sp.replace('"','')
            sp = ' '.join(sp.split('_')[:2])
            sp_list.append(sp)
            print(line.split()[1])
    print(len(set(sp_list)))

def eggnog():
    #os.chdir(C://Users/igor.costa/Desktop/)
    sp_list = []
    n=0
    with open('eggnog4.core_species_list.txt', 'r') as sp_file: #http://eggnogdb.embl.de/download/eggnog_4.5/
        for line in sp_file:
            sp = line.split(t)
            #if sp[4].strip() != not available:
##            if sp[3].strip() == Ensembl: #(56)
##                print(sp)
##                n += 1
##            if sp[3].strip() == Ensembl Fungi: #(28)
##                print(sp)
##                n += 1
##            if sp[3].strip() == Ensembl Plants: #(22)
##                print(sp)
##                n += 1
            source = sp[3].strip()
            if source == 'Ensembl' or source == 'Ensembl Fungi' or source == 'Ensembl Plants':
                sp_list.append(sp[0]) #106
    with open('eggnog_106species.txt', 'w') as outfile:
        for sp in sp_list:
            outfile.write(sp + n)

def archea():
    #ftp://ftp.ncbi.nih.gov/pub/COG/COG2014/static/lists/homeCOGs.html
    #os.chdir(C://Users/igor.costa/Desktop/)
    with open('archea', 'r') as sp_file, open('archea_list.txt','w') as outfile:
        for line in sp_file:
            sp = ' '.join(line.split()[1:])
            #sp = sp.replace(','')
            #sp = ' '.join(sp.split('_')[:2])
            outfile.write(sp + '\n')


def bacteria():
    #ftp://ftp.ncbi.nih.gov/pub/COG/COG2014/static/lists/homeCOGs.html
    #os.chdir('C://Users/igor.costa/Desktop/')
    orgs = {}
    with open('bacteria', 'r') as sp_file, open('bacteria_list.txt','w') as outfile:
        for line in sp_file:
            if len(line.split()) <3:
                family = line.split()[0]
                orgs[family] = []
            else:
                sp = ' '.join(line.split()[1:])
                orgs[family].append(sp)
        for k in orgs.keys():
            if len(orgs[k]) < 5:
                for sp in orgs[k]:
                    outfile.write(sp + '\n')
            else:
                sp_list = sample(orgs[k], 4)
                for sp in sp_list:
                    outfile.write(sp + '\n')
#ensembl()
#eggnog()
#archea()
bacteria()

