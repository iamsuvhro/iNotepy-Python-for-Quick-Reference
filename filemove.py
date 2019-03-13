# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 21:02:05 2019

@author: HP
"""

import shutil
import os
from tqdm import tqdm

#file path
source = "C:\\Users\\HP\\Desktop\\cell_images\Parasitized"
#destination path
dest1 = "C:\\Users\\HP\\Desktop\\cell_images\\Parasitized_Test"

import math
files = os.listdir(source)

split = 0.70
mark = math.floor(split * len(files))

for f in tqdm(files[mark:]):
        shutil.move(source+"\\"+f, dest1)