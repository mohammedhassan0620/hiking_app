import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\ELCOT\OneDrive\New folder\Dataset.csv.csv")
correlation = df['Aggregate rating'].corr(df['Votes'])
print("Correlation between Aggregate Rating and Votes:", correlation)
with open("Level2_Task4_Correlation.txt", "w", encoding='utf-8') as f:
    f.write("Correlation between Aggregate Rating and Votes:\n")
    f.write(str(correlation))
plt.figure(figsize=(8, 6))
plt.scatter(df['Aggregate rating'], df['Votes'], color='teal', alpha=0.6)
plt.title("Correlation between Rating and Votes")
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Votes")
plt.tight_layout()
plt.savefig("Level2_Task4_Correlation.png")
plt.show()
