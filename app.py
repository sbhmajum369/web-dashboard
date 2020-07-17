
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table

df = pd.read_excel(r'Live Data.xlsx', sheet_name='Sheet6')
Col1=df.columns[0]
Col2=df.columns[1]
Col3=df.columns[2]
Col4=df.columns[3]

fig = px.bar(df, x=Col1, y=[Col2,Col3,Col4], barmode="group")
# fig.show()
df2 = pd.read_excel(r'Live Data.xlsx', sheet_name='Sheet7')

app = dash.Dash(__name__)
server=app.server

app.layout = html.Div(style={
	'background-image': 'url("/assets/covid.jpeg")',
	'background-size': '1500px 800px'
	},children=[
	html.H1(
		children='COVID-19 Dashboard',
		style={
		'textAlign':'center',
		'color':'white'
		}
	),
	html.Div([	# Body
		html.Div([
			html.H2(
				'Canada Cases',
				style={
				'textAlign':'center'
				}
			),
			dash_table.DataTable( #style_cell = {'backgroundColor': 'orange','fontFamily': 'cursive'}
				id='table',
				columns=[{"name": i, "id": i} for i in df2.columns],
				data=df2.to_dict('records'),
				style_cell={'fontSize':'20px','textAlign': 'left','width':'33%','height': '60px'},
				style_header={
				'backgroundColor': 'white',
				'fontWeight': 'bold',
				'height': '40px'
				}
				)],style={'backgroundColor': 'white','width': '80%','float': 'right'}
			),
		html.Div([
			html.H3(
				'Canada Provincial Data',
				style={
				'textAlign':'center'
				}
			),
			dcc.Graph(
				id='Graph1',
				figure=fig)
			], style={'backgroundColor': 'white','width': '80%','float': 'right','display': 'inline-block'}
			)
		],style={'width': '80%','float': 'center','display': 'inline-block'}),
	])


if __name__ == '__main__':
	app.run_server(port=8090,debug=True)

