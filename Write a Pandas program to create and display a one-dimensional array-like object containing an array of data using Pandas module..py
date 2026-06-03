# Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using Pandas module.
import pandas as pd
data = [18,45,7,33,17,333]
series = pd.Series(data)
print(series)
# Write a Pandas program to convert a Pandas Series to Python list and its type
import pandas as pd
data = [18,97,38,61,6,15]
series = pd.Series(data)
list_data = series.tolist()
print(list_data)
print(type(list_data))
