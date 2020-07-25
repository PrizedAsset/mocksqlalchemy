from mocksqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """
    An example User class.

    Args:
        db ([SQLAlchemy]): The SQLAlchemy class/object that contains reference to the Model class
    """    
    __tablename__ = "user"

    rollno = db.Column("rollno", db.Integer, default=1)
    username = db.Column("username", db.String)
    
    def __init__(self, rollno=None, username=None):
        self.rollno.value = rollno
        self.username.value = username
    
    def __str__(self):
        return "User <{}>: {}".format(self.rollno.value, self.username.value)

if __name__ == "__main__":
    u = User(rollno=1, username="monkfromearth")
    print(u)