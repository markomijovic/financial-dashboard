### Dependencies ###
import json
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from urllib.request import urlopen
import plotly.graph_objects as gobj
### Main Dash HTML ###
app = dash.Dash()
app.layout = html.Div([
    html.H1('Financial Dashboard'),
    html.Div([
        dcc.Input(id='company'),
        html.H3(id='text'),
        dcc.Graph(id='revenue'),
        dcc.Graph(id='netincome'),
        dcc.Graph(id="ebitdaratio"),
        dcc.Graph(id="epsdiluted")
    ])
])
### Data Gathering and Processing ###

### REVENUE ###
@app.callback(Output('revenue', 'figure'),
              [Input('company', 'value')]
)
def get_revenue(company):
    apikey = "demo" #17ffa068079c34a13bc371458bc7dc91
    statement = get_jsonparsed_data(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?apikey={apikey}")
    revenues = []
    years = []
    for item in statement:
        revenues.append(float(item['revenue']))
        years.append(int(item['date'][0:4]))
    datapts = {"data": [gobj.Bar(x=years, y=revenues)], 
               "layout": dict(
                   xaxis={'title': 'Year'},
                   yaxis={'title': 'Annual Revenue (USD)'}
        )
    }
    return datapts

### Net Income ###
@app.callback(Output('netincome', 'figure'),
              [Input('company', 'value')]
)
def get_netIncome(company):
    apikey = "demo" #17ffa068079c34a13bc371458bc7dc91
    statement = get_jsonparsed_data(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?apikey={apikey}")
    netIncome = []
    years = []
    for item in statement:
        netIncome.append(float(item['netIncome']))
        years.append(int(item['date'][0:4]))
    datapts = {"data": [gobj.Bar(x=years, y=netIncome)], 
               "layout": dict(
                   xaxis={'title': 'Year'},
                   yaxis={'title': 'Net Income (USD)'}
        )
    }
    return datapts

### EBITDARATIO ###
@app.callback(Output('ebitdaratio', 'figure'),
              [Input('company', 'value')]
)
def get_ebitdaRatio(company):
    apikey = "demo" #17ffa068079c34a13bc371458bc7dc91
    statement = get_jsonparsed_data(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?apikey={apikey}")
    ebitdaRatio = []
    years = []
    for item in statement:
        ebitdaRatio.append(float(item['ebitdaratio']))
        years.append(int(item['date'][0:4]))
    datapts = {"data": [gobj.Bar(x=years, y=ebitdaRatio)], 
               "layout": dict(
                   xaxis={'title': 'Year'},
                   yaxis={'title': 'EBITDA Ratio'}
        )
    }
    return datapts

### Net Income ###
@app.callback(Output('epsdiluted', 'figure'),
              [Input('company', 'value')]
)
def get_epsDiluted(company):
    apikey = "demo" #17ffa068079c34a13bc371458bc7dc91
    statement = get_jsonparsed_data(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?apikey={apikey}")
    epsDiluted = []
    years = []
    for item in statement:
        epsDiluted.append(float(item['epsdiluted']))
        years.append(int(item['date'][0:4]))
    datapts = {"data": [gobj.Bar(x=years, y=epsDiluted)], 
               "layout": dict(
                   xaxis={'title': 'Year'},
                   yaxis={'title': 'EPS Diluted (USD)'}
        )
    }
    return datapts

def get_jsonparsed_data(url):
    reponse = urlopen(url)
    data = reponse.read().decode("utf-8")
    return json.loads(data)

if __name__ == "__main__":
    app.run_server()