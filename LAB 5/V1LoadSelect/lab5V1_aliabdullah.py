import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
# Description:
# This program performs precession analysis on astronomical data obtained from the 'horizons_results' file.
# It includes functions for loading data, processing coordinates, selecting relevant data, and generating plots.
def main():
    data = loaddata('horizons_results')
    data = locate(data) # Perihelia
    data = select(data,25,('Jan','Feb','Mar'))
    makeplot(data,'horizons_results')
def loaddata(filename):
    #    Purpose: Load data from a text file and convert it into a list of dictionaries.
    #    Arguments: filename (str) - the name of the file to be loaded.
    #    Side Effects: Prints progress information to the console.
    #                  Reports if the $$SOE line is missing in the input file.
    #    Returns: List of dictionaries containing astronomical data.
    file = open(filename+'.txt','r')
    lines = file.readlines()
    file.close()
    noSOE = True
    num = 0
    data = []
    for line in lines:
        if noSOE:
            if line.rstrip() == "$$SOE":
                noSOE = False
        elif line.rstrip() != "$$EOE":
            num = num+1
            if num % 10000 == 0:
                print(filename,":",num,"line(s)")
            datum = str2dict(line)
            data.append(datum)
        else:
            break # for
    if noSOE:
        print(filename,": no $$SOE line")
    else:
        print(filename,":",num,"line(s)")
    return data
def str2dict(line):
    #    Purpose: Convert a string representing astronomical data into a dictionary.
    #    Arguments: line (str) - a line of text containing comma-separated values.
    #    Returns: Dictionary with keys 'numdate', 'strdate', and 'coord'.
    values = line.split(',')
    numdate = float(values[0].strip())
    # Remove 'A.D.' and '00:00:00.0000' from strdate
    strdate = values[1].replace('A.D. ', '').replace('00:00:00.0000', '').strip()
    x = float(values[2].strip())
    y = float(values[3].strip())
    z = float(values[4].strip())
    coord = (x, y, z)
    return {'numdate': numdate, 'strdate': strdate, 'coord': coord}
def locate(data1):
    #    Purpose: Identify and return perihelion data points based on vector lengths.
    #    Arguments: data1 (list of dictionaries) - astronomical data.
    #    Returns: List of dictionaries representing perihelion data.
    dist = [] # Vector lengths
    for datum in data1:
        coord = np.array(datum['coord'])
        dot = np.dot(coord,coord)
        dist.append(np.sqrt(dot))
    data2 = []
    for k in range(1,len(dist)-1):
        if dist[k] < dist[k-1] and dist[k] < dist[k+1]:
            data2.append(data1[k])
    return data2
def select(data,ystep,month):
    #    Purpose: Select data based on the year step and specified months.
    #    Arguments: data (list of dictionaries) - astronomical data.
    #               ystep (int) - year step for selection.
    #               month (tuple of str) - months to include in the selection.
    #    Returns: List of dictionaries containing selected data.
    data3 = []
    for i in data:
        date=i['strdate'].split('-')
        if int(date[0])%ystep == 0 and date[1] in month:
            data3.append(i)
    return data3

def makeplot(data,filename):
    (numdate,strdate,arcsec) = precess(data)
    plt.xlabel('Perihelion date')
    plt.ylabel('Precession (arcsec)')
    plt.plot(numdate,arcsec,'bo')
    plt.xticks(numdate,strdate,rotation=45)
    add2plot(numdate,arcsec)
    plt.savefig(filename+'.png',bbox_inches='tight')
    plt.show()
def precess(data):
    numdate = []
    strdate = []
    arcsec = []
    v = np.array(data[0]['coord']) # Reference (3D)
    for datum in data:
        u = np.array(datum['coord']) # Perihelion (3D)
        ratio = np.dot(u,v)/np.sqrt(np.dot(u,u)*np.dot(v,v))
        if np.abs(ratio) <= 1:
            angle = 3600*np.degrees(np.arccos(ratio))
            numdate.append(datum['numdate'])
            strdate.append(datum['strdate'])
            arcsec.append(angle)
    return (numdate,strdate,arcsec)
def add2plot(numdate,actual):
    r = stats.linregress(numdate,actual)
    bestfit = []
    for k in range(len(numdate)):
        bestfit.append(r[0]*numdate[k]+r[1])
    plt.plot(numdate,bestfit,'b-')
    plt.legend(["Actual data","Best fit line"])
    

main()
