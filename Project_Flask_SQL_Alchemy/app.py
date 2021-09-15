from flask import Flask,render_template,request,redirect
from models import db,GuestsModel
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:paypal123@localhost:5433/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()
 
@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        guest_id = request.form['guest_id']
        name = request.form['name']
        age = request.form['age'] 
        email = request.form['email']
        guest = GuestsModel(guest_id=guest_id, name=name, age=age, email = email)
        db.session.add(guest)
        db.session.commit()
        return redirect('/data')
 
 
@app.route('/data')
def RetrieveList():
    guests = GuestsModel.query.all()
    return render_template('datalist.html',guests = guests)
 
 
@app.route('/data/<int:id>')
def Retrieveguest(id):
    guest = GuestsModel.query.filter_by(guest_id=id).first()
    if guest:
        return render_template('data.html', guest = guest)
    return f"guest with id ={id} Doesnt exist"
 
 
@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
    guest = GuestsModel.query.filter_by(guest_id=id).first()
    if request.method == 'POST':
        if guest:
            db.session.delete(guest)
            db.session.commit()
            name = request.form['name']
            age = request.form['age']
            email = request.form['email']
            guest = GuestsModel(guest_id=id, name=name, age=age, email = email)
            db.session.add(guest)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"guest with id = {id} Does not exist"
 
    return render_template('update.html', guest = guest)
 
 
@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    guest = GuestsModel.query.filter_by(guest_id=id).first()
    if request.method == 'POST':
        if guest:
            db.session.delete(guest)
            db.session.commit()
            return redirect('/data')
        abort(404)
 
    return render_template('delete.html')
 
app.run(host='localhost', port=6000, debug=True)

# Before adding docker used localhost
#app.run(host='localhost', port=5000, debug=True)