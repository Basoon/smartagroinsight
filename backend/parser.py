import pandas as pd

def load_and_prepare(path):
    df = pd.read_csv(path, parse_dates=['Data'], dayfirst=True, infer_datetime_format=True)
    df.rename(columns={'Nazwa pola': 'field_name', 'Lokalizacja': 'location'}, inplace=True)
    return df

def group_by_field_and_date(df):
    return df.groupby(['field_name', 'Data'])

if __name__ == '__main__':
    df = load_and_prepare('../data/smartagro_dane_laboratoryjne.csv')
    groups = group_by_field_and_date(df)
    print(f"Found {len(groups)} groups.")
