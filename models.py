"""
The file that holds the schema/classes
that will be used to create objects
and connect to data tables.
"""

from sqlalchemy import ForeignKey, Column, INTEGER, TEXT
from sqlalchemy.orm import relationship
from database import Base
import webbrowser
import spotipy

# TODO: Complete your models
class User(Base):
    __tablename__ = "users"
    # Columns
    username = Column("username", TEXT, primary_key=True)
    password = Column("password", TEXT, nullable=False)

    following = relationship("User", 
                             secondary="followers",
                             primaryjoin="User.username==Follower.follower_id",
                             secondaryjoin="User.username==Follower.following_id")
    
    followers = relationship("User", 
                             secondary="followers",
                             primaryjoin="User.username==Follower.following_id",
                             secondaryjoin="User.username==Follower.follower_id",
                             overlaps="following")


    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def __repr__(self):
        return self.username + ", " + self.password

    

class Follower(Base):
    __tablename__ = "followers"

    # Columns
    id = Column("id", INTEGER, primary_key=True)
    follower_id = Column('follower_id', TEXT, ForeignKey('users.username'))
    following_id = Column('following_id', TEXT, ForeignKey('users.username'))
    

class Search(Base):
    __tablename__ = "searches"
    # Columns
    id = id = Column("id", INTEGER, primary_key=True)
    input = Column("input", TEXT, nullable=False)

    