# Now making a function

# We use def to make a function to make code easier
# In this function we write all the code without putting values or path of the file we use UI


import numpy as np
import csv
import pandas as pd
import plotly.express as px

def graph(path):
  with open(path) as csv_file:
    bh=csv.DictReader(csv_file)
    fig = px.scatter(bh, x="Coffee in ml" , y="sleep in hours")
    fig.show()

def get_dataStore(path):
  ice_S = []
  cold_S = []
  with open(path) as csv_file:
    bh=csv.DictReader(csv_file)
    for r in bh:
      ice_S.append(float(r["Coffee in ml"]))
      cold_S.append(float(r["sleep in hours"]))
  return{"x":ice_S,"y":cold_S}

def find_relation(path1):
  corelation = np.corrcoef(path1["x"],path1["y"])
  print(corelation[0,1])

path="Data-1.csv"
path1=get_dataStore(path)
find_relation(path1)
graph(path)