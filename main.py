import csv
import pandas

#Gets the CSV file via Pandas and detects the header of the columns
col_list = ["No.", 'PosX', "PosY", "PosZ", "Rx", "Ry", "Rz", "DWNx", "DWNy", "DWNz", "Lx", "Ly", "Lz"]
allCols = pandas.read_csv("rmc.csv", usecols = col_list)

#Each variable is assigned to the corresponding column list
number = allCols["No."]
posx = allCols["PosX"]
posy =  allCols["PosY"]
posz = allCols["PosZ"]
rx = allCols["Rx"]
ry = allCols["Ry"]
rz = allCols["Rz"]
dwnx = allCols["DWNx"]
dwny = allCols["DWNy"]
dwnz = allCols["DWNz"]
lx = allCols["Lx"]
ly = allCols["Ly"]
lz = allCols["Lz"]
groupSize = 37

def grouping(size, lisx, lisy, lisz):
    a = []
    b = []
    c = []
    group = []
    k = 0
    while(k < size):
        a.append(lisx[k])
        b.append(lisy[k])
        c.append(lisz[k])
        k+=1
        
    group.append(a)
    group.append(b)
    group.append(c)
    return group

groups = int((len(number)//groupSize) + 1)
print("pos" + str(grouping(groupSize, posx, posy, posz)))
print("RIGHT" + str(grouping(groupSize, rx, ry, rz)))
print("DOWN" + str(grouping(groupSize, dwnx, dwny, dwnz)))
print("LEFT" + str(grouping(groupSize, lx, ly, lz)))