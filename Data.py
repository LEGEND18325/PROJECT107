import pandas as p
import csv
from pandas.core import groupby

import plotly_express as px

fileName = p.read_csv('StudentData.csv')



grouping=fileName.groupby(["student_id",'level'],as_index=False)['attempt'].mean()

graph=px.scatter(
    grouping,
    x='student_id',
    y='level',
    size='attempt',
    color='attempt'
    
)

print(grouping)

graph.show()
