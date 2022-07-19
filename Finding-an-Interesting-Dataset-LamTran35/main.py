import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

top_albums = pandas.read_csv("Top5000.csv")

print(top_albums)