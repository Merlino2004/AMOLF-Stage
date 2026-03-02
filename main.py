import sys
sys.path.append("..")

from MidValues import MidValues
from ChangeRecipe import ChangeRecipe
from QuickPlot import plottingAMU

import os
import numpy as np

replacefile = True
path = '../logs/c1c2.csv'
new_file = '../logs/c1c2(1).csv'

if replacefile == True:
    os.remove(path)
    os.rename(new_file,path)

with open("RunCounter.txt") as f:
    run_count = int(f.read())+ 1

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

plottingAMU(t,Table_AMU_C1, Table_AMU_C2, ICP_AMU_C1, ICP_AMU_C2, Table_RF_Forward, Table_RF_Reflected, ICP_RF_Forward, ICP_RF_Reflected, run_count)

new_icp_c1, new_icp_c2, new_table_c1, new_table_c2 = MidValues(Table_AMU_C1, Table_AMU_C2, ICP_AMU_C1, ICP_AMU_C2)

changer = ChangeRecipe(
    path_old_recipe="../recipes/StabalizePlasma.processrecipe",
    path_new_recipe="../recipes/StabalizePlasma.processrecipe",
    new_icp_c1=new_icp_c1,
    new_icp_c2=new_icp_c2,
    new_table_c1=new_table_c1,
    new_table_c2=new_table_c2
)

changer.ChangePreProcess()
#changer.ChangeBoschLoop()
changer.save()

with open("RunCounter.txt", 'w') as f:
        f.write(f"{run_count}")