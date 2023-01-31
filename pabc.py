# Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from sklearn import impute
from apyori import apriori

from utils.main import transform_dataset, data_prepare, extract
from utils.chart import plot_chart_all, plot_chart_numerical
from utils.output import displayResult


# Read excel file (sheet name: 'After matched')
clinical_experiment = pd.read_excel('data/pabc_dataset.xlsx', sheet_name='After matched')

# print(clinical_experiment.shape)
displayResult('Shape of Dataset', clinical_experiment.shape)
displayResult('Dataset Info', clinical_experiment.info())

# Check number of occurence of text value in 'Age at first delivery' column
displayResult('Age at first delivery', clinical_experiment['Age at first delivery'].value_counts())

# Check if missing or null values exist in other columns
displayResult('Missing/Null Values', clinical_experiment.isnull().sum())

# Change text (未生育) in 'Age at first delivery' column to null (using np.nan)
clinical_experiment['Age at first delivery'] = clinical_experiment['Age at first delivery'].replace(['未生育'], [np.nan])

displayResult('Uniques Age Values', clinical_experiment['Age at first delivery'].unique())

# Replace missing values with median
numImputer = impute.SimpleImputer(missing_values=np.nan, strategy='median')
numImputer = numImputer.fit(clinical_experiment[['Age at first delivery', 'Tumor size cm']])

# Transform data and save as integer type
clinical_experiment[['Age at first delivery', 'Tumor size cm']] = numImputer.transform(
    clinical_experiment[['Age at first delivery', 'Tumor size cm']]
).astype(int)

displayResult('Updated Age Values', clinical_experiment['Age at first delivery'].unique())

# Describe dataset
clinical_experiment.describe(include='all')

# Univariate distribution of numerical variables in dataset
plot_chart_all(clinical_experiment)

# Distribution of numerical variables in the breast_tissue dataset
plot_chart_numerical(clinical_experiment)

# Pre-process data
transformed_dataset = transform_dataset(clinical_experiment)
displayResult('Transformed Dataset', transformed_dataset)

# View summation of positives and negatives in the dataset
death = (transformed_dataset=='Yes').sum()
survival = (transformed_dataset=='No').sum()
os_status = pd.concat([death, survival], axis=1, keys=['Death', 'Survival'])

os_status.plot.bar(figsize=(16,8))
plt.title('Summation of Positives and Negatives')

# Prepare dataset
list_of_item_sets = data_prepare(transformed_dataset)

# Create association rules
rules = list(apriori(list_of_item_sets, min_support=0.02, min_confidence=0.2))
association_rules = extract(rules)
rules_dataframe = pd.DataFrame(association_rules, columns=['LHS', 'RHS', 'Support', 'Confidence', 'Lift'])

displayResult('Number of rules created', len(rules_dataframe))

rules_dataframe.describe(include='all')
rules_dataframe.nlargest(10, 'Lift')
rules_dataframe.nlargest(10, 'Support')
rules_dataframe.nlargest(10, 'Confidence')

non_empty_rules = rules_dataframe[rules_dataframe['LHS'].apply(lambda x: len(x) > 0)]
highest_support = non_empty_rules.sort_values(by=['Support'], ascending=False)
highest_lift = non_empty_rules.sort_values(by=['Lift'], ascending=False)

displayResult('Highest Support: ', highest_support)
displayResult('Highest Lift: ', highest_lift)

# Create association rules (decrease size of maximum itemset)
rules = list(apriori(list_of_item_sets, min_support=0.02, min_confidence=0.2, max_length=3))
association_rules = extract(rules)
rules_dataframe = pd.DataFrame(association_rules, columns=['LHS', 'RHS', 'Support', 'Confidence', 'Lift'])

displayResult('Number of rules created', len(rules_dataframe))

rules_dataframe.sort_values(by=['Support'], ascending=False)

# Create association rules for HR (Reason: From the plot, HR has more records of death)
rules = list(apriori(list_of_item_sets, min_support=0.04, min_confidence=0.54))
hr_association_rules = extract(rules, 'HR')
hr_rules_dataframe = pd.DataFrame(hr_association_rules, columns=['LHS', 'RHS', 'Support', 'Confidence', 'Lift'])

hr_rules_dataframe = hr_rules_dataframe[hr_rules_dataframe['LHS'].apply(lambda x: len(x) > 0)]

displayResult('Rules', hr_rules_dataframe)

figure = px.scatter(hr_rules_dataframe, x='Support', y='Confidence', color='Lift', hover_data=['LHS', 'RHS'], size='Confidence', color_continuous_scale='agsunset', title='Generated Rules')

plt.show()
figure.show()
