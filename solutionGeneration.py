
solutions = []

for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            for l in range(1, 7):
                solutions.append([i, j, k, l])  # Convert tuple to list

print(len(solutions))


# Convert solutions list to a CSV using pandas
import pandas as pd


# Convert solutions list to a DataFrame with a single column
df = pd.DataFrame({'combinations': solutions})


df.to_csv('solutions.csv', index=False, header=False)