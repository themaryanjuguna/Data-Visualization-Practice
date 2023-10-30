import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset from seaborn
iris = sns.load_dataset('iris')

# Create a bubble chart
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', size='petal_length', sizes=(20, 1000), hue='species')

# Add labels and title
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Iris Sepal Size')

# move legend outside the chart
plt.legend(bbox_to_anchor=(1.01, 1),borderaxespad=0)

# Show the plot
plt.show()