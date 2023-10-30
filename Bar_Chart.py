import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Imaginary data
subjects = ['Math', 'Science', 'English', 'History']
scores = [85, 90, 75, 80]

# Create a DataFrame with subjects and scores
data = {'Subjects': subjects, 'Scores': scores}
df = pd.DataFrame(data)

# Create a bar plot using Seaborn
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x='Subjects', y='Scores')
plt.title('Student Scores in Different Subjects')
plt.xlabel('Subjects')
plt.ylabel('Scores')
plt.show()

# Run in the terminal python bar_chart.py