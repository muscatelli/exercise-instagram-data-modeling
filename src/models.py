import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    post= relationship('post')

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey("user.id"))
    user_to_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String, nullable=False)
    autor_id = Column(Integer, ForeignKey("user.id"))
    user_id = Column(Integer, ForeignKey("post.id") )
   # post_id = Column(Integer, ForeignKey("user.id"))
    #comment = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey("user.id"))
    #person = relationship(User)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
 

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e