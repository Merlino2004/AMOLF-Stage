import sys
sys.path.append("..")

import numpy as np
from reading import ReadingData
from plotting import Plotting

loops = 50 # Setting loop count

# Reading etch time data 
file_name = 'ParameterDataEtchTime'
df = ReadingData(file_name,printing='no')

# Calling class for etch time
obj = Plotting(file_name,df['Selectivity'],df['SidewallAngle'],df['Undercut'],
            df['Scallops'],df['MicromaskingLength'], loops, time=df['EtchTime'], depth=df['EtchDepth'])

# Plotting etch time plots and calculating etch quality
obj.PlotRelations(obj.time,obj.micromaskingratio,obj.error_time,obj.error_micromaskingratio,
                  'EtchTime $t$ [min]','MicromaskingRatio $M/d$ [-]')
obj.PlotRelations(obj.time,df['EtchDepth'],obj.error_time,obj.error_length,
                  'EtchTime $t$ [min]','EtchDepth $D$ [\u03BCm]')
obj.PlotRelations(obj.time,df['Selectivity'],obj.error_time,obj.error_selectivity,
                  'EtchTime $t$ [min]','Selectivity $S$ [-]')
obj.CalculateEtchQuality(printing='yes')

# Reading C4F8 gasflow data
file_name = 'ParameterDataC4F8'
df = ReadingData('ParameterDataC4F8',printing='no')

# Calling class for C4F8 gasflow
obj = Plotting(file_name,df['Selectivity'],df['SidewallAngle'],df['Undercut'],
            df['Scallops'],df['MicromaskingLength'], loops, gasflow=df['C4F8gasflow'])

# Plotting for C4F8 gasflow and calculating etch quality
obj.PlotRelations(df['C4F8gasflow'],df['SidewallAngle'],obj.error_gasflow,obj.error_angle,
                  'C4F8gasflow $Q$ [sccm]','SidewallAngle $\u03B8$ [\u00b0]')
obj.CalculateEtchQuality(printing='yes')

# Reading table power data
file_name = 'ParameterDataTablePower'
df = ReadingData(file_name,printing='no')

# Calling class for table power
obj = Plotting(file_name,df['Selectivity'],df['SidewallAngle'],df['Undercut'],
            df['Scallops'],df['MicromaskingLength'], loops, power=df['TablePower'],voltage=df['Voltage'])

# Plotting for table power and calculating etch quality
obj.PlotRelations(df['TablePower'],df['SidewallAngle'],obj.error_power,obj.error_angle,
                  'TablePower $P$ [W]','SidewallAngle $\u03B8$ [\u00b0]')
obj.PlotRelations(df['TablePower'],df['Voltage'],obj.error_power,obj.error_voltage,
                  'TablePower $P$ [W]','Voltage $U$ [V]')
obj.CalculateEtchQuality(printing='yes')

# Reading break time data
file_name = 'ParameterDataBreakTime'
df = ReadingData(file_name,printing='no')

# Calling class and plotting for break time and calculating etch quality
obj = Plotting(file_name,df['Selectivity'],df['SidewallAngle'],df['Undercut'],
            df['Scallops'],df['MicromaskingLength'], loops, time=df['BreakTime'])
obj.PlotRelations(obj.time,df['SidewallAngle'],obj.error_time,obj.error_angle,
                  'BreakTime $t$ [min]','SidewallAngle $\u03B8$ [\u00b0]')
obj.CalculateEtchQuality(printing='yes')

# Reading table power data
file_name = 'ParameterDataPressure'
df = ReadingData(file_name,printing='no')

# Calling class for table power
obj = Plotting(file_name,df['Selectivity'],df['SidewallAngle'],df['Undercut'],
            df['Scallops'],df['MicromaskingLength'], loops, pressure=df['Pressure'],voltage=df['Voltage'])

# Plotting for table power and calculating etch quality
obj.PlotRelations(df['Pressure'],df['Undercut'],obj.error_pressure,obj.error_length,
                  'Pressure $p$ [mTorr]','Undercut $u$ [\u03BCm]')
obj.PlotRelations(df['Pressure'],df['Voltage'],obj.error_pressure,obj.error_voltage,
                  'Pressure $p$ [mTorr]','Voltage $U$ [V]')
obj.CalculateEtchQuality(printing='yes')

# Reading table power data
file_name = 'ParameterDataICPpower'
df = ReadingData(file_name,printing='no')

# Calling class for table power
obj = Plotting(file_name,df['Selectivity'],df['SidewallAngle'],df['Undercut'],
            df['Scallops'],df['MicromaskingLength'], loops)

# Calculating etch quality
obj.CalculateEtchQuality(printing='yes')