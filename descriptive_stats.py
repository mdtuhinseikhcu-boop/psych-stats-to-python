import pandas as pd

# Fake data: replace with your real data later
data = {'Group_A': [23, 25, 21, 27, 24], 'Group_B': [30, 28, 32, 29, 31]}
df = pd.DataFrame(data)

print("Descriptive Statistics:")
print(df.describe())

print("\nMean difference:")
print(df['Group_B'].mean() - df['Group_A'].mean())
Transitioning from SPSS to Python for cognitive modeling. Application project for UTN Human & AI M.Sc. 2026
