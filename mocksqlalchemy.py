class Column:
    """
    Mocks the Column api of the SQLAlchemy library
    A name, datatype and a (default) value can be assigned throughout
    the lifecycle of the model (table) of the database.
    """
    
    def __init__(self, name = None, datatype = None, default = None):
        """=
        Args:
            name ([str], optional): This is the column name in the SQL table. Defaults to None.
            datatype ([type], optional): This is any datatype for the SQL Table. Defaults to None.
            default ([type], optional): This is the initial value for the model's object. Defaults to None.
        """        
        self.name = name
        self.datatype = datatype
        self.value = default


class Model:
    """
    Mocks the Model api of the SQLAlchemy library.
    It creates a Python Object that relates to a SQL Table.
    This forms the fundamental of ORM through SQLAlchemy.
    """    

    def __init__(self):
        self.__tablename__ = None

    def getTableName(self):
        return self.__tablename__

class SQLAlchemy:
    """
    Mocks the frontend interface of the SQLAlchemy libary.
    It contains references to all the helper classes in the library.
    It can be instantiated as an object, and classes can be used as
    super-classes in other model/column class.
    """    

    Model = Model
    Column = Column
    String = str
    Integer = int
