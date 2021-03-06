
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
import matplotlib.pyplot as plt # for data visualization 
from sklearn.metrics import confusion_matrix
import joblib


class decision_tree:
    model_decision_filename = "decision_model_job_lib.job_lib"
    result= []
    y_pred_decision_test= []
    model_1 = DecisionTreeClassifier(max_depth=2, random_state=0)
         
    def __init__ (self ,x_train , x_test , y_train ,  y_test ):
        self.x_train =x_train 
        self.x_test = x_test
        self. y_train= y_train 
        self.y_test=y_test
      
    def classification_decision (self):
                    
        self.model_1.fit(self.x_train, self.y_train)
        
           # predicting train result
       # y_pred_decision_train =  self.model_1.predict(self.x_train)
           
    # predicting test result
        self.y_pred_decision_test =  self.model_1.predict(self.x_test)
               
       # Making the Confusion Matrix for Logistic Regression
        decision_cm = confusion_matrix(self.y_test, self.y_pred_decision_test)
      # model accuracy for each model
        decisiontree_accuracy = metrics.accuracy_score(self.y_test , self.y_pred_decision_test)
                     
       # save model        
        joblib.dump(  self.model_1, self.model_decision_filename)
        print( end = '\n')
        print('Model decision is saved into to disk successfully')
        print( end = '\n')
     
        print("DECISION TREE MODEL ::  ")
        print( end = '\n')
        print ("predict is : " , self.y_pred_decision_test )
        print( end = '\n')

        print("accuracy is  : " , decisiontree_accuracy )
        print( end = '\n')
        print("confusion matrix is : " , decision_cm )
        print( end = '\n')
        print ("-------------------------------------------------------------")
                  
     #load model    
    def load_decision(self,test1):
        decision_model = joblib.load(self.model_decision_filename)
        self.result = decision_model.predict(test1)
        print( end ='\n')
        print("Decision predict is : " ,self.result)    
        print( end = '\n')
        print("...................................................................")
        
        
   





    
            
            
        
        


        
                  
           


