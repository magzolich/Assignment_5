# easter egg hunt with csv
# You decided that every chocolate egg is worth three points and the regular one, one point.
# It appeared that some of found regular eggs laid in bushes since the last Easter, no points for the stinky ones, sorry.
# Your job is to analyze and present the results. Pandas will help you with this task.

# Who is the winner?
# How many chocolate eggs was found in total?
# Print individual results (kid and his/her score)
# Print team results (by family)
# Install 'openpyxl' library and use it to print the individual results to 'result.xlsx' file

import pandas as pd

df = pd.read_csv("egghunt.csv")
# print(df)

# Who is the winner?
score = df['chocolate']*3+df['regular']
df['score'] = score
print(df)
winner = df.max(axis=0)
print(winner)

# How many chocolate eggs was found in total?
total_chocolate_eggs = df['chocolate'].sum()
print("Total number of chocolate eggs founded is:", total_chocolate_eggs)

# Print individual results (kid and his/her score)
kid_and_score = df[['name', 'score']]
print(kid_and_score)

# Print team results (by family)
family_score = df[['family', 'score']]
family_score_total = family_score.groupby(['family']).sum()
print(family_score_total)

# Install 'openpyxl' library and use it to print the individual results to 'result.xlsx' file
# kid_and_score.to_excel("results.xlsx")
