import sys
sys.path.append("..")

from MidValues import MidValues
from ChangeRecipe import ChangeRecipe
from QuickPlot import plottingAMU, AMUconverge

import os
import shutil
import numpy as np

replacefile = False # Set to True if you exported a new log file 
rawprocessfile = False # Set to True of you need a new process log file
path = 'file_path'
new_file = 'file_path'

if replacefile == True:
    os.remove(path)
    os.rename(new_file,path)

if rawprocessfile == True:
     os.remove('ProcessFiles/ProcessFile.csv')
     shutil.copy('ProcessFiles/Raw/ProcessFileRaw.csv','ProcessFiles/ProcessFile.csv')

# All parameters in the csv file
meetdata = np.genfromtxt(path, delimiter=',', encoding='utf-8-sig')
meetdata = meetdata[~np.isnan(meetdata).any(axis=1)] # Remove NaN values

t = meetdata[:,0]
Table_AMU_C1 = meetdata[:,1]
Table_AMU_C2 = meetdata[:,2]
ICP_AMU_C1 = meetdata[:,3]
ICP_AMU_C2 = meetdata[:,4]
Table_RF_Forward = meetdata[:,5]
Table_RF_Reflected = meetdata[:,6]
ICP_RF_Forward = meetdata[:,7]
ICP_RF_Reflected = meetdata[:,8]

# Elemenate values beneath 15 seconds
for i in range(len(t)):
    if t[i] - 15 >= 0:
         a = i
         break

t = t[a:]
Table_AMU_C1 = Table_AMU_C1[a:]
Table_AMU_C2 = Table_AMU_C2[a:]
ICP_AMU_C1 = ICP_AMU_C1[a:]
ICP_AMU_C2 = ICP_AMU_C2[a:]
Table_RF_Forward = Table_RF_Forward[a:]
Table_RF_Reflected = Table_RF_Reflected[a:]
ICP_RF_Forward = ICP_RF_Forward[a:]
ICP_RF_Reflected = ICP_RF_Reflected[a:]

ICP_Percentage = []
Table_Percentage = []
for i in range(len(ICP_RF_Forward)):
    if ICP_RF_Forward[i] != 0:
        ICP_Percentage.append(ICP_RF_Reflected[i]/ICP_RF_Forward[i]*100)
        
    if Table_RF_Forward[i] != 0:
        Table_Percentage.append(Table_RF_Reflected[i]/Table_RF_Forward[i]*100)
        
Table_max = np.max(Table_Percentage)
Table_av = np.mean(Table_Percentage)
ICP_max = np.max(ICP_Percentage)
ICP_av = np.mean(ICP_Percentage)

meetdata = np.genfromtxt('ProcessFiles/ProcessFile.csv', delimiter=',', encoding='utf-8-sig')
iterations = meetdata[:,0]
mean_icp_c1 = meetdata[:,1]
mean_icp_c2 = meetdata[:,2]
mean_tables_c1 = meetdata[:,3]
mean_tables_c2 = meetdata[:,4]
md_icp_c1 = meetdata[:,5]
md_icp_c2 = meetdata[:,6]
md_tables_c1 = meetdata[:,7]
md_tables_c2 = meetdata[:,8]

last_run = iterations[-1] # Last iteration is last run

plottingAMU(t, Table_AMU_C1, Table_AMU_C2, ICP_AMU_C1, ICP_AMU_C2, Table_max, Table_av, ICP_max, ICP_av,last_run)

new_icp_c1, new_icp_c2, new_table_c1, new_table_c2, MD = MidValues(Table_AMU_C1, Table_AMU_C2, ICP_AMU_C1, ICP_AMU_C2,last_run)

dataset = [last_run+1,new_icp_c1, new_icp_c2, new_table_c1, new_table_c2,*MD,ICP_av,Table_av] # Convert arrays into one array
dataset = ",".join(map(str, dataset)) # Convert to string

# Documenting in file
#with open('ProcessFiles/ProcessFile.csv','a') as csvfile:
#    csvfile.write(dataset + '\n')

changer = ChangeRecipe(
    path_old_recipe="file_path",
    path_new_recipe="file_path",
    new_icp_c1=new_icp_c1,
    new_icp_c2=new_icp_c2,
    new_table_c1=new_table_c1,
    new_table_c2=new_table_c2
)

#changer.ChangePreProcess()
#changer.ChangeBoschLoop()
#changer.save()

#if last_run+1 == 18:
#    AMUconverge(iterations,md_tables_c1,md_tables_c2,md_icp_c1,md_icp_c2,mean_icp_c1, mean_icp_c2, mean_tables_c1, mean_tables_c2)