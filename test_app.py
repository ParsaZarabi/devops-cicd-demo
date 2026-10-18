from app import add, is_service_healthy

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_health():
    assert is_service_healthy() is True
