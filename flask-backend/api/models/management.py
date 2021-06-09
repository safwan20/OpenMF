"""
Class definition of management user model.
"""
from api.models.base_user import BaseUser
from api.extansions import db

class Management(BaseUser):
    __tablename__="management"
    id = db.Column(db.Integer, unique=True, primary_key=True)
    role = db.Column(db.String(255), default="management")
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))

    def __init__(self, name, email, password, admin):
        """
        Constructor for management user model.
        """
        super().__init__(name, email,password)
        self.admin = admin

    def __repr__(self):
        """
        Official way of representing management user in db.
        """
        return (
            f"<Management email={self.email}, public_id={self.public_id}, admin_email={self.admin.email}>"
        )