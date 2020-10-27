
import ast
import dash
import dash_core_components as dcc
import dash_html_components as html
import requests

## cargue de estilos y bootstrap
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css', 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([html.Div([], className='col-md-1'),
    html.Div(style={'font-size': '15px'}, children=[  
    html.Div([html.H5('Recomendación de tecnología a instalar en nuevos comercios',style={'textAlign': 'center'})], className='p-1 mb-1 bg-info text-white'), 
    html.Br(),
    html.Div([html.Img(id='imagen',src=app.get_asset_url('logo.png'))], style={'textAlign': 'center'}),
    html.Div([html.Label('''La presente herramienta permite determinar el listado de tecnologías sugeridas
                         a instalar para nuevos comercios a partir de su información geográfica y económica.
                         El objetivo es instalar la primera recomendación, en caso de no ser posible debe instalarse
                         la tecnología de la siguiente recomendación.''')], className='col-md-12 text-justify'),
    html.Br(),
    html.Div([html.Label('''Por favor seleccione las características correspondientes al comercio.
                         En la parte inferior encontrará las recomendaciones''')], className='col-md-12 text-justify'),
    html.Br(),
    html.Div([
    html.Div([html.H5('Actividad económica')], className='col-md-12'),
    html.Div([html.Label('Seleccione la actividad económica del comercio')], className='col-md-12 text-justify'),
    html.Br(),
    html.Div([dcc.Dropdown(placeholder='Seleccione la opción correspondiente', id='opcion1',options=[{'label':'RESTAURANTES', 'value': 'RESTAURANTES'},
                                                           {'label':'TIENDAS DE DEPARTAMENTOS Y ALI', 'value': 'TIENDAS DE DEPARTAMENTOS Y ALI'},{'label':'ELECTRODOMESTICOS Y ELECTRONI', 'value': 'ELECTRODOMESTICOS Y ELECTRONI'},
                                                           {'label':'SERVICIOS PROFESIONALES', 'value': 'SERVICIOS PROFESIONALES'},{'label':'EDUCACION', 'value': 'EDUCACION'},
                                                           {'label':'SERVICIOS DE SALUD', 'value': 'SERVICIOS DE SALUD'},{'label':'DROGUERIAS', 'value': 'DROGUERIAS'},    
                                                           {'label':'CARGA', 'value': 'CARGA'},{'label':'AUTOMOTORES', 'value': 'AUTOMOTORES'}, 
                                                           {'label':'COMERCIO MISCELANEO', 'value': 'COMERCIO MISCELANEO'},{'label':'EVENTOS', 'value': 'EVENTOS'},
                                                           {'label':'HOTELES Y CLUBES SOCIALES', 'value': 'HOTELES Y CLUBES SOCIALES'},{'label':'PAGOS E IMPUESTOS', 'value': 'PAGOS E IMPUESTOS'},
                                                           {'label':'TRANSPORTE DIARIO', 'value': 'TRANSPORTE DIARIO'},{'label':'GRANDES CADENAS MINORISTAS', 'value': 'GRANDES CADENAS MINORISTAS'},
                                                           {'label':'COMUNICACIONES', 'value': 'COMUNICACIONES'},{'label':'ESTACIONES DE COMBUSTIBLE', 'value': 'ESTACIONES DE COMBUSTIBLE'},                                                                                                 
                                                           {'label':'COMIDA RAPIDA', 'value': 'COMIDA RAPIDA'},{'label':'AUTOMOTORES', 'value': 'AUTOMOTORES'}], value=None, style={'textAlign':'center'})], className='col-md-5'),
    html.Br(),
    html.Div([html.H5('Entidad financiera')], className='col-md-12'),
    html.Div([html.Label('Seleccione la actividad financiera del comercio')], className='col-md-12 text-justify'),
    html.Br(),
    html.Div([dcc.Dropdown(placeholder='Seleccione la opción correspondiente', id='opcion2',options=[{'label':'AV Villas', 'value': 'AV Villas'},{'label':'Banco Agrario', 'value': 'Banco Agrario'},
                                                           {'label':'Banco de Bogota', 'value': 'Banco de Bogota'},{'label':'Banco de Occidente', 'value': 'Banco de Occidente'},
                                                           {'label':'Banco Pichincha', 'value': 'Banco Pichincha'},{'label':'Bancolombia', 'value': 'Bancolombia'},
                                                           {'label':'BBVA', 'value': 'BBVA'},{'label':'Colmena', 'value': 'Colmena'},    
                                                           {'label':'Colpatria', 'value': 'Colpatria'},{'label':'Coomeva', 'value': 'Coomeva'}, 
                                                           {'label':'Davivienda', 'value': 'Davivienda'},{'label':'GNB Sudameris', 'value': 'GNB Sudameris'},
                                                           {'label':'Itau', 'value': 'Itau'}], value=None, style={'textAlign':'center'})],className='col-md-5'),
    html.Br(),
    html.Div([html.H5('Zona comercial')], className='col-md-12'),
    html.Div([html.Label('Seleccione la zona comercial del comercio')], className='col-md-12 text-justify'),
    html.Br(),
    html.Div([dcc.Dropdown(placeholder='Seleccione la opción correspondiente', id='opcion3',options=[{'label':'Zona 0', 'value': 'Zona 0'},{'label':'Zona 1', 'value': 'Zona 1'},
                                                           {'label':'Zona 2', 'value': 'Zona 2'},{'label':'Zona 3', 'value': 'Zona 3'},
                                                           {'label':'Zona 4', 'value': 'Zona 4'},{'label':'Zona 5', 'value': 'Zona 5'},
                                                           {'label':'Zona 6', 'value': 'Zona 6'},{'label':'Zona 7', 'value': 'Zona 7'},    
                                                           {'label':'Zona 8', 'value': 'Zona 8'},{'label':'Sin asignar', 'value': 'Sin asignar'}], value=None, style={'textAlign':'center'})],className='col-md-5'),
    html.Br(),
    html.Div([html.H5('Zona técnica')], className='col-md-12'),
    html.Div([html.Label('Seleccione la zona técnica del comercio')], className='col-md-12 text-justify'),
    html.Br(),
    html.Div([dcc.Dropdown(placeholder='Seleccione la opción correspondiente', id='opcion4',options=[{'label':'Zona 0', 'value': 'Zona 0'},{'label':'Zona 1', 'value': 'Zona 1'},
                                                           {'label':'Zona 2', 'value': 'Zona 2'},{'label':'Zona 3', 'value': 'Zona 3'},
                                                           {'label':'Zona 4', 'value': 'Zona 4'},{'label':'Zona 5', 'value': 'Zona 5'},
                                                           {'label':'Zona 6', 'value': 'Zona 6'},{'label':'Zona 7', 'value': 'Zona 7'},    
                                                           {'label':'Zona 8', 'value': 'Zona 8'},{'label':'Zona 9', 'value': 'Zona 9'},
                                                           {'label':'Zona 11', 'value': 'Zona 11'},{'label':'No definida', 'value': 'No definida'}], value=None, style={'textAlign':'center'})],className='col-md-5'),
    html.Br(),
    html.Div([html.Button('Limpiar Campos',id='boton2', n_clicks=0, style={'font-size': '13px'}, className='col-md-2 btn btn-info')], className='row align-items-center justify-content-center'),
    html.Br(),
    html.Div([html.Button('Enviar información',id='boton', n_clicks=0, disabled=True, style={'font-size': '13px'}, className='col-md-2 btn btn-info')], className='row align-items-center justify-content-center'),
    html.Br(),
    html.B(html.Div('Tecnologías recomendadas para el comercio', id='respuesta', style={'textAlign': 'center'})),
    html.Div(id='mensaje', style={'textAlign': 'center'}),
    html.Br()
])], className='col-md-9')], className='row')

## habilitar boton envio
@app.callback(
    dash.dependencies.Output(component_id='boton', component_property='disabled'),
    [dash.dependencies.Input('opcion1', 'value'),
     dash.dependencies.Input('opcion2', 'value'),
     dash.dependencies.Input('opcion3', 'value'),
     dash.dependencies.Input('opcion4', 'value')])
def envio(value1,value2,value3,value4):
    if value1 == "" or value2 == "" or value3 == "" or value4 == "" or value1 is None or value2 is None or value3 is None or value4 is None:
        return True

ind = 0

## habilitar mensaje respuesta
@app.callback(
    dash.dependencies.Output(component_id='mensaje', component_property='children'),
    [dash.dependencies.Input(component_id='boton', component_property='n_clicks'),
     dash.dependencies.Input('opcion1', 'value'),
     dash.dependencies.Input('opcion2', 'value'),
     dash.dependencies.Input('opcion3', 'value'),
     dash.dependencies.Input('opcion4', 'value')])
def mensaje(n_clicks,value1,value2,value3,value4):
    global ind
    if n_clicks > ind:   
        url = "http://3.137.205.27:5000//rec-disp/"
        parametros = {'actividad':value1, 'entidad_fin':value2, 'zona_com':value3, 'zona_tec':value4}
        req = requests.get(url = url, params = parametros)
        data = req.json()
        data = dict(data)
        rec1 = data['respuesta']
        rec1 = ast.literal_eval(rec1)[0]
        rec2 = data['respuesta']
        rec2 = ast.literal_eval(rec2)[1]
        ind+=1
        return 'Recomendación 1: {recom1}. Recomendación 2: {recom2}'.format(recom1=rec1,recom2=rec2)
    else:    
        return 'Seleccione la información correspondiente'
    
## eliminar valores de opciones
@app.callback(
    dash.dependencies.Output(component_id='opcion1', component_property='value'),
    [dash.dependencies.Input(component_id='boton2', component_property='n_clicks')])
def opcion1(n_clicks):
    if n_clicks > 0:
       return ""
@app.callback(
    dash.dependencies.Output(component_id='opcion2', component_property='value'),
    [dash.dependencies.Input(component_id='boton2', component_property='n_clicks')])
def opcion2(n_clicks):
    if n_clicks > 0:
       return ""
@app.callback(
    dash.dependencies.Output(component_id='opcion3', component_property='value'),
    [dash.dependencies.Input(component_id='boton2', component_property='n_clicks')])
def opcion3(n_clicks):
    if n_clicks > 0:
       return ""
@app.callback(
    dash.dependencies.Output(component_id='opcion4', component_property='value'),
    [dash.dependencies.Input(component_id='boton2', component_property='n_clicks')])
def opcion4(n_clicks):
    if n_clicks > 0:
       return ""

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
