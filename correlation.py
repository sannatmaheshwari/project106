import plotly.express as px
import csv
import numpy as n

def getdatasource(datapath):
    data1 = []
    data2 = []
    with open(datapath) as x:
        df = csv.DictReader(x)
        #graph = px.scatter(df,x="Days Present",y="Marks In Percentage")
        #graph.show()
        for row in df:
            data1.append(float(row["Marks In Percentage"]))
            data2.append(float(row["Days Present"]))
    return {"x":data1,"y":data2}

def getcorrelation(data):
    correlation = n.corrcoef(data["x"],data["y"])
    print("Correlation :- \n--->",correlation[0,1])

def main():
    datasource = getdatasource("data3.csv")
    getcorrelation(datasource)
main()