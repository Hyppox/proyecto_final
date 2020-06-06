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

print(data.isnull().sum())
print(data["ejercicio"].value_counts())

data["x1"] = data["x1"].astype("float")
data["y1"] = data["y1"].astype("float")
data["z1"] = data["z1"].astype("float")
data["x2"] = data["x2"].astype("float")
data["y2"] = data["y2"].astype("float")
print(data.info())
Fs = 10
#print(processedList)