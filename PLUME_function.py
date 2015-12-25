import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#function for data importing
def DataImporting():
    'Data importing : Xtrain, Ytrain & Xtest'
    Xtrain = pd.read_csv('raw data/XtrainDfInterpolatedFilteredWithoutIndex.csv',sep = ',',header = 0)
    Ytrain = pd.read_csv('raw data/Ytrain.csv',sep = ';',header = 0)
    Xtest = pd.read_csv('raw data/XtestDfInterpolatedFilteredWithoutIndex.csv',sep = ',',header = 0)
    variable_names = Xtrain.columns.values
    var_names=[[] for i in range(len(variable_names))]
    for i in range(len(variable_names)):
        if len(variable_names[i].split('_')) >= 3:
            var_names[i] = '_'.join(variable_names[i].split('_')[0:-1])
        elif len(variable_names[i].split("_")) == 2:
            var_names[i] = variable_names[i].split('_')[0]
        else:
            var_names[i] = variable_names[i]
    VarNames = sorted(list(set(var_names)))
        
    return Xtrain,Ytrain,Xtest,VarNames

#function for data sampling
def DataSample(data,index,date = 'None'):
    "X is the data set"
    "index is the variable name"
    "date in the date, you can add hours after the date"
    c = [0]
    for i in range(len(data.columns.values)):
        if index in data.columns.values[i]:
            c.append(i)
    if date == 'None':        
        return data.iloc[:,c]
    else:
        d = []
        for i in range(len(data)):
            if date in data.date.values[i]:
                d.append(i)
        return data.iloc[d,c]

#output dataframe in csv format
def DataOutput(filename,data,index,date = "None"):
    DataSample(data, index, date = 'None').to_csv('sample data/' + str(filename) ,sep = ',',header = True, index = False,encoding ='utf-8')
    return 'The file has been created !'







    
    