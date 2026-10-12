import pytest 

class FakeDatabase:
    def __init__(self):
        self.connected = False 
        self.data = [] 
    def connection(self):
        self.connected = True 
    def disconnect(self):
        self.connected = False 
        
@pytest.fixture
def database():
    db = FakeDatabase()
    db.connection()
    yield db 
    db.disconnect()
    
def test_database_connected(database):
    assert database.connected is True 