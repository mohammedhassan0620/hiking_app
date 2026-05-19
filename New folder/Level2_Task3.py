import pandas as pd
df = pd.read_csv(r"C:\Users\ELCOT\OneDrive\New folder\Dataset.csv.csv")
city_cuisine_counts = df.groupby(['City', 'Cuisines']).size().reset_index(name='Count')
top_cuisine_per_city = city_cuisine_counts.loc[city_cuisine_counts.groupby('City')['Count'].idxmax()]
print("Most popular cuisine in each city:\n", top_cuisine_per_city)
top_cuisine_per_city.to_csv("Level2_Task3_TopCuisinePerCity.csv", index=False, encoding='utf-8')
with open("Leve2_Task3_TopCuisinePerCity.txt", "w", encoding='utf-8') as f:
    f.write("Most popular cuisine in each city:\n\n")
    f.write(top_cuisine_per_city.to_string(index=False))
