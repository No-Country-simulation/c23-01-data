### We use this file to define functions that will use regularly in different files
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.metrics import accuracy_score, recall_score, f1_score, classification_report
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    classification_report,
    confusion_matrix,
)
from sklearn.metrics import RocCurveDisplay, roc_auc_score, roc_curve
from sklearn.metrics import precision_recall_curve, PrecisionRecallDisplay

import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler


# Define an scaler that transforms only non-binary data.
# In our case we have ordinal features 
def my_scaler(X,scaler):
    scaler = scaler
    X_copy = X.copy()
    
    for col in X_copy.columns:
        if X_copy[col].nunique()!=2:
            X_copy[col] = scaler.fit_transform(X[[col]])
    return X_copy

### Define a new class
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler

class OrdinalStandardScaler(BaseEstimator, TransformerMixin):
    def __init__(self, ordinal_features):
        """
        Initialize the transformer.
        
        Parameters:
        ordinal_feature_indices : list or array with the ordinal features to be transformed
        """
        self.ordinal_features = ordinal_features
        self.scaler = StandardScaler()
        
    def fit(self, X, y=None):
        """
        Fit the transformer to the data.
        
        Parameters:
        X : array-like of shape (n_samples, n_features)
            Input data
        y : None
            Ignored
        """
        # Extract ordinal features and fit the scaler
        ordinal_features = X[self.ordinal_features]
        self.scaler.fit(ordinal_features)
        return self
    
    def transform(self, X):
        """
        Transform the data.
        
        Parameters:
        X : array-like of shape (n_samples, n_features)
            Input data
        """
        # Create a copy of the input data
        X_transformed = X.copy()
        
        # Scale only the ordinal features
        X_transformed[self.ordinal_features] = self.scaler.transform(
            X[self.ordinal_features]
        )
        
        return X_transformed
    
    def fit_transform(self, X, y=None):
        """
        Fit the transformer to the data and transform it.
        """
        return self.fit(X, y).transform(X)

## Define a function to summarize the metrics of our model training
def evaluate_model(model, X_train, y_train, X_test, y_test):

    #set model to the input model
    model = model
    
    ## Fit model to training data
    model.fit(X_train, y_train)

    ## Predictions of the model for both training and test sets
    y_predict_train = model.predict(X_train)
    y_predict_test = model.predict(X_test)

    y_test_score = model.predict_proba(X_test)[:,1]

    ## Classification report
    print("Classification report for training data")
    print(classification_report(y_train,y_predict_train))
    
    print("Classification report for test data")
    print(classification_report(y_test,y_predict_test))

    # Plot confusion matrix
    print("Confusion matrix for test set")
    ConfusionMatrixDisplay.from_estimator(model,X_test,y_test);

    "Ask the function to return the probability scores"
    #return y_test_score

def AUC_study(model, X_test, y_test):   

    y_test_score = model.predict_proba(X_test)[:,1]
    fpr, tpr, thresholds = roc_curve(y_test, y_test_score)
    
    distances = np.sqrt(fpr**2 + (1-tpr)**2)
    optimal_idx = np.argmin(distances)
    optimal_threshold = thresholds[optimal_idx] 

    print("The optimal threshold to minimize the fpr and maximize the tpr is:", optimal_threshold)
    print("The false positive rate at the opt threshold:", fpr[optimal_idx])
    print("The true positive rate at the opt threshold:", tpr[optimal_idx])

    roc_auc = roc_auc_score(y_test, y_test_score)
    display = RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc)
    display.plot();

    


