from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_rpn_calculator():
    # Test sum
    response = client.post("/calculate/", json={"expression": ["2", "3", "+"]})
    assert response.status_code == 200
    assert response.json() == {"expression": "2 3 +", "result": 5}

def test_invalid_expression():
    # Test invalid expression
    response = client.post("/calculate/", json={"expression": ["2", "3", "a"]})
    assert response.status_code == 400  # Erreur d'opérateur invalide

def test_empty_expression():
    # Test empty expressions
    response = client.post("/calculate/", json={"expression": []})
    assert response.status_code == 400  # Erreur d'expression invalide
def test_division_by_zero():
    # Test division by zero
    response = client.post("/calculate/", json={"expression": ["4", "0", "/"]})
    assert response.status_code == 400  # Erreur pour division par zéro
    assert response.json() == {"detail": "Division by zero is not allowed"}
