from src.main import greet

def test_greet():
    assert greet("test") == "Hello, test!"
