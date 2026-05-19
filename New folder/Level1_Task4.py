import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\ELCOT\OneDrive\New folder\Dataset.csv.csv")
delivery_counts = df['Has Online delivery'].value_counts()
percentages = (delivery_counts / len(df)) * 100
print("Online delivery availability:\n", delivery_counts)
print("\nPercentages:\n", percentages)
with open("Level1_Task4_OnlineDelivery.txt", "w") as f:
    f.write("Online delivery availability:\n")
    f.write(str(delivery_counts))
    f.write("\n\nPercentages:\n")
    f.write(str(percentages))
plt.figure(figsize=(6, 5))
delivery_counts.plot(kind='bar', color=['green', 'red'])
plt.title("Restaurants Offering Online Delivery")
plt.xlabel("Online Delivery (Yes/No)")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.savefig("Level1_Task4_OnlineDelivery.png")
plt.show()
