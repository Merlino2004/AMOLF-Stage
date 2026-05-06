import sys
sys.path.append("..")

import os
import numpy as np

replacefile = True
path = 'file_path'
new_file = 'file_path'

if replacefile == True:
    os.remove(path)
    os.rename(new_file,path)


# All parameters in the csv file
meetdata = np.genfromtxt(path, delimiter=',', encoding='utf-8-sig')
meetdata = meetdata[~np.isnan(meetdata).any(axis=1)] # Remove NaN values

t = meetdata[:,0]
Table_RF_Forward = meetdata[:,5]
Table_RF_Reflected = meetdata[:,6]
ICP_RF_Forward = meetdata[:,7]
ICP_RF_Reflected = meetdata[:,8]

ICP_Percentage = []
Table_Percentage = []
for i in range(len(ICP_RF_Forward)):
    if ICP_RF_Forward[i] != 0:
        ICP_Percentage.append(ICP_RF_Reflected[i]/ICP_RF_Forward[i]*100)
        
    if Table_RF_Forward[i] != 0:
        Table_Percentage.append(Table_RF_Reflected[i]/Table_RF_Forward[i]*100)

# Elemenate values beneath 15 seconds
for i in range(len(t)):
    if t[i] - 15 >= 0:
         a = i
         break

Table_RF_Forward = meetdata[a:]
Table_RF_Reflected = meetdata[a:]
ICP_RF_Forward = meetdata[a:]
ICP_RF_Reflected = meetdata[a:]

Table_max = np.max(Table_Percentage)
Table_av = np.mean(Table_Percentage)
ICP_max = np.max(ICP_Percentage)
ICP_av = np.mean(ICP_Percentage)

dataset = [ICP_av,ICP_max,Table_av,Table_max] # Convert arrays into one array
dataset = ",".join(map(str, dataset)) # Convert to string with delimiter

# Documenting in file
with open('ProcessFiles/ProcessFileStabilization.csv','a') as csvfile:
    csvfile.write(dataset + '\n')