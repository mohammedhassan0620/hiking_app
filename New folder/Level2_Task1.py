import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\ELCOT\OneDrive\New folder\Dataset.csv.csv")
rating_counts = df['Aggregate rating'].value_counts().sort_index()
percentages = (rating_counts / len(df)) * 100
print("Rating distribution:\n", rating_counts)
print("\nPercentages:\n", percentages)
with open("Level2_Task1_Ratings.txt", "w") as f:
    f.write("Rating distribution:\n")
    f.write(str(rating_counts))
    f.write("\n\nPercentages:\n")
    f.write(str(percentages))
plt.figure(figsize=(10, 6))
rating_counts.plot(kind='bar', color='purple')
plt.title("Distribution of Restaurant Ratings")
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.savefig("Level2_Task1_Ratings.png")
plt.show()
