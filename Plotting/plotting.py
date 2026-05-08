import sys
sys.path.append("..")

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

class Plotting:
    def __init__(self,file_name, selectivity, angle, undercut, scallops, micromasking, loops,
                 pressure=None, power=None, voltage=None, time=None, depth=None, gasflow=None):
        
        # Adress file name to class
        self.file_name = file_name

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
        self.error_angle = 1 # \degree
        self.error_length = 0.08 # um, all lengths measured
        self.error_micromaskingratio = 0.05 # -

        self.error_pressure = 0.0005*pressure if pressure is not None else None # mTorr
        self.error_power = 0.015*power if power is not None else None # W
        self.error_voltage = 0.01*voltage if voltage is not None else None # V
        self.error_time = 0.03*loops/60 if time is not None else None # min
        self.error_gasflow = 0.01*gasflow if gasflow is not None else None # sccm

    def CalculateEtchQuality(self,printing='no'):
        # Determine tolerence values
        tolerence_angle = 3 # degree
        tolerence_scallops = 0.5 # um
        tolerence_micromasking = 1 # um

        # Determine model values
        model_angle = 90 # degree
        model_scallops = 0 # um
        model_micromasking = 0 # um

        # Determine weight values
        weight_angle = 1 # -
        weight_scallops = 1 # -
        weight_micromasking = 1 # -

        # Create arrays for error rate of etch quality for storage, all parameters have the same length
        sigma = np.zeros(len(self.angle))
        sigma_angle = np.zeros(len(self.angle))
        sigma_scallops = np.zeros(len(self.scallops))
        sigma_micromasking = np.zeros(len(self.micromasking))

        # Calculate difference in parameters
        for i in range(len(self.angle)): # All parameters have the same length
            # Calculate difference between model and measurement per parameter
            difference_angle = np.abs(model_angle-self.angle[i])
            difference_scallops = np.abs(model_scallops-self.scallops[i])
            difference_micromasking = np.abs(model_micromasking-self.micromasking[i])

            # Calculate and store each sigma component
            sigma_angle[i] = (difference_angle/(tolerence_angle+difference_angle))
            sigma_scallops[i] = (difference_scallops/(tolerence_scallops+difference_scallops))
            sigma_micromasking[i] = (difference_micromasking/(tolerence_micromasking+difference_micromasking))

            # Calculate error rate of etch quality
            sigma[i] = np.sqrt(weight_angle*sigma_angle[i]**2+weight_scallops*sigma_scallops[i]**2+
                               weight_micromasking*sigma_micromasking[i]**2)
            
        # Printing error rates if needed
        if printing == 'yes':
            print(f'File name: {self.file_name} \n',
                  f'Sigma values per sum: \n',
                  f'Sigma_angle: {sigma_angle} \n',
                  f'Sigma_scallops: {sigma_scallops} \n',
                  f'Sigma_micromasking: {sigma_micromasking} \n',
                  f'Error rates of etch qualities: {sigma} \n')
            
        return sigma

    def PlotRelations(self,x,y,error_x,error_y,xlabel,ylabel):
        plt.errorbar(x,y,xerr=error_x,
                    yerr=error_y, label=f'{self.loops} bosch loops', fmt='o')

        plt.grid()
        plt.legend()
        plt.xlabel(f'{xlabel}')
        plt.ylabel(f'{ylabel}')

        plt.savefig(f'plots/{ylabel.split()[0]}Over{xlabel.split()[0]}_{self.loops}Loops.pdf')
        plt.show()