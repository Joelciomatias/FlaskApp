from flask_restful import Resource, reqparse
# from models.hotel import HotelModel
from models.hotel import HotelModel
hoteis = [
    {
    'hotel_id':'alpha',
    'nome':'Alpha Hotel',
    'estrelas':4.3,
    'diaria':420.34,
    'cidade':'Curitiba'
    },
    {
    'hotel_id':'beta',
    'nome':'Beta Hotel',
    'estrelas':2.3,
    'diaria':220.34,
    'cidade':'Curitiba'
    },
    {
    'hotel_id':'omega',
    'nome':'Omega Hotel',
    'estrelas':2.3,
    'diaria':620.34,
    'cidade':'Curitiba'
    },
    {
    'hotel_id':'Theta',
    'nome':'Theta HotResourceel',
    'estrelas':5.3,
    'diaria':520.34,
    'cidade':'Curitiba'
    },
    {
    'hotel_id':'alpha',
    'nome':'Alpha Hoteltasks',
    'estrelas':4.3,
    'diaria':420.34,
    'cidade':'Curitiba'
    },
]

class Hoteis(Resource):
    def get(self):
        return hoteis,200

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def find_hotel(self,hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None
    def get(self,hotel_id):
        hotel = self.find_hotel(hotel_id)
        if hotel:
            return hotel
        return []
    def post(self,hotel_id):

        dados = self.argumentos.parse_args()
    
        _novo_hotel = HotelModel(hotel_id, **dados)
        novo_hotel = _novo_hotel.json()

        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self,hotel_id):
        dados = self.argumentos.parse_args()

        _novo_hotel = HotelModel(hotel_id, **dados)
        novo_hotel = _novo_hotel.json()
        hotel = self.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel,200
        hoteis.append(novo_hotel)
        return novo_hotel,201

    def delete(self,hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return 'hotel deleted'
   