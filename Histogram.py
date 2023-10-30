import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have a list of test scores called 'scores'
scores = [78, 85, 90, 74, 92, 85, 76, 88, 80, 90, 85, 82, 94, 83]

# Create a histogram
sns.histplot(scores, bins=8)
plt.title('Distribution of Test Scores')
plt.xlabel('Scores')
plt.ylabel('Frequency')
plt.show()