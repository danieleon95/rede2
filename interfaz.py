
import ast
import dash
import dash_core_components as dcc
import dash_html_components as html
import requests

## cargue de estilos y bootstrap
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css', 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([html.Div([], className='col-md-1'),
    html.Div(style={'font-size': '15px'}, children=[  
    html.Div([html.H5('Recomendación de tecnología a instalar en nuevos comercios',style={'textAlign': 'center'})], className='p-1 mb-1 bg-info text-white'), 
    html.Br(),
    html.Div([html.Label('''La presente herramienta permite determinar el listado de tecnologías sugeridas
                         a instalar para nuevos comercios a partir de su información geográfica y económica.
                         El objetivo es instalar la primera recomendación, en caso de no ser posible debe instalarse
                         la tecnología de la siguiente recomendación.''')], className='col-md-12 text-justify'),
    html.Br(),
    html.Div([html.Label('''Por favor seleccione las características correspondientes al comercio.
                         En la parte inferior encontrará las recomendaciones''')], className='col-md-12 text-justify'),
    html.Br(),
    html.Div([
    html.Div([html.H5('Tipo de comercio')], className='col-md-12'),
    html.Div([html.Label('Seleccione el tipo de comercio')], className='col-md-12 text-justify'),
    html.Div([dcc.Dropdown(placeholder='Seleccione la opción correspondiente', id='opcion1',
                           options=[{'label':'Corresp Bancarios','value':'Corresp Bancarios'},{'label':'Entidades Bancarias','value':'Entidades Bancarias'},{'label':'Incocredito','value':'Incocredito'},
                                    {'label':'Internacional','value':'Internacional'},{'label':'RBM','value':'RBM'},{'label':'Tarjeta Privada','value':'Tarjeta Privada'}],
                           value=None, style={'textAlign':'center'})], className='col-md-5'),
    html.Br(),
    html.Div([html.H5('Zona comercial')], className='col-md-12'),
    html.Div([html.Label('Seleccione la zona comercial')], className='col-md-12 text-justify'),
    html.Div([dcc.Dropdown(placeholder='Seleccione la opción correspondiente', id='opcion2',
                           options=[{'label':'ZONA COMERCIAL 0','value':'ZONA COMERCIAL 0'},{'label':'ZONA COMERCIAL 1','value':'ZONA COMERCIAL 1'},{'label':'ZONA COMERCIAL 2','value':'ZONA COMERCIAL 2'},
                                    {'label':'ZONA COMERCIAL 3','value':'ZONA COMERCIAL 3'},{'label':'ZONA COMERCIAL 4','value':'ZONA COMERCIAL 4'},{'label':'ZONA COMERCIAL 5','value':'ZONA COMERCIAL 5'},
                                    {'label':'ZONA COMERCIAL 6','value':'ZONA COMERCIAL 6'},{'label':'ZONA COMERCIAL 7','value':'ZONA COMERCIAL 7'},{'label':'ZONA COMERCIAL 8','value':'ZONA COMERCIAL 8'}],
                           value=None, style={'textAlign':'center'})], className='col-md-5'),
    html.Br(),
    html.Div([html.H5('Zona técnica')], className='col-md-12'),
    html.Div([html.Label('Seleccione la zona técnica')], className='col-md-12 text-justify'),
    html.Div([dcc.Dropdown(placeholder='Seleccione la opción correspondiente', id='opcion3',
                           options=[{'label':'ZONA TECNICA 0','value':'ZONA TECNICA 0'},{'label':'ZONA TECNICA 1','value':'ZONA TECNICA 1'},{'label':'ZONA TECNICA 2','value':'ZONA TECNICA 2'},
                                    {'label':'ZONA TECNICA 3','value':'ZONA TECNICA 3'},{'label':'ZONA TECNICA 5','value':'ZONA TECNICA 5'},{'label':'ZONA TECNICA 6','value':'ZONA TECNICA 6'},
                                    {'label':'ZONA TECNICA 7','value':'ZONA TECNICA 7'},{'label':'ZONA TECNICA 8','value':'ZONA TECNICA 8'},{'label':'ZONA TECNICA 11','value':'ZONA TECNICA 11'}],
                           value=None, style={'textAlign':'center'})], className='col-md-5'),
    html.Br(),
    html.Div([html.H5('Entidad financiera')], className='col-md-12'),
    html.Div([html.Label('Seleccione la entidad financiera del comercio')], className='col-md-12 text-justify'),
    html.Div([dcc.Dropdown(placeholder='Seleccione la opción correspondiente', id='opcion4',
                           options=[{'label':'AVVILLAS','value':'AVVILLAS                                          '},{'label':'BANCO AGRARIO','value':'BANCO AGRARIO                                     '},{'label':'BANCO DE BOGOTA','value':'BANCO DE BOGOTA                                   '},
                                    {'label':'BANCO DE OCCIDENTE','value':'BANCO DE OCCIDENTE                                '},{'label':'BANCO PICHINCHA','value':'BANCO PICHINCHA                                   '},{'label':'BANCOLOMBIA','value':'BANCOLOMBIA                                       '},
                                    {'label':'BBVA','value':'BBVA                                              '},{'label':'COLMENA','value':'COLMENA                                           '},{'label':'COLPATRIA','value':'COLPATRIA                                         '},
                                    {'label':'DAVIVIENDA','value':'DAVIVIENDA 0051                                   '},{'label':'GNB SUDAMERIS S.A.','value':'GNB SUDAMERIS S.A.                                '},{'label':'ITAU','value':'ITAU                                              '},
                                    {'label':'NO APLICA','value':'No_Aplica'},{'label':'TEMPORARL SIN ADQUIRIENTE','value':'TEMPORARL SIN ADQUIRIENTE                         '}],
                           value=None, style={'textAlign':'center'})], className='col-md-5'),
    html.Br(),
    html.Div([html.H5('Tipo afiliación')], className='col-md-12'),
    html.Div([html.Label('Seleccione el tipo de afiliación del comercio')], className='col-md-12 text-justify'),
    html.Div([dcc.Dropdown(placeholder='Seleccione la opción correspondiente', id='opcion5',
                           options=[{'label':'Asesor Comercial','value':'Asesor Comercial'},{'label':'Entidad Emisora','value':'Entidad Emisora'}],
                           value=None, style={'textAlign':'center'})], className='col-md-5'),
    html.Br(),
    html.Div([html.H5('Actividad consolidada')], className='col-md-12'),
    html.Div([html.Label('Seleccione la actividad económica consolidada del comercio')], className='col-md-12 text-justify'),
    html.Div([dcc.Dropdown(placeholder='Seleccione la opción correspondiente', id='opcion6',
                           options=[{'label':'AEROLINEAS', 'value': 'AEROLINEAS'},{'label':'AGENCIAS DE VIAJE', 'value': 'AGENCIAS DE VIAJE'},{'label':'AUTOMOTORES', 'value': 'AUTOMOTORES'},
                                    {'label':'BENEFICENCIAS', 'value': 'BENEFICENCIAS'},{'label':'CADENAS MINORISTAS', 'value': 'CADENAS MINORISTAS'},{'label':'CARGA, SERVICIO  DE MENSAJERÍA', 'value': 'CARGA, SERVICIO  DE MENSAJERA'},
                                    {'label':'COMERCIO MISCELANEO', 'value': 'COMERCIO MISCELANEO--TODOS  LO'},{'label':'COMIDA RAPIDA', 'value': 'COMIDA RAPIDA'},{'label':'COMUNICACIONES', 'value': 'COMUNICACIONES'},
                                    {'label':'DROGUERIAS', 'value': 'DROGUERIAS'},{'label':'EDUCACION', 'value': 'EDUCACION'},{'label':'ELECTRODOMESTICOS Y ELECTRONI', 'value': 'ELECTRODOMESTICOS Y ELECTRONI'},
                                    {'label':'ESTACIONES DE COMBUSTIBLE', 'value': 'ESTACIONES DE COMBUSTIBLE'},{'label':'EVENTOS', 'value': 'EVENTOS'},{'label':'GRANDES CADENAS MINORISTAS', 'value': 'GRANDES CADENAS MINORISTAS'},
                                    {'label':'HOTELES Y CLUBES SOCIALES', 'value': 'HOTELES Y CLUBES SOCIALES'},{'label':'KIOSKOS', 'value': 'KIOSKOS'},{'label':'MERCADEO DIRECTO', 'value': 'MERCADEO DIRECTO'},
                                    {'label':'PAGOS E IMPUESTOS', 'value': 'PAGOS E IMPUESTOS'},{'label':'PAGOS PERSONALES', 'value': 'PAGOS PERSONALES'},{'label':'RESTAURANTES', 'value': 'RESTAURANTES'},
                                    {'label':'SERVICIOS DE SALUD', 'value': 'SERVICIOS DE SALUD'},{'label':'SERVICIOS PROFESIONALES', 'value': 'SERVICIOS PROFESIONALES'},{'label':'TIENDAS DE DEPARTAMENTOS Y ALI', 'value': 'TIENDAS DE DEPARTAMENTOS Y ALI'},
                                    {'label':'TRANSPORTE DIARIO', 'value': 'TRANSPORTE DIARIO'},{'label':'VENTAS MINORISTAS GENERALES', 'value': 'VENTAS  MINORISTAS GENERALES'}],value=None, style={'textAlign':'center'})], className='col-md-5'),
    html.Br(),
    html.Div([html.H5('MCC normal')], className='col-md-12'),
    html.Div([html.Label('Seleccione el Código de categoría mercante correspondiente al comercio')], className='col-md-12 text-justify'),
    html.Div([dcc.Dropdown(placeholder='Seleccione la opción correspondiente', id='opcion7',
                           options=[{'label':'ABOGADOS, SERVICIOS JURIDICOS','value':'ABOGADOS, SERVICIOS JURIDICOS'},{'label':'ACCESORIOS DE COSTURA','value':'ACCESORIOS DE COSTURA'},{'label':'ACCESORIOS DEPORTIVOS','value':'ACCESORIOS DEPORTIVOS'},
                                    {'label':'ACCESORIOS FOTOGRAFIAS','value':'ACCESORIOS FOTOGRAFIAS'},{'label':'AG MUDANZAS Y BODEGA','value':'AG MUDANZAS Y BODEGA'},{'label':'AGENCIAS DE VIAJE Y OPERADORES TURISTICOS','value':'AGENCIAS DE VIAJE Y OPERADORES TURISTICOS'},
                                    {'label':'AGENTES Y ADMINISTRADORES DE BIENES RAICES','value':'AGENTES Y ADMINISTRADORES DE BIENES RAICES ALQUILE'},{'label':'ALARMAS Y SEGURIDAD','value':'ALARMAS Y SEGURIDAD'},{'label':'ALM X DPTO CON SUPERMERCADO','value':'ALM X DPTO CON SUPERMERCADO'},
                                    {'label':'ALM X DPTO SIN SUPERMERCADO','value':'ALM X DPTO SIN SUPERMERCADO'},{'label':'ALMACENES DE CALZADO Y REMONTADORAS','value':'ALMACENES DE CALZADO Y REMONTADORAS'},{'label':'ALMACENES DE DISCOS','value':'ALMACENES DE DISCOS'}],
                           value=None, style={'textAlign':'center'})], className='col-md-5'),
    html.Br(), 
    html.Div([html.H5('Latitud ubicación')], className='col-md-12'),
    html.Div([html.Label('Ingrese la latitud de la ubicación del comercio')], className='col-md-12 text-justify'),
    html.Br(),
    html.Div([dcc.Input(placeholder='Ingrese la información correspondiente',id='opcion8',type="number",style={'font-size': '15px'}, className='col-md-4 text-center')]),
    html.Br(),
    html.Div([html.H5('Longitud ubicación')], className='col-md-12'),
    html.Div([html.Label('Ingrese la longitud de la ubicación del comercio')], className='col-md-12 text-justify'),
    html.Br(),
    html.Div([dcc.Input(placeholder='Ingrese la información correspondiente',id='opcion9',type="number",style={'font-size': '15px'}, className='col-md-4 text-center')]),
    html.Br(),
    html.Br(),
    html.Div([html.Button('Limpiar Campos',id='boton2', n_clicks=0, style={'font-size': '13px'}, className='col-md-2 btn btn-info')], className='row align-items-center justify-content-center'),
    html.Br(),
    html.Div([html.Button('Enviar información',id='boton', n_clicks=0, disabled=True, style={'font-size': '13px'}, className='col-md-2 btn btn-info')], className='row align-items-center justify-content-center'),
    html.Br(),
    html.Br(),
    html.B(html.Div(html.H5('Tecnologías recomendadas para el comercio', id='respuesta', style={'textAlign': 'center'}))),
    html.Br(),    
    html.Div(id='mensaje', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Br(),
    html.B(html.Div('Redeban Multicolor - Proyecto Trabajo de Grado - Universidad de los Andes - 2020', style={'textAlign': 'center'})),    
])], className='col-md-9')], className='row')

## habilitar boton envio
@app.callback(
    dash.dependencies.Output(component_id='boton', component_property='disabled'),
    [dash.dependencies.Input('opcion1', 'value'),
     dash.dependencies.Input('opcion2', 'value'),
     dash.dependencies.Input('opcion3', 'value'),
     dash.dependencies.Input('opcion4', 'value'),
     dash.dependencies.Input('opcion5', 'value'),
     dash.dependencies.Input('opcion6', 'value'),
     dash.dependencies.Input('opcion7', 'value'),
     dash.dependencies.Input('opcion8', 'value'),
     dash.dependencies.Input('opcion9', 'value'),])
def envio(value1,value2,value3,value4,value5,value6,value7,value8,value9):
    if value1 == "" or value2 == "" or value3 == "" or value4 == "" or value5 == "" or value6 == "" or value7 == "" or value8 == "" or value9 == "" or value1 is None or value2 is None or value3 is None or value4 is None or value5 is None or value6 is None or value7 is None or value8 is None or value9 is None:
        return True

ind = 0

## habilitar mensaje respuesta
@app.callback(
    dash.dependencies.Output(component_id='mensaje', component_property='children'),
    [dash.dependencies.Input(component_id='boton', component_property='n_clicks'),
     dash.dependencies.Input('opcion1', 'value'),
     dash.dependencies.Input('opcion2', 'value'),
     dash.dependencies.Input('opcion3', 'value'),
     dash.dependencies.Input('opcion4', 'value'),
     dash.dependencies.Input('opcion5', 'value'),
     dash.dependencies.Input('opcion6', 'value'),
     dash.dependencies.Input('opcion7', 'value'),
     dash.dependencies.Input('opcion8', 'value'),
     dash.dependencies.Input('opcion9', 'value'),])
def mensaje(n_clicks,value1,value2,value3,value4,value5,value6,value7,value8,value9):
    global ind
    if n_clicks > ind:   
        url = "http://18.224.165.114:5000/rec_disp/"
        parametros = {'tipo_comercio':value1, 'zona_comercial':value2, 'zona_tecnica':value3, 'entidad_financiera':value4,
                      'tipo_afiliacion':value5, 'actividad_consolidada':value6, 'mcc_normal':value7, 'longitud_ubicacion':value8, 'latitud_ubicacion':value9}
        req = requests.get(url = url, params = parametros)
        data = req.json()
        data = ast.literal_eval(data['respuesta'])['lista']
        rec1_disp = data[0][0]
        rec1_proba = round(data[0][1],2)
        rec2_disp = data[1][0]
        rec2_proba = round(data[1][1],2)
        rec3_disp = data[2][0]
        rec3_proba = round(data[2][1],2)        
        ind+=1
        return """Recomendación 1: {rec1_disp}. Prob: {rec1_proba}. Recomendación 2: {rec2_disp}. Prob: {rec2_proba}. Recomendación 3: {rec3_disp}. Prob: {rec3_proba}.""".format(rec1_disp=rec1_disp,rec1_proba=rec1_proba,
                                                                                                                                                                                                          rec2_disp=rec2_disp,rec2_proba=rec2_proba,
                                                                                                                                                                                                          rec3_disp=rec3_disp,rec3_proba=rec3_proba)
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
@app.callback(
    dash.dependencies.Output(component_id='opcion5', component_property='value'),
    [dash.dependencies.Input(component_id='boton2', component_property='n_clicks')])
def opcion5(n_clicks):
    if n_clicks > 0:
       return ""
@app.callback(
    dash.dependencies.Output(component_id='opcion6', component_property='value'),
    [dash.dependencies.Input(component_id='boton2', component_property='n_clicks')])
def opcion6(n_clicks):
    if n_clicks > 0:
       return ""  
@app.callback(
    dash.dependencies.Output(component_id='opcion7', component_property='value'),
    [dash.dependencies.Input(component_id='boton2', component_property='n_clicks')])
def opcion7(n_clicks):
    if n_clicks > 0:
       return "" 
@app.callback(
    dash.dependencies.Output(component_id='opcion8', component_property='value'),
    [dash.dependencies.Input(component_id='boton2', component_property='n_clicks')])
def opcion8(n_clicks):
    if n_clicks > 0:
       return ""
@app.callback(
    dash.dependencies.Output(component_id='opcion9', component_property='value'),
    [dash.dependencies.Input(component_id='boton2', component_property='n_clicks')])
def opcion9(n_clicks):
    if n_clicks > 0:
       return ""
   
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
