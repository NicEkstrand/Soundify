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
class User:
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

    

class Follower:
    __tablename__ = "followers"

    # Columns
    id = Column("id", INTEGER, primary_key=True)
    follower_id = Column('follower_id', TEXT, ForeignKey('users.username'))
    following_id = Column('following_id', TEXT, ForeignKey('users.username'))
    

class Search:
    __tablename__ = "searches"
    # Columns
    id = id = Column("id", INTEGER, primary_key=True)
    user_id = Column('user_id', TEXT, ForeignKey('users.username'))
    input = Column("input", TEXT, nullable=False)
    