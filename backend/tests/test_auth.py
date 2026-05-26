import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)



# ===================
# Registration Tests
# ===================
def test_register_user_success(client):
    response = client.post(
        "/auth/register",
        json={
            "username" : "amyra",
            "email" : "amyra@test.com",
            "password" : "test123"
        }
    )

    assert response.status_code == 200


def test_register_user_duplicate_email(client):
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

def test_register_user_invalid_email(client):
    response = client.post(
        "/auth/register",
        json={
            "username" : "amyra",
            "email" : "Invalid Email",
            "password" : "test123"
        }
    )

    assert response.status_code == 422


def test_register_user_missing_data(client):
    response = client.post(
        "/auth/register",
        json={
            "username" : "amyra",
            "email" : "Invalid Email",
            
        }
    )

    assert response.status_code == 422


# =================
# Login Test Routes
# =================
def test_login_success(client): 
    client.post(
        "/auth/register",
        json={
            "username" : "amyra",
            "email" : "amyra@test.com",
            "password" : "test123"
        }
    )


    response = client.post(
        "/auth/login",
        json={
            "email" : "amyra@test.com",
            "password" : "test123"
        }
    )

    assert response.status_code == 200


def test_login_wrong_password(client):
    response = client.post(
        "/auth/login",
        json={
            "email" : "amyra@test.com",
            "password" : "wrong password"
        }
    )

    assert response.status_code == 400

def test_login_invalid_user(client):
    response = client.post(
        "/auth/login",
        json={
            "email" : "notreal@test.com",
            "password" : "wrong password"
        }
    )

    assert response.status_code == 400

def test_login_missing_data(client):
    response = client.post(
        "/auth/login",
        json={
            "email" : "notreal@test.com",
        }
    )

    assert response.status_code == 422


def test_login_invalid_email(client):
    response = client.post(
        "/auth/login",
        json={
            "email" : "notreal@.com",
            "password" : "test123"
        }
    )

    assert response.status_code == 422