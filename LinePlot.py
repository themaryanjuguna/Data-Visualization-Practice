import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Imaginary data
dates = ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01']
scores = [85, 90, 80, 95, 88]

# Create a DataFrame with dates and scores
data = {'Date': dates, 'Score': scores}
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Create a line plot using Seaborn
plt.figure(figsize=(15, 6))
sns.lineplot(data=df, x='Date', y='Score')
plt.title('Student Score Progression Over Time')
plt.xlabel('Date')
plt.ylabel('Score')
plt.show()