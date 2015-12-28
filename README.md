# Predict-pollution-in-an-asian-megacity
Predict pollution in an asian megacity for PLUME labs

* #### reference :
https://challengedata.ens.fr/en/challenge/2/predict_pollution_in_an_asian_megacity.html

* #### data :
The data could be downloaded from the site above, and they are supposed to be put in the folder called "raw data". Attention! Xtrain and Xtest are .zip format files.

### Introduction for PLUME_function.py :
* #### DataImporting : 
function for importing data.
It returns Xtrain,Ytrain,Xtest,VarNames.
* #### DataSample :
DataSample(data,index,date = 'None'):
    "X is the data set, index is the variable name, and date in the date, you can add hours after the date". It returns a dataframe.
* #### DataOutput :
DataOutput(filename,data,index,date = "None"): Output csv file in the folder sample data.
* #### SimpleRegression : 
SimpleRegression(X,Y,X_hour,Y_hour,Object): Output MSE and $R^2$
    
## schedule ：

### 24-12-2015
* set-up from prof : bug fixed.

### 25-12-2015
* add DataImporting function ( found in PLUME_function.py ), finish analysis of var names
* add DataSample function ( found in PLUME_function.py )
* add DataOutput function ( the .csv file will be found in the folder "sample data")

### 28-12-2015
* add features to DataSample function
* add SimpleRegression function
* add nominal variable analysis (boxplot, test not finished)
