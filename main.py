from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)


df = pd.read_excel("Vendas.xlsx")

fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")

# Lista de opções para o Dropdown
opcoes = list(df['ID Loja'].unique())
opcoes.append('Todas as Lojas')

app.layout = html.Div(children=[
    html.H1(children='Faturamento das Lojas'),

    html.Div(children='''
        Gráfico com Faturamento de Todos os Produtos separados por loja
    '''),

    html.Div(id='Texto'),  

    dcc.Dropdown(
        options=[{'label': loja, 'value': loja} for loja in opcoes],
        value='Todas as Lojas',
        id='lista-de-lojas'
    ),

    dcc.Graph(
        id='Gráfico Quantidade Vendas',
        figure=fig
    )
])

# callback
@app.callback(
    Output('Gráfico Quantidade Vendas', 'figure'),  
    Input('lista-de-lojas', 'value')
)
def update_output(value):
    if value == "Todas as Lojas":  
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df['ID Loja'] == value, :]  
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig
if __name__ == '__main__':
    app.run_server(debug=True)
