import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Supporter(Base):
    __tablename__ = 'supporter'
   
    id = Column(Integer, primary_key=True)
    user_to = Column(Integer)
    user_from = Column (Integer)
    

class Likes(Base):
    __tablename__ = 'likes'
    
    id = Column(Integer, primary_key=True)
    like = Column(Integer)
    
class MediaCenter(Base):
    __tablename__ = 'mediacenter'
    id = Column(Integer, primary_key=True)
    type = Column(String(200), nullable=False)
    url = Column(String(200))
    tag = Column(String(200))
    likes_id = Column(Integer, ForeignKey('likes.id'))
    likes = relationship(Likes)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    text = Column(String(200), nullable=False)
    media_center_id = Column(Integer, ForeignKey('mediacenter.id'))
    media_center = relationship(MediaCenter)  

class Profile(Base):
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    username = Column(String(200), nullable=False)
    phone = Column(String(200),nullable=False)
    bio = Column(String(200))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    user_to_id = Column(Integer, ForeignKey('supporter.id'))
    supporter = relationship(Supporter)
    user_from_id = Column(Integer, ForeignKey('supporter.id'))
    follower= relationship(supporter)   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e