import pandas as pd 
import plotly_express as px 

df = pd.read_csv("data.csv")
student_df = df.loc[df["student_id"]== "TRL_xyz"]

# showing bar graph using plotly express
fig = px.scatter(
    x = student_df.groupby("level")["attempt"].mean(),
    y = ["Level 1","Level 2","Level 3","Level 4"]
)
fig.show()

