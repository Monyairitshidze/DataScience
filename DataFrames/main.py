# You're a data analyst at a retail chain with three stores. 
# Management wants a report that lets them look up performance by store and department without scanning through raw rows,
# see which departments beat their monthly revenue targets, and view results ordered in a way that 
# highlights the best-performing store first, 
# with departments neatly grouped underneath.
import pandas as pd

sales = pd.DataFrame({
    "store": ["A", "A", "A", "B", "B", "B", "C", "C", "C"],
    "department": ["Electronics", "Clothing", "Toys", "Electronics", "Clothing", "Toys", "Electronics", "Clothing", "Toys"],
    "month": ["Jan", "Feb", "Mar", "Jan", "Feb", "Mar", "Jan", "Feb", "Mar"],
    "revenue": [15200, 8700, 4300, 12100, 9600, 5100, 17800, 7200, 3900],
    "target": [14000, 9000, 5000, 13000, 9000, 5000, 16000, 8000, 4000]
})

sales['beat_target'] = sales['revenue'] > sales['target']

sales_ind = sales.set_index(['store', 'department'])
sales_sorted = sales_ind.sort_index()

winners = sales[sales['beat_target']]

print(sales_sorted)
print(winners)


