import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\ELCOT\OneDrive\New folder\Dataset.csv.csv")
votes_summary = df['Votes'].describe()
print("Votes summary:\n", votes_summary)
with open("Level2_Task2_Votes.txt", "w") as f:
    f.write("Votes summary:\n")
    f.write(str(votes_summary))
plt.figure(figsize=(10, 6))
df['Votes'].plot(kind='hist', bins=30, color='blue', edgecolor='black')
plt.title("Distribution of Restaurant Votes")
plt.xlabel("Number of Votes")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("Level2_Task2_Votes.png")
plt.show()
