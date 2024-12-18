from src.mathoperation import add, sub

def test_add():
    assert add(2,3) == 5
    assert add(-1,1)==0
    
def test_sub():
    assert sub(5,4)==1
    assert sub(6,1)==5
    