from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////C:\\Users\\emers\\Documents\\CMSC 447\\HW_2\\users.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class users( db.Model):
        id = db.Column(db.Integer, primary_key=True),
        name  = db.Column(db.String(20))
        points = db.Column(Integer)
def __init__(self, id, name, points):
        self.name = name
        self.points = points
class ArticleSchema(ma.Schema):
        class Meta:
                fields = ('id', 'name', 'points')

article_schema = ArticleSchema()
article_schema = ArticleSchema(many=True)

@app.route('/get', methods = ['GET'])
def get_articles():
        all_articles = Articles.query.all()
        results = articles_schema.dump(all_articles)
        return jsonify(results)

@app.route('/get/<id>', methods = ['GET'])
def post_details(id):
        article = Articles.query.get(id)
        return article_schema.jsonify(article)

@app.route('/add', methods = ['POST'])
def add_article():
        name = request.json['name']
        points = request.json['points']

        articles = Articles(name, points)
        db.session.add(articles)
        db.sesesion.commit()
        return article_schema.jsonify(articles)

@app.route('/update/<id>', methods = ['PUT'])
def update_article(id):
        article = Articles.query.get(id)

        name = request.json['name']
        points = request.json['points']
        
        article.name = name
        article.points = points

        db.session.commit()
        return article_schema.jsonify(article)

@app.route('/delete/<id>', methods = ['DELETE'])
def article_delete(id):
        article = Articles.query.get(id)
        db.session.delete(article)
        db.session.commit()

        return article_schema.jsonify(article) 

if __name__ == "__main__":
        app.run(debug=True)