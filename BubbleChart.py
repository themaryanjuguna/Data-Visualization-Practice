import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create an imaginary dataset
data = pd.DataFrame({
    'City': ['London', 'Paris', 'Rome', 'Lagos', 'Nairobi', 'Accra', 'Berlin', 'Cairo'],
    'Population': [8900000, 2141000, 2873000, 21000000, 4397000, 2062000, 3645000, 20340000],
    'Average Temperature (C)': [13, 12, 18, 28, 24, 28, 9, 32],
    'Pollution Level': [3, 2, 2, 6, 5, 4, 2, 7]
})

# Create a bubble chart
sns.scatterplot(data=data, x='Average Temperature (C)', y='Pollution Level', size='City', hue='City', sizes=(20, 1000))

# Add labels and title
plt.xlabel('Average Temperature (C)')
plt.ylabel('Pollution Level')
plt.title('Temperature vs Pollution Level')

# move legend outside the chart
plt.legend(bbox_to_anchor=(1.01, 1),borderaxespad=0)

# Show the plot
plt.show()