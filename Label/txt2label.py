## converting txt to labels
# Run this file in the directory of txt files
import os
import glob
import pandas as pd
import numpy as np

#labels = np.ndarray
FN = pd.DataFrame()
labels = pd.DataFrame()

list_of_files = glob.glob('./*.txt')

for fileName in list_of_files:
    fin = open( fileName, "r" )
    data_list = fin.readlines()
    fin.close() # closes file
  
    FN = FN.append({'FN':fileName}, ignore_index = True)
    labels = labels.append({'Remarks':data_list}, ignore_index = True)
    #creating 2 df for file name and remarks

LB = pd.concat([FN, labels], axis=1)
#outer joins the 2 df
LB1 = LB.sort_values("FN", axis = 0)
#sort by file name

#TO_DO, converting to binary labels

print (LB1.to_string())
