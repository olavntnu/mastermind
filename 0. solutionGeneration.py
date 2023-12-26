solutions  = []

for i in range (1,7):
    for j in range (1,7):
        for k in range (1,7):
            for l in range (1,7):
                solutions.append([i,j,k,l])

print(len(solutions))

#Convert solutions list to a csv using pandas
import pandas as pd
df = pd.DataFrame(solutions)
df.to_csv('solutions.csv', index=False, header=False)
