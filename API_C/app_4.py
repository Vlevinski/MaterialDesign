from flask import Flask, render_template, request
from API_C.models import  db, User
app = Flask(__name__)

POSTGRES = {
 'user': 'postgres',
 'pw': 'silverTip',
 'db': 'flaskmovie',
 'host': 'localhost',
 'port': '5432',
}
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)

@app.route('/')
def index():
    return render_template('addU.html')

@app.route('/postU', methods=['POST', 'GET'])
def postU():

    if request.form:
        user = User(id=request.form.get("id"), username=request.form.get("username"),email=request.form.get("email"))

        db.session.add(user)
        db.session.commit()
    return render_template('addU.html')

if __name__ == '__main__':
    app.run()
