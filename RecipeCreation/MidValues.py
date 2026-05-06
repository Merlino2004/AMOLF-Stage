import numpy as np

def MidValues(Table_AMU_C1, Table_AMU_C2, ICP_AMU_C1, ICP_AMU_C2,run_count):

    # Needed arrays
    parameters = [Table_AMU_C1, Table_AMU_C2, ICP_AMU_C1, ICP_AMU_C2]
    processed_params = []

    for param in parameters:
        val0 = param[0] # Find the first value of each array
        val_last = param[-1] # Find the last value of each array

        # Filter the same values at the beginning of the array
        if np.all(param == val0): 
            processed_params.append(np.array([]))
            continue

        start_idx = np.argmax(param != val0)
        trimmed = param[start_idx:]

        # Filter the same values at the beginning of the end
        end_idx = np.argmax(trimmed[::-1] != val_last)
        final = trimmed[:len(trimmed) - end_idx]

        processed_params.append(final)

    # New value is mean of values
    means = np.zeros(len(parameters))
    MD = np.zeros(len(parameters))
    for i in range(len(means)):
        means[i] = np.mean(processed_params[i]) # Mean values
        MD[i] = np.mean(np.abs(processed_params[i]-means[i])) # Mean deviation 

    print('new_ICP_C1: ',means[0], 'new_ICP_C2: ',means[1], 'new_table_C1: ',means[2], 'new_table_C2: ',means[3])
    return means[0], means[1], means[2], means[3], MD