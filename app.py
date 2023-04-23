from flask import Flask
from resources import Exchange,MaxMin,MajorDiff
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint

#Setting up the application
app = Flask(__name__)
api = Api(app)

#Setting up the front-end part
SWAGGER_URL = '/swagger'
API_URL='/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(SWAGGER_URL,API_URL,config={'app_name':'NBP data extractor'})
app.register_blueprint(SWAGGER_BLUEPRINT,url_prefix=SWAGGER_URL)

#Setting up API endpoints
api.add_resource(Exchange,'/exchanges/<string:currency_code>/<string:date>')
api.add_resource(MaxMin,'/max_min/<string:currency_code>/<int:num_of_last_quot>')
api.add_resource(MajorDiff,'/major_diff/<string:currency_code>/<int:num_of_last_quot>')

#Running the server
if __name__ == '__main__':
    app.run(host='0.0.0.0')