import pandas as pd

CSV_URL="https://docs.google.com/spreadsheets/d/e/2PACX-1vQkcAXziIREjBPcuVUzQIMhDJZE6cS1nIBiDx-5towy7_gWqWbs9GYdB-2SGAbba6fTeZQu_o-9GnYs/pub?output=csv"

def docLich():
  df=pd.read_csv(CSV_URL)
  print(df.head())
docLich()

