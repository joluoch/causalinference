import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import statsmodels.api as sm
from sklearn.preprocessing import LabelEncoder
from dowhy import CausalModel
from IPython.display import Image, display
import os 
import sys





class Causal_Model:
    def __init__(self,df:pd.DataFrame,treatment:str,outcome:str)->None:
        self.df=df
        self.treatment=treatment
        self.outcome=outcome

    def dowhy_model(self):
        labelencoder = LabelEncoder()
        self.df[self.outcome] = labelencoder.fit_transform(self.df[self.outcome])
        cols=list(self.df.columns)
        if self.treatment in cols and self.outcome in cols :
            xs = self.df.drop([self.treatment,self.outcome], axis = 1)
        xs=xs.columns.tolist()
        model=CausalModel(
            data= self.df,
            treatment=self.treatment,
            outcome=self.outcome,
            common_causes=xs
        )
        model.view_model()
        display(Image(filename="causal_model.png"))
        estimands = model.identify_effect() 
        print(estimands)
        estimate = model.estimate_effect(estimands,method_name = "backdoor.propensity_score_weighting")
        print(estimate)
        refutel1 = model.refute_estimate(estimands,estimate, "random_common_cause")
        print(refutel1)
        refutel2 = model.refute_estimate(estimands,estimate, "data_subset_refuter")
        print(refutel2)
        refutel3 = model.refute_estimate(estimands,estimate, "placebo_treatment_refuter")
        print(refutel3)
        return estimands