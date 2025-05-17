import matplotlib.pyplot as plt
import pandas as pd

def plot_time_series(df, field_name, metric):
    subset = df[df['Nazwa pola'] == field_name]
    subset = subset.dropna(subset=['Data'])
    subset = subset.sort_values('Data')
    plt.figure()
    plt.plot(subset['Data'], subset[metric])
    plt.title(f"{metric} over time for {field_name}")
    plt.xlabel('Date')
    plt.ylabel(metric)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    df = pd.read_csv('../data/smartagro_dane_laboratoryjne.csv', parse_dates=['Data'])
    for field in df['Nazwa pola'].unique():
        plot_time_series(df, field, 'pH')
