import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    users = db.relationship('User', backref='role')

    def __repr__(self):
        return "<User %r>" % self.name


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(64), unique=True)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return "<User %r>" % self.username


@app.route("/", methods=["GET", "POST"])
def index():
    pass


if __name__ == '__main__':
    # db.create_all()
    # admin_role = Role(name="Admin", id=1)
    # mod_role = Role(name="Moderator", id=2)
    # user_role = Role(name='User', id=3)
    #
    # user_john = User(username='john', role=admin_role)
    # user_susan = User(username='susan', role=user_role)
    # user_david = User(username='david', role=user_role)
    #
    # db.session.add(admin_role)
    # db.session.add(mod_role)
    # db.session.add(user_role)
    # db.session.add(user_john)
    # db.session.add(user_susan)
    # db.session.add(user_david)
    #
    # db.session.commit()

    print(Role.query.all())
