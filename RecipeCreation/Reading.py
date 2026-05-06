from QuickPlot import plottingAMU, AMUconverge, PlotReflected, PercentageOverMD
import os
import shutil
import numpy as np

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
reflected_icp = meetdata[:,9]
reflected_table = meetdata[:,10]

AMUconverge(iterations,md_tables_c1,md_tables_c2,md_icp_c1,md_icp_c2,mean_icp_c1, mean_icp_c2, mean_tables_c1, mean_tables_c2)
PlotReflected(iterations,reflected_table,reflected_icp)
#PercentageOverMD(reflected_table,reflected_icp,md_tables_c1,md_tables_c2,md_icp_c1,md_icp_c2)