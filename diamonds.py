import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the "diamonds" dataset
diamonds = sns.load_dataset("diamonds")

# Create a scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(data=diamonds, x="carat", y="price")
plt.title("Scatter Plot of Carat vs. Price in Diamonds")
plt.xlabel("Carat")
plt.ylabel("Price")
plt.show()