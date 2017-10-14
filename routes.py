#-*- coding:utf-8 -*-

"""
Routes and views for the bottle application.
"""
 

from hotelhurbano import buscahoteis
from hotelhurbano.buscahoteis import to_dict
from bottle import route, view, response, request
from datetime import datetime
import json




@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )



@route('/service/cidades')
def getcidades():

    """PEGANDO TODA AS CIDADES """



    cidade =  buscahoteis.getCidades('artefatos/hoteis.csv')

    response.content_type = 'application/json'
    return json.dumps(to_dict(cidade))






@route('/service/get-hoteis/')
def gethoteis():

    """PESQUISANDO TODOS OS HOTEIS PELA CIDADE """

    term =  request.query['term'] 

    list_hoteis =  buscahoteis.getList('artefatos/hoteis.csv')

    result_search = buscahoteis.searchHotel(term,list_hoteis)

    response.content_type = 'application/json'
 
    return json.dumps(to_dict(result_search))





@route('/service/get-disponibilidade/')
def getdisponibilidade():

    """ PESQUISANDO AS DISPONIBILIDADE DOS  HOTEIS """

    # pegando os parametro
    idhotel = int(request.query['idhotel'])
    data_inicio = (request.query['data_inicio'])
    data_fim = (request.query['data_fim'])
    todos =  request.query['todos'] 

    # argumentos para a consulta

    args = [idhotel,data_inicio,data_fim,todos ]

    dis_list  =  buscahoteis.getListDisp('artefatos/disponibilidade.csv')

    result_search = buscahoteis.searchDips(args, dis_list)


    response.content_type = 'application/json'
   
    return json.dumps(to_dict(result_search))
