import sys
sys.path.append("..")

import numpy as np
import re
import pandas as pd 

def ReadingData(csv_name,printing='no'):
        # Reading all parameters from csv file and adressing them to their own variable
        with open(f'data/{csv_name}.csv','r', encoding='utf-8-sig') as f:
                header = f.readline().strip() # Strip first row from the whole file array
                header = header.replace('"','') # Replace doctring with normal string
                header = re.sub(r'#\w+', '', header).strip() # Filter unit
                header = [h.strip() for h in header.split(',')] # split header array from the comma
                data = np.genfromtxt(f, delimiter=',') # Rest of file values

                df = pd.DataFrame(data,columns=header)
                if printing == 'yes':
                        print(df)
        return df