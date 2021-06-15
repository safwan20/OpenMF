"""
Class definition of extractor user model.
"""
from api.models.base_user import BaseUser
from api.extansions import db

class Extractor(BaseUser):
    __tablename__="extractor"
    id = db.Column(db.Integer, unique=True, primary_key=True)
    role = db.Column(db.String(255), default="extractor")
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))
    extracted_cases = db.relationship("Case", backref="extractor", lazy=True)
    assinged_tasks = db.relationship("Task", backref="extractor", lazy=True)

    def __init__(self, name, email, password, admin, role="extractor"):
        """
        Constructor for extractor user model.
        """
        super().__init__(name, email,password)
        self.admin = admin
        self.role = role

    def __repr__(self):
        """
        Official way of representing extractor user in db.
        """
        return (
            f"<Extractor email={self.email}, public_id={self.public_id}, admin_email={self.admin.email}>"
        )