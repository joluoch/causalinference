import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import numpy as np
# Set random seed
seed = 42

################################
########## DATA PREP ###########
################################

# Load in the data
#df = pd.read_csv("wine_quality.csv")

data = pd.read_csv('../data/data_outlier.csv')





# Split into train and test sections
target_name = "diagnosis"
target = data[target_name]
data = data.drop(columns=target_name)

data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=0.30, random_state=42)


#################################
########## MODELLING ############
#################################

# Fit a model on the train section

select_feature = SelectKBest(chi2, k=5)
select_feature.fit(data_train, target_train)



##########################################
##### PLOT FEATURE IMPORTANCE ############
##########################################
# Calculate feature importance in random forest
importances = select_feature.feature_importances_
labels = data.columns
feature_df = pd.DataFrame(list(zip(labels, importances)), columns = ["feature","importance"])
feature_df = feature_df.sort_values(by='importance', ascending=False,)

# image formatting
axis_fs = 18 #fontsize
title_fs = 22 #fontsize
sns.set(style="whitegrid")

ax = sns.barplot(x="importance", y="feature", data=feature_df)
ax.set_xlabel('Importance',fontsize = axis_fs) 
ax.set_ylabel('Feature', fontsize = axis_fs)#ylabel
ax.set_title('Random forest\nfeature importance', fontsize = title_fs)

plt.tight_layout()
plt.savefig("feature_importance.png",dpi=120) 
plt.close()



