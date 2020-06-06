import pandas as pd

file = open("registro_de_ejercicios.txt")
lines = file.readlines()
processedList = []
for i, line in enumerate(lines):
    try:
        line = line.split(",")
        temp = [line[0],line[1],line[2],line[3],line[4],line[5]]
        processedList.append(temp)
    except:
        print("Error en la línea: ", i)
columns = ["ejercicio","x1","y1","z1","x2","y2"]

data = pd.DataFrame(data = processedList,columns = columns)
print(data.head())

print(data.shape)
print(data.info())
print(data.isnull().sum())
print(data["ejercicio"].value_counts())
#print(processedList)