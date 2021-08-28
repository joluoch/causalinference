# causalinference

# introduction 
Breast cancer is the most common malignancy among women, accounting for nearly 1 in 3 cancers diagnosed among women in the United States, and it is the second leading cause of cancer death among women. Breast Cancer occurs as a results of abnormal growth of cells in the breast tissue, commonly referred to as a Tumor. A tumor does not mean cancer - tumors can be benign (not cancerous), pre-malignant (pre-cancerous), or malignant (cancerous). Tests such as MRI, mammogram, ultrasound and biopsy are commonly used to diagnose breast cancer performed.
We will use this data set and make causal graphhs based on our hypothesis to see what causes brest cancer

# Causuality
Causal Inference is the process where causes are inferred from data. And not only do we use causal inference to navigate the world, we use causal inference to solve problems.
Causality is all about interventions, about doing. Standard statistics is all about correlations, which are all good and fun, but correlations can lead to wrong assumptions which can lead to a lot worse thing.

In correlations, the notation is P(x|y) i.e. the probability of x given y: for example, the probability of a disease given an active gene. However, in causal calculus, a very small but important change is made. Instead of P(x|y) it’s P(x|do(y)) i.e. the probability of x given that y is done: for example, the probability of a disease given that I start a diet. The ‘do’ is very important: it represents the intervention, the actual doing of something that will cause the effect.

# dataset
This is an analysis of the Breast Cancer Wisconsin (Diagnostic) DataSet, obtained from Kaggle. This data set was created by Dr. William H. Wolberg, physician at the University Of Wisconsin Hospital at Madison, Wisconsin,USA. To create the dataset Dr. Wolberg used ???uid samples, taken from patients with solid breast masses and an easy-to-use graphical computer program called Xcyt, which is capable of perform the analysis of cytological features based on a digital scan. The program uses a curve-???tting algorithm, to compute ten features from each one of the cells in the sample, than it calculates the mean value, extreme value and standard error of each feature for the image, returninga 30 real-valuated vector


Attribute Information:

ID number 2) Diagnosis (M = malignant, B = benign) 3-32)
Ten real-valued features are computed for each cell nucleus:

radius (mean of distances from center to points on the perimeter)
texture (standard deviation of gray-scale values)
perimeter
area
smoothness (local variation in radius lengths)
compactness (perimeter^2 / area - 1.0)
concavity (severity of concave portions of the contour)
concave points (number of concave portions of the contour)
symmetry
fractal dimension (“coastline approximation” - 1)
The mean, standard error and “worst” or largest (mean of the three largest values) of these features were computed for each image, resulting in 30 features. For instance, field 3 is Mean Radius, field 13 is Radius SE, field 23 is Worst Radius.

