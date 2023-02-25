#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 08:33:05 2023

@author: marik
"""

import glob
import re
import os


def zpracuj(odstavec):
    kopie = odstavec
    odstavec = re.sub(">  *Definice \((.*?)\)\.",r"```{prf:definition} \1.\n:nonumber:\n",odstavec)
    odstavec = re.sub(">  *Důsledek \((.*?)\)\.",r"```{prf:corollary} \1.\n:nonumber:\n",odstavec)
    odstavec = re.sub(">  *Věta \((.*?)\)\.",r"```{prf:theorem} \1.\n:nonumber:\n",odstavec)
    odstavec = re.sub(">  *Poznámka \((.*?)\)\.",r"```{prf:remark} \1.\n:nonumber:\n",odstavec)
    if kopie != odstavec:
        odstavec = re.sub(">  *","",odstavec)
        odstavec = odstavec + "\n```\n"
    return odstavec


files = glob.glob('../*/*md')

for file in files:
    print(file)
    f = open(file, 'r')
    obsah_souboru = f.read()    
    f.close()
    odstavce = obsah_souboru.split("\n\n")
    vystup = []
    for odstavec in odstavce:
        x = re.search("^>", odstavec)
        if x is None:
            vystup = vystup + [odstavec+"\n"]
        else:
            vystup = vystup + [zpracuj(odstavec)+"\n"]
    f = open(file+"_", 'w')
    f.write("\n".join(vystup))
    f.close()            
    os.remove(file)
    os.rename(file+"_",file)

            