# You want to quickly look up temperature readings by country and city,
# and you want the results sorted in a sensible order.
import pandas as pd

temperatures = pd.DataFrame({
    "city": ["Moscow", "Moscow", "Cairo", "Cairo", "Cairo", "Delhi", "Delhi"],
    "country": ["Russia", "Russia", "Egypt", "Egypt", "Egypt", "India", "India"],
    "date": ["2013-01-01", "2013-02-01", "2013-01-01", "2013-02-01", "2013-03-01", "2013-01-01", "2013-02-01"],
    "avg_temp_c": [-7.2, -3.1, 14.7, 16.9, 20.3, 14.0, 17.5]
})

temperatures_index = temperatures.set_index(['city','country']).sort_index(ascending=[True,False])

print(temperatures_index)