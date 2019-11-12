from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r, %r>' % (self.username, self.name)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    # def get_id(self):
    #     return str(self.id)

# APENAS PARA MODELO DE RELACIONAMENTO
# class Post(db.Model):
#     __tablename__ = "posts"
#
#     id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
#     content = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id', name='FK_post_user'))
#
#     user = db.relationship("User", foreign_keys=user_id)
#
#     def __init__(self, content, user_id):
#         self.content = content
#         self.user_id = user_id
#
#     def __repr__(self):
#         return '<Post %r>' % self.id
#
#
# class Follow(db.Model):
#     __tablename__ = "follow"
#
#     id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id', name='FK_Follow_User'))
#     follower_id = db.Column(db.Integer, db.ForeignKey('users.id', name='FK_Follow_Follower'))
#
#     user = db.relationship('User', foreign_keys=user_id)
#     follower = db.relationship('User', foreign_keys=follower_id)
#
#     def __init__(self, user_id, post_id):
#         self.user_id = user_id
#         self.post_id = post_id
#
#     def __repr__(self):
#         return '<Follow %r>' % self.id
