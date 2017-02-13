import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 以下都是套路
app = Flask(__name__)
app.secret_key = 'model'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 指定数据库的路径
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weibos.db'

db = SQLAlchemy(app)


# 定义一个Model，继承自 db.Model
class Weibo(db.Model):
    __tablename__ = 'weibos'
    # 下面是定义字段
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    created_time = db.Column(db.String(), default=0)
    user_id = db.Column(db.Integer)

    def __repr__(self):
        return u'<Weibo {} {}>'.format(self.id, self.content)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __init__(self, form, user_id):
        self.content = form.get('content', '')
        self.created_time = int(time.time())
        self.user_id = user_id

    def valid(self):
        return len(self.content) > 0


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    created_time = db.Column(db.Integer, default=0)

    def __repr__(self):
        return u'<User {} {}'.format(self.id, self.username)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __init__(self, form):
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.created_time = int(time.time())

    def valid(self):
        return len(self.username) > 2 and len(self.password) > 2 and (User.query.filter_by(username=self.username).first() is None)

    def validate_login(self, u):
        return u.username == self.username and u.password == self.password

    def change_password(self, password):
        if len(password) > 2:
            self.password = password
            self.save()
            return True
        return False


class Comment(db.Model):
    __tablename__ = 'comments'
    # 下面是定义字段
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    created_time = db.Column(db.String(), default=0)
    user_id = db.Column(db.Integer)
    weibo_id = db.Column(db.Integer)

    def __repr__(self):
        return u'<Weibo {} {}>'.format(self.id, self.content)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __init__(self, form, user_id):
        self.content = form.get('content', '')
        self.created_time = int(time.time())
        self.user_id = user_id

    def valid(self):
        return len(self.content) > 0


if __name__ == '__main__':
    # 先 drop_all 删除所有数据库中的表
    # 再 create_all 创建所有的表
    db.drop_all()
    db.create_all()
    print('rebuild database')