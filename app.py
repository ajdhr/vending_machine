from flask_migrate import Migrate
from flask_restplus import Api

from config.develop import DevelopConfig
from db_factory import db
from flask_factory import create_app

import web.model

app = create_app(DevelopConfig)
api = Api(app)
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
