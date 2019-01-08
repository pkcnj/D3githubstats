import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Bar(
    x=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
    y=[3, 9, 9, 6, 12, 7, 2]
)

data = [trace0]
layout = go.Layout(
    title='d3 Github Repository: Commits per day, past year ending December 8, 2018',
)

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename = 'basic-bar', auto_open=True)