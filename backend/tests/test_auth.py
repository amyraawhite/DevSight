import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# ===================
# Registration Tests
# ===================
def test_register_user_success():
    response = client.post(
        "/auth/register",
        json={
            "username" : "amyra",
            "email" : "amyra@test.com",
            "password" : "test123"
        }
    )

    assert response.status_code == 200


def test_register_user_duplicate_email():
    client.post(
        "/auth/register",
        json={
            "username" : "amyra",
            "email" : "amyra@test.com",
            "password" : "test123"
        }
    )

    response = client.post(
        "/auth/register",
        json={
            "username" : "amyra",
            "email" : "amyra@test.com",
            "password" : "test123"
        }
    )

    assert response.status_code == 400

def test_register_user_invalid_email():
    response = client.post(
        "/auth/register",
        json={
            "username" : "amyra",
            "email" : "Invalid Email",
            "password" : "test123"
        }
    )

    assert response.status_code == 422


def test_register_user_missing_data():
    response = client.post(
        "/auth/register",
        json={
            "username" : "amyra",
            "email" : "Invalid Email",
            
        }
    )

    assert response.status_code == 422
