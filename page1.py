mport matplotlib.pyplot as plt

df['month'] = df['date'].dt.month
monthly_group = df.groupby('month').agg({
    'temperature':'mean',
    'rainfall':'sum',
    'humidity':'mean'
})

# Group by season
def season(month):
    if month in [12,1,2]: return 'Winter'
    elif month in [3,4,5]: return 'Spring'
    elif month in [6,7,8]: return 'Summer'
    else: return 'Autumn'

df['season'] = df['month'].apply(season)
seasonal_group = df.groupby('season').agg({
    'temperature':'mean',
    'rainfall':'sum',
    'humidity':'mean'
})

# Bar chart comparing seasons
seasonal_group[['temperature','rainfall']].plot(kind='bar', figsize=(8,6))
plt.title("Seasonal Climate Comparison")
plt.ylabel("Values")
plt.xlabel("Season")
plt.legend(["Avg Temperature (°C)", "Total Rainfall (mm)"])
plt.savefig("seasonal_comparison.png")