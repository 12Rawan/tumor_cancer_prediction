
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn import metrics
import joblib


#y_pred_test




class logistic__regression:
    def __init__ (self ,x_train , x_test , y_train , y_test , model3_filename , result ,  y_pred_logistic_test , model3):
    
        self.x_train =x_train 
        self.x_test = x_test
        self. y_train= y_train 
        self.y_test=y_test
        self.model3_filename = "logistic_model_job_lib.job_lib" 
        self.result =[]
        self.y_pred_logistic_test =  []
        self.model3 = LogisticRegression()
        
        
        
    def classification_logistic(self):
        
        


     #Train data
        self.model3.fit(self.x_train, self.y_train)
    
      
    # Predicting the Training data
        y_pred_logistic_train = self.model3.predict(self.x_train)         
    # Predicting the Test data
        self.y_pred_logistic_test =  self.model3.predict(self.x_test)
    
    
   

        
        
        
        # Making the Confusion Matrix for logistic regression
        Confusion_Matrix_logistic = confusion_matrix(self.y_test, self.y_pred_logistic_test)
#Model Accuracy for Logistic Regression
        logistic_regression_accuracy = metrics.accuracy_score(self.y_test, self.y_pred_logistic_test) 
        
        # save model 
        joblib.dump( self.model3, self.model3_filename)
        print('Model is saved into to disk successfully')
        
        
        print( self.y_pred_logistic_test , self.model3 , logistic_regression_accuracy , Confusion_Matrix_logistic)
        
        
    def load_logistic(self):
        logistic_model = joblib.load(self.model3_filename)
        self.result = logistic_model.predict(self.x_test)
        print(self.result) 
        print ("Logistic Accuracy : " ,logistic_model.score(self.x_test,self.y_test))



