__author__ = "Himmler Louissaint"

from Web_Development.Web_Tutorial_SQLAchemy.app import app
from Web_Development.Web_Tutorial_SQLAchemy.db import db

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()