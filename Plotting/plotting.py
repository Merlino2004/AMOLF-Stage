import sys
sys.path.append("..")

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

class Plotting:
    def __init__(self,selectivity, angle, undercut, scallops, micromasking, loops,
                 pressure=None, power=None, voltage=None, time=None, depth=None, gasflow=None):
        
        # Adress parameters of etch to class
        self.selectivity = selectivity #um
        self.angle = angle # \degree
        self.undercut = undercut # um
        self.scallops = scallops # um
        self.micromasking = micromasking #um
        self.loops = loops

        # Calculate parameters and adress if needed
        self.micromaskingratio = []
        if depth is not None:
            for i in range(len(depth)):
                self.micromaskingratio.append(self.micromasking[i]/depth[i])
        else: 
            None

        self.time = time*self.loops/60 if time is not None else None # min, all times entered

        # Determining uncertainties
        self.error_selectivity = 2 # - 
        self.error_angle = 2 # \degree
        self.error_length = 0.1 # um, all lengths measured
        self.error_micromaskingratio = 0.05 # -

        self.error_pressure = 0.0005*pressure if pressure is not None else None # mTorr
        self.error_power = 0.015*power if power is not None else None # W
        self.error_voltage = 0.01*voltage if voltage is not None else None # V
        self.error_time = 0.03*loops/60 if time is not None else None # min
        self.error_gasflow = 0.005*gasflow if gasflow is not None else None # sccm

    def PlotEtchQuality(self):
        self.angle = a

    def PlotRelations(self,x,y,error_x,error_y,xlabel,ylabel):
        plt.errorbar(x,y,xerr=error_x,
                    yerr=error_y, label=f'{self.loops} bosch loops', fmt='o')

        plt.grid()
        plt.legend()
        plt.xlabel(f'{xlabel}')
        plt.ylabel(f'{ylabel}')

        plt.savefig(f'plots/{ylabel.split()[0]}Over{xlabel.split()[0]}_{self.loops}Loops.pdf')
        plt.show()