# Data structure and analizing


# Using Pandas to read a file and use it
# go to https://kaggle.com and downlode any data file with extention like .csv, .xml, etc
# I have some allready downloaded 
# You can also use the file

# Uses of Pandas
# Panda is mainly used for taking data from file to code
# You can see in file there is Data-1.csv and I am going to use this in this code

# Installation of Pandas
# open terminal or cmd and run `pip install pandas` if not then use `sudo` for mac and `yarn` for Windows before `pip install pandas`
# Once it is installed then follow the code given below

import pandas as pd

a=pd.read_csv('./Data-1.csv')
print(a) # Output will be seen in terminal or Output log



# Making a graph using plotly.express
# Plotly.express is used only for data representation

# Installation of Plotly.express
#open terminal or cmd and run `pip install Plotly.express` if not then use `sudo` for mac and `yarn` for Windows before `pip install Plotly.express`

import pandas as pd
import plotly.express as px

df = pd.read_csv('./Data-1.csv')

# Making a bar graph of data-1.csv files.
fig1=px.bar(df, x="Coffee in ml", y="sleep in hours")           # px.bar(variable, x='cordinate', y='cordinate') this is used for making a bar graph
fig1.show()     # .show is used for making a print of graph.

# Making a scatter graph of data-1.csv files.
fig2 = px.scatter(df, x="Coffee in ml", y="sleep in hours")     # px.scatter(variable, x='cordinate', y='cordinate') this is used for making a scatter graph
fig2.show()

# Making a line graph of data-1.csv files.
fig3=px.line(df, x="week", y="sleep in hours", color="Coffee in ml")        # px.line(variable, x='cordinate', y='cordinate', color='cordinate') this is used for making a line graph
fig3.show()







