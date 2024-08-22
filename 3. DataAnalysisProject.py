import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset from Seaborn's built-in datasets
iris = sns.load_dataset('iris')

# Show the initial few rows of the dataset
print(iris.head())

# Summarize basic statistics
print(iris.describe())

# Display data information
print(iris.info())

# Count distribution of the species
print(iris['species'].value_counts())

# Scatter plot of sepal length vs sepal width
plt.figure(figsize=(10, 6))
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species', palette='Set2')
plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.show()

# Pairplot to explore feature relationships
sns.pairplot(iris, hue='species', palette='Set2')
plt.show()

# Box plot to compare feature distributions
plt.figure(figsize=(12, 8))
sns.boxplot(data=iris, orient='h', palette='Set2')
plt.title('Box Plot of Iris Features')
plt.show()