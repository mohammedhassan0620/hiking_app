import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\ELCOT\OneDrive\New folder\Dataset.csv.csv")
top_cuisines = df['Cuisines'].value_counts().head(3)
percentages = (top_cuisines / len(df)) * 100
print("Top 3 cuisines:\n", top_cuisines)
print("\nPercentage of restaurants serving each:\n", percentages)
with open("Level1_Task1_TopCuisines.txt", "w") as f:
    f.write("Top 3 cuisines:\n")
    f.write(str(top_cuisines))
    f.write("\n\nPercentages:\n")
    f.write(str(percentages))
top_cuisines.plot(kind='bar', color='skyblue')
plt.title("Top 3 Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.savefig("Level1_Task1_TopCuisines.png")
plt.show()
