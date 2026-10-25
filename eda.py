import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
df = pd.read_csv('StudentPerformanceFactors.csv')
df.head()
df.shape    # it return rows and columns of the dataset.
df.columns.tolist()     # it return the list of columns in the dataset.
df.info()   # it return the information about the dataset.(jaise column name , non-null values, and data type of each column.)
df.isnull().sum()   # it return the number of missing values in each column of the dataset.
df.isnull().sum()[df.isnull().sum() > 0]
# Understand data  --> dataset's dimensions, column names, data types, and statistical properties to understand the information available for analysis.

print("Dataset shape:", df.shape)       # it will return the number of rows and columns
print(df.columns.tolist())      # column names
print(df.dtypes)        # data types of each column

numerical_cols = df.select_dtypes(include="number").columns.tolist()        # it will return the list of numerical columns in the dataset.
categorical_cols = df.select_dtypes(include=["str", "category", "bool"]).columns.tolist()       # it will return the list of categorical columns in the dataset.
print("Numerical columns:", numerical_cols)
print("\nCategorical columns:", categorical_cols)
missing = df.isnull().sum()     # it will return the number of missing values in each column of the dataset.
missing_summary = pd.DataFrame({
    "Missing_Count": missing,
    "Missing_Percentage": (missing / len(df) * 100).round(2)
})                              # it will create a new DataFrame called missing_summary that contains the count and percentage of missing values for each column in the original DataFrame df.

missing_summary = missing_summary[
    missing_summary["Missing_Count"] > 0
].sort_values("Missing_Percentage", ascending=False)    # it will sort the DataFrame by the percentage of missing values in descending order

missing_summary
print("Duplicate rows:", df.duplicated().sum())     # it will return the number of duplicate rows in the dataset.

df[numerical_cols].describe().T     # it will return the statistical summary of the numerical columns in the dataset, including count, mean, standard deviation, minimum, maximum, and quartiles.
for col in categorical_cols:
    print(f"\n--- {col} ---")
    print(df[col].value_counts(dropna=False))
sns.histplot(data=df, x="Exam_Score", bins=20)
plt.title("Distribution of Exam Scores")
plt.show()
sns.scatterplot(data=df, x="Hours_Studied", y="Exam_Score")
plt.title("Study Hours vs Exam Score")
plt.show()
sns.barplot(data=df, x="School_Type", y="Exam_Score")
plt.title("Average Exam Score by School Type")
plt.show()
selected_cat_cols = [
    "Parental_Involvement",
    "Internet_Access",
    "School_Type",
    "Gender"
]

fig, axes = plt.subplots(2, 2, figsize=(13, 9))

for col, ax in zip(selected_cat_cols, axes.flatten()):
    sns.countplot(data=df, x=col, ax=ax)
    ax.set_title(f"Count of {col}")
    ax.tick_params(axis="x", rotation=25)

plt.tight_layout()
plt.show()
