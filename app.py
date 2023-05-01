from flask import *
from database import init_db, db_session
from models import *

app = Flask(__name__)

# TODO: Change the secret key
app.secret_key = "Change Me"

# TODO: Fill in methods and routes

@app.before_first_request
def setup():
    init_db()

if __name__ == "__main__":
    app.run(debug=True)
