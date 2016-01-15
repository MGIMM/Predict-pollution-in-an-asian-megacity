import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model
from scipy import stats

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
def DataSample(data,index,date = 'None',sample_method = "in",keep_date = False):
    "X is the data set"
    "index is the variable name, separated by '-'"
    "date in the date, you can add hours after the date"
    index_list = index.split('-')
    
    if keep_date == True:
        c = [0]
    else:
        c = []
    if sample_method =="in":
        for index_name in index_list:
            for i in range(len(data.columns.values)):

                if index_name in data.columns.values[i]:
                    c.append(i)
    elif sample_method =="equal":
        for index_name in index_list:
            for i in range(len(data.columns.values)):

                if index_name == data.columns.values[i]:
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


def SimpleRegression(X,Y,X_hour,Y_hour,Object):
    bound = np.shape(DataSample(X,Object))[1]
    X_input = DataSample(X,Object).iloc[:,range(24+X_hour,bound,25)]
    Y_output = DataSample(Y,str(Object)+"_04143_"+str(Y_hour),sample_method='equal')
    lm = linear_model.LinearRegression()
    lm.fit(X_input,Y_output)
    MSE = np.mean((Y_output - lm.predict(X_input)) ** 2)
    R2 = lm.score(X_input,Y_output)
    print 'MSE = ' + str(MSE) + '\n'
    print 'R2 = ' + str(R2) + '\n'
    return R2,MSE

# plot histogram
# def PlotHist(data,index)

def MyAnova(X,Y,var,sub_group = 'all'):
    IndexSet =list(set(X[var]))
    TestList = {}
    print 'IndexSet :',IndexSet
    for i in range(len(IndexSet)):
        TestList.update({str(IndexSet[i]) : Y.loc[X[var] == IndexSet[i]]})
    if sub_group == 'all':
        anova = stats.f_oneway(*TestList.values())
    else:
        SubTestList = {key : TestList[key] for key in sub_group} 
        anova = stats.f_oneway(*SubTestList.values())
    return anova


    
    