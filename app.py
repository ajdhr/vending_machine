from flask_login import current_user
from flask_migrate import Migrate
from flask_principal import Principal, identity_loaded, UserNeed, RoleNeed
from flask_restplus import Api

from config.develop import DevelopConfig
from db_factory import db
from flask_factory import create_app

import web.model

app = create_app(DevelopConfig)
api = Api(app)
migrate = Migrate(app, db)
principals = Principal(app)


@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    identity.user = current_user

    if hasattr(current_user, "id"):
        identity.provides.add(UserNeed(current_user.id))

    if hasattr(current_user, "role"):
        identity.provides.add(RoleNeed(str(current_user.role)))


if __name__ == "__main__":
    app.run(debug=True)
