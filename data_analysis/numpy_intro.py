# NumPy Introduction
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Creating Sample Data
data = {
    'Species': ['Setosa', 'Versicolor', 'Virginica'],
    'Sepal Length': [5.1, 7.0, 6.3],
    'Sepal Width': [3.5, 3.2, 3.3]
}
df = pd.DataFrame(data)

# 2. Basic Line Plot
plt.plot(df['Species'], df['Sepal Length'], marker='o')
plt.title('Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Sepal Length')
plt.show()

# 3. Bar Plot
sns.barplot(x='Species', y='Sepal Length', data=df)
plt.title('Sepal Length by Species')
plt.show()

# 4. Histogram
plt.hist(df['Sepal Length'], bins=5)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

# 5. Scatter Plot
plt.scatter(df['Sepal Length'], df['Sepal Width'])
plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()

# 6. Box Plot
sns.boxplot(x='Species', y='Sepal Length', data=df)
plt.title('Box Plot of Sepal Length by Species')
plt.show()

# 7. Pair Plot
iris = sns.load_dataset("iris")
sns.pairplot(iris, hue='species')
plt.title('Pair Plot of Iris Dataset')
plt.show()

# 8. Heatmap
corr = iris.corr()
sns.heatmap(corr, annot=True)
plt.title('Heatmap of Correlation Matrix')
plt.show()

# 9. Customizing Plots
plt.figure(figsize=(10, 5))
plt.plot(df['Species'], df['Sepal Length'], marker='o', color='red')
plt.title('Customized Plot')
plt.xlabel('Species')
plt.ylabel('Sepal Length')
plt.grid()
plt.show()

# 10. Saving Plots
plt.figure()
plt.plot(df['Species'], df['Sepal Length'], marker='o')
plt.savefig('sepal_length_plot.png')

# 11. Adding Legends
plt.figure()
plt.plot(df['Species'], df['Sepal Length'], marker='o', label='Sepal Length')
plt.title('Legend Example')
plt.legend()
plt.show()

# 12. Subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].bar(df['Species'], df['Sepal Length'])
axes[0].set_title('Bar Plot')
axes[1].scatter(df['Sepal Length'], df['Sepal Width'])
axes[1].set_title('Scatter Plot')
plt.show()

# 13. FacetGrid
g = sns.FacetGrid(iris, col="species")
g.map(plt.scatter, "sepal_length", "sepal_width")
plt.show()

# 14. Area Plot
plt.fill_between(df['Species'], df['Sepal Length'], color='skyblue', alpha=0.5)
plt.title('Area Plot Example')
plt.show()

# 15. Polar Plot
theta = [0, 1, 2, 3, 4]
radii = df['Sepal Length'].values
plt.polar(theta, radii)
plt.title('Polar Plot Example')
plt.show()

# 16. Violin Plot
sns.violinplot(x='Species', y='Sepal Length', data=df)
plt.title('Violin Plot Example')
plt.show()

# 17. Cumulative Distribution Function (CDF)
plt.hist(df['Sepal Length'], bins=10, cumulative=True, color='blue', alpha=0.5)
plt.title('CDF of Sepal Length')
plt.show()

# 18. 3D Plot (Requires mpl_toolkits)
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['Sepal Length'], df['Sepal Width'], zs=[1, 2, 3], zdir='y', alpha=0.8)
ax.set_title('3D Scatter Plot Example')
plt.show()

# 19. Pie Chart
plt.pie(df['Sepal Length'], labels=df['Species'], autopct='%1.1f%%')
plt.title('Pie Chart Example')
plt.show()

# 20. Combining Matplotlib and Seaborn
sns.set_style("whitegrid")
plt.figure(figsize=(10, 5))
sns.barplot(x='Species', y='Sepal Length', data=df, palette='pastel')
plt.title('Combined Plot Example')
plt.show()
