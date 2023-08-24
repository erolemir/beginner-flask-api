from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/araba'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Araba(db.Model):
    __tablename__='araba'
    id=db.Column(db.Integer,primary_key=True)
    marka=db.Column(db.String)
    model=db.Column(db.String)
    yil = db.Column(db.Date)
    fiyat = db.Column(db.Integer)
    resim = db.Column(db.String)
    
    



@app.route('/gorevler',methods=['GET'])
def getir():
    gorevler = Araba.query.all()
    return ([{'id':g.id, 'marka':g.marka, 'model':g.model, 'yil':g.yil, 'fiyat':g.fiyat, 'resim':g.resim}for g in gorevler])


@app.route('/gorevler',methods=['POST'])
def ekle():
    araba = Araba(marka ='Ford', model='Mustang', yil='2020-1-18', fiyat=2000, resim='link')
    db.session.add(araba)
    db.session.commit()
    return jsonify({'id':araba.id, 'marka':araba.marka, 'model':araba.model, 'yil':araba.yil, 'fiyat':araba.fiyat, 'resim':araba.resim})


@app.route('/gorevler/<int:id>',methods=['DELETE'])
def sil(id):
    Araba.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({'message':'araba silindi'})


@app.route('/gorevler/<int:id>',methods=['PUT'])
def guncel(id):
    araba = Araba.query.get(id)
    araba.model= "Şahin",
    araba.marka = "Tofaş",
    araba.yil = "2020-01-01",
    araba.fiyat = 50000,
    araba.resim = "link"
    db.session.commit()
    
    return jsonify ({'id':araba.id, 'marka':araba.marka, 'model':araba.model, 'yil':araba.yil, 'fiyat':araba.fiyat, 'resim':araba.resim})
    


if __name__ == '__main__':
    app.run(debug=True)
