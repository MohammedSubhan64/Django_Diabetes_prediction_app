from tokenize import String
from django.shortcuts import render
#imports of prediction model
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
# from sklearn.svm import SVC
# Create your views here.
def index(request):
    return render(request,"index.html")
    # return HttpResponse("home page")

def about(request):
     return render(request,"about.html")

def predict(request):
    return render(request,"predict.html")

def result(request):
    df = pd.read_csv(r'D:\Django websites\Diabetes\static\diabetes_refined.csv')
    y = df.class_n
    X = df.drop('class_n',axis='columns')
    X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.8,random_state=10)
    rf = RandomForestClassifier(n_estimators=40,random_state=10)
    rf.fit(X_train,y_train)
    # rf.score(X_test,y_test)    
    v1= int(request.GET['n1'])
    v2=str(request.GET['n2'])
    if v2=="Male":
        v22=1
    else:
        v22=0
    #v2=int(request.GET['n2'])
    def bin(x):
        if(x=="Yes"):
            return 1
        else:
            return 0
    v3= str(request.GET['n3'])
    v33=bin(v3)
    v4= str(request.GET['n4'])
    v44=bin(v4)
    v5= str(request.GET['n5'])
    v55=bin(v5)
    v6= str(request.GET['n6'])
    v66=bin(v6)
    v7=str(request.GET['n7'])
    v77=bin(v7)
    v8= str(request.GET['n8'])
    v88=bin(v8)
    v9= str(request.GET['n9'])
    v99=bin(v9)
    v10= str(request.GET['n10'])
    v100=bin(v10)
    v11= str(request.GET['n11'])
    v111=bin(v11)
    v12= str(request.GET['n12'])
    v122=bin(v12)
    v13= str(request.GET['n13'])
    v133=bin(v13)
    v14= str(request.GET['n14'])
    v144=bin(v14)
    v15= str(request.GET['n15'])
    v155=bin(v15)
    v16= str(request.GET['n16'])
    v166=bin(v16)
    pred=rf.predict([[v1,v22,v33,v44,v55,v66,v77,v88,v99,v100,v111,v122,v133,v144,v155,v166]])
    # p=pred[0]
    result1=""
    if pred==[1]:
        result1 ="Oops! Seems like you are diabetes 'POSITIVE',   please get yourself tested"
    elif pred==[0]:
        result1 ="Hurray! Seems like you are diabetes Negative"

    return render(request,"predict.html",{"result2":result1})





    # df = pd.read_csv('static\diabetes_refined.csv')
    # y = df.class_n
    # X = df.drop('class_n',axis='columns')
    # X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.8,random_state=10)
    # model_svm = SVC(kernel='linear')
    # model_svm.fit(X_train,y_train)
    # #model_svm.score(X_test,y_test)
    # #X_test.head()
    #  try:
    #     if pred==[1]:
    #         result1 ="Oops! Seems like you are diabetes 'POSITIVE',   please get yourself tested"
    #     elif pred==[0]:
    #         result1 ="Hurray! Seems like you are diabetes Negative."
    # except:
    #     result1="Please Enter all details"