from flask_restful import Resource, reqparse
from sqlAlchemy import banco

class HotelModel(banco.Model):
    # mapear tabela do banco
    __tablename__  = 'hoteis'

    id = banco.Column(banco.String,primary_key = True)
    nome = banco.Column(banco.String(80))
    estrelas = banco.Column(banco.Float(precision=1))
    diaria = banco.Column(banco.Float(precision = 2))
    cidade = banco.Column(banco.String(40))

    def __init__(self,nome,estrelas,diaria,cidade):
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def json(self):
        return {
            'nome':self.nome,
            'estrelas':self.estrelas,
            'diaria':self.diaria,
            'cidade':self.cidade
        }

class Hotel(Resource):
    
    atributos = reqparse.RequestParser()
        
    atributos.add_argument('nome')
    atributos.add_argument('estrelas')
    atributos.add_argument('diaria')
    atributos.add_argument('cidade')

    def post(self):

        dados = Hotel.atributos.parse_args() #objeto
        hotel_objeto = HotelModel(**dados)
        novo_hotel = hotel_objeto.json()

        return novo_hotel,200
    
    def get(self):
        return {'hoteis':'meus hoteis'}