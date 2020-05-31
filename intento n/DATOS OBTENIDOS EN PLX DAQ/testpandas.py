import pandas as pd 
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("./DATOS OBTENIDOS EN PLX DAQ/PRUEBA 1  RADIAL DEVIATION.csv") 
# Preview the first 5 lines of the loaded data 
data.head()
print(data)