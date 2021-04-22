from flask import Flask
from flask_restful import Api,Resource
from resources.hotel import Hotel
#from sqlAlchemy import banco
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///banco.bd"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

#antes da primeira requisicao criar banco
@app.before_first_request
def cria_banco():
    banco.create_all()


api.add_resource(Hotel,'/hotel') 

if __name__ == '__main__':
    from sqlAlchemy import banco
    banco.init_app(app)
    app.run(debug=True)