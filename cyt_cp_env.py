# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 16:13:24 2021

@author: aaa
"""


import os

path = "C:/hangul-syllable-recognition-main/data/train_data.csv"

save_path="C:/hangul-syllable-recognition-main/data/ss.txt"

while True:
    
    with open(path, 'r',encoding='UTF8') as fin:
        data = fin.read().splitlines(True)
    with open(save_path, 'w',encoding='UTF8') as fout:
        fout.writelines(data[:15001])
        
    if not data: 
        break

fin.close()
fout.close()