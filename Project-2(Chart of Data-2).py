import pandas as pd
import plotly.express as px

df=pd.read_csv('./Data-2.csv')
print(df)

fig=px.line(df, x='Year', y='Per capita income', color='Country')
fig.show()

fig2=px.bar(df, x='Year', y='Per capita income', color='Country')
fig2.show()

fig3=px.scatter(df, x='Year', y='Per capita income', color='Country')
fig3.show()

exit()