import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\ELCOT\OneDrive\New folder\Dataset.csv.csv")
price_counts = df['Price range'].value_counts()
percentages = (price_counts / len(df)) * 100
print("Price range distribution:\n", price_counts)
print("\nPercentages:\n", percentages)
with open("Level1_Task3_PriceRange.txt", "w") as f:
    f.write("Price range distribution:\n")
    f.write(str(price_counts))
    f.write("\n\nPercentages:\n")
    f.write(str(percentages))
plt.figure(figsize=(8, 6))
price_counts.plot(kind='bar', color='orange')
plt.title("Distribution of Price Ranges")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.savefig("Level1_Task3_PriceRange.png")
plt.show()
