from flask import *
import waitress


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('dashboard.html')


print('Server is running on 0.0.0.0:5000')
waitress.serve(app, host='0.0.0.0', port=8080)
