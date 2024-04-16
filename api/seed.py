from sqlalchemy import text
from app import db, app

sql = open("user.sql", "r")
statement = sql.read()

with app.app_context():
    db.session.execute(text(statement))
    db.session.commit()