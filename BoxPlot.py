import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Imaginary data
math_scores    = [85, 90, 75, 80, 92]
science_scores = [78, 85, 88, 82, 90]
english_scores = [70, 80, 75, 85, 82]
history_scores = [80, 85, 88, 90, 85]

# Create a DataFrame with subjects and scores
data = {'Math': math_scores, 'Science': science_scores, 'English': english_scores, 'History': history_scores}
df = pd.DataFrame(data)

# Create a box plot using Seaborn
plt.figure(figsize=(8, 6))
sns.boxplot(data=df)
plt.title('Distribution of Scores in Different Subjects')
plt.xlabel('Subjects')
plt.ylabel('Scores')
plt.show()