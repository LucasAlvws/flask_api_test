from flask import Flask

from views import blueprint
from extensions import db, migrate, ma


app = Flask(__name__)
app.register_blueprint(blueprint)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)
migrate.init_app(app, db)
ma.init_app(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)