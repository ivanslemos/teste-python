import csv

from builtins import int
from hotelhurbano.hotel import hotel
from hotelhurbano.cidade import cidade
from hotelhurbano.disponibilidade import disponibilidade
from datetime import datetime

def getCidades(path):


    """LENDO O ARQUIVO DE HOTEIS E RETORNANDO UMA LISTA"""
    try:
        list = []

        registros = csv.reader(open(path), delimiter=',')

        for [id, cid, nome] in registros:
            item_hotel = hotel(id,cid,nome)
            if len(list) == 0:
                list.append(item_hotel)
            else:
                if cidadeInList(item_hotel, list) == False :
                    list.append(hotel(int(id), cid, nome))


        return list

    except Exception as  e:
        print('Erro ao buscar os hoteis no csv  ' + str(e))
        return list



def getList(path):

    """LENDO O ARQUIVO DE HOTEIS E RETORNANDO UMA LISTA"""
    try:
        list = []
        arquivo = open(path,'r')
        registros = csv.reader(arquivo, delimiter=',')

        for [id, cid, nome] in registros:
            item_hotel = hotel(int(id), cid, nome)
            list.append(item_hotel)

        return list

    except Exception as  e:
        print('Erro ao buscar os hoteis no csv  ' + str(e))
        return list


def searchDips(arg = [], list_disp = []):

    """ BUSCANDO AS DISPONIBILIDADES DE ARCODO COM OS ARGUMENTOS """

    list = []
    try:
        if  arg[3] == 'true' : #se o usuário selecior todas, trago todos registro do id selecionado
            for item in list_disp:
                if (item.idhotel == arg[0]) and item.vagas > 0:
                    list.append(item) 
                 
        else:
            for item in list_disp: #se nao,aplico os filtros de datas
                if   item.idhotel == arg[0]  and   datetime.strptime(item.data, "%d-%m-%Y")  >= datetime.strptime(arg[1], "%d-%m-%Y")  and   datetime.strptime(item.data, "%d-%m-%Y")  <= datetime.strptime(arg[2], "%d-%m-%Y") and item.vagas > 0    :
                    list.append(item)

        return list
    except Exception as  e:
            print('Erro ao pesquisa a disponibilidade: '+ str(e))
            return list 




def getListDisp(path):

    """ BUSCO UMA LISTA COM TODOS AS NOITES E DADAS DISPONÍVEIS DOS HOTEIS """
    try:
        list = []
        arquivo = open(path,'r')
        registros = csv.reader(arquivo, delimiter=',')

        for [idhotel, data, vagas, noites] in registros:
            hotel = getHotelByid(int(idhotel))
            disp = disponibilidade(int(idhotel), hotel.nome, hotel.cidade,  data.replace('/','-')  ,int(vagas),  int(noites))
            list.append(disp)

        return list

    except Exception as  e:
        print('Erro ao buscar as diponiidades  no csv:  ' + str(e))
        return list





def searchHotel(cidade,list_hoteis):

    """PROCURANDO HOTEIS POR CIDADE """

    list = []
    try:
        for item in list_hoteis:
                if item.cidade.lower().find(cidade.lower()) > -1  or item.nome.lower().find(cidade.lower()) > -1  :
                     list.append(item)

        return list
    except Exception as  e:
        #print('Erro ao fazer a busca na lista de hoteis '+ str(e))
        return list




def cidadeInList(cidade, list ):
    #procuro ocorrencia no array, se nao encontrar, retorno False
    for item in list:
        if item.cidade == cidade.cidade:
            return True

        return  False


def getHotelByid(idhotel):
    #procuro ocorrencia no array, se nao encontrar, retorno False
        arquivo = open('artefatos/hoteis.csv','r')
        registros = csv.reader(arquivo, delimiter=',')
       
        for [id, cid, nome] in registros:
            if int(id)== idhotel:
                return  hotel(id,cid,nome)
        
        return ''

 
    
""" CONVERTO UM LISTA DE OBJETOS EM UM DICIONÁRIO - PARA USO NO JSON """
def to_dict(obj):
    # Se for um objeto, transforma num dict
    if hasattr(obj, '__dict__'):
        obj = obj.__dict__

    # Se for um dict, lê chaves e valores; converte valores
    if isinstance(obj, dict):
        return { k:to_dict(v) for k,v in obj.items() }
    # Se for uma lista ou tupla, lê elementos; também converte
    elif isinstance(obj, list) or isinstance(obj, tuple):
        return [to_dict(e) for e in obj]
    # Se for qualquer outra coisa, usa sem conversão
    else:
        return obj
     

