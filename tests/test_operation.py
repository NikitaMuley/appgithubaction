from src.math_operations import add,sub  # importing add, sub functions fom math_operations.py file located in src folder

def test_add():
    assert add(2,3)==5   # assert checks if the statement is True
    assert add(-1,1)==0
    
def test_sub():
    assert sub(5,3)==2
    assert sub(4,3)==1
    assert sub(3,3)==0
    assert sub(2,3)==-1
