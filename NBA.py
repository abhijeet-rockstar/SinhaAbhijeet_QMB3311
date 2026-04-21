import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = pd.read_csv('nbaShots17_18.csv')

# Insight 1: Summary Statistics
# Mean shot distance for made vs missed shots
summary_stats = df.groupby('SHOT_MADE_FLAG')['SHOT_DISTANCE'].mean()
print("Average Shot Distance by Outcome:")
print(f"Missed Shot (0): {summary_stats[0]:.2f} ft")
print(f"Made Shot (1): {summary_stats[1]:.2f} ft")
print("-" * 30)

# Insight 2: Regression Analysis
# Predicting SHOT_MADE_FLAG based on SHOT_DISTANCE
X = df['SHOT_DISTANCE']
X = sm.add_constant(X)
y = df['SHOT_MADE_FLAG']

model = sm.Logit(y, X).fit()
print(model.summary())
