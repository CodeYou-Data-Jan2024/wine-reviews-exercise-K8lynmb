import pandas as pd

df = pd.read_csv('data/winemag-data-130k-v2.csv')

country_summary = df.groupby('country').agg(
    count=('country', 'size'),
    points=('points', 'mean')
).reset_index()

country_summary['points'] = country_summary['points'].round(1)

country_summary.to_csv('data/reviews-per-country.csv', index=False)
