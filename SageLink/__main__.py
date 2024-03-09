from SageLink import app
from SageLink.models import *
from SageLink.controllers import *


"""
This file runs the server at a given port
"""
sqlalchemy = SQLAlchemy()
sqlalchemy.init_app(app)
FLASK_PORT = 8081

if __name__ == "__main__":
    app.run(debug=True, port=FLASK_PORT)
