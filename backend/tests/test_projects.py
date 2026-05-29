import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

def get_auth_token(client): 
    register_response = client.post(
        "/auth/register",
        json={
            "username" : "amyra",
            "email" : "amyra@test.com",
            "password" : "test123"
        }
    )
    print(register_response.json())
    assert register_response.status_code == 200

    # Login
    login_response = client.post(
        "/auth/login",
        data={
            "username" : "amyra@test.com",
            "password" : "test123"
        }
    )
    print(login_response.json())

    assert login_response.status_code == 200

    # Token extraction
    token = login_response.json()["access_token"]

    return token

# ===================
# Project Tests
# ===================
def test_create_and_get_project_success(client):
    token = get_auth_token(client)

    # Project creation
    response = client.post(
        "/projects",
        json={
            "name" : "DevSight",
            "description" : "Security Monitoring Platform"
        },
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )

    assert response.status_code == 200 

    response = client.get(
        "/projects",
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    projects = response.json()

    assert len(projects) == 1
    assert projects[0]["name"] == "DevSight"

    project_id = projects[0]["id"]
    response = client.get(
        f"/projects/{project_id}",
        headers = {
            "Authorization" : f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    assert response.json()["name"] == "DevSight"

def test_create_dupe_project(client): 
    token = get_auth_token(client)

    # Project creation
    response = client.post(
        "/projects",
        json={
            "name" : "DevSight",
            "description" : "Security Monitoring Platform"
        },
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    response = client.post(
        "/projects",
        json={
            "name" : "DevSight",
            "description" : "Security Monitoring Platform"
        },
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )

    assert response.status_code == 400 
    assert response.json()["detail"] == "Project already exists."

def test_no_jwt_project_create(client):
    response = client.post(
        "/projects",
        json={
            "name" : "DevSight",
            "description" : "Security Monitoring Platform"
        },

    )

    assert response.status_code == 401

def test_no_jwt_project_get(client):
    response = client.get(
        "/projects",
    )

    assert response.status_code == 401

def test_no_jwt_project_id_get_no_jwt(client):
    response = client.get(
        "/projects/9000",

    )

    assert response.status_code == 401

def test_project_id_get_fail(client):
    token =get_auth_token(client)
    response = client.get(
        "/projects/9000",
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )

    assert response.status_code == 404


def test_project_ownership(client): 
    user_a_token = get_auth_token(client)

    project_response = client.post(
        "/projects",
        json={
            "name": "DevSight",
            "description" : "Security monitoring application"
        },
        headers={
            "Authorization" : f"Bearer {user_a_token}"
        }

    )

    assert project_response.status_code == 200

    # create new temp user
    register_response = client.post(
        "/auth/register",
        json={
            "username" : "user2",
            "email" : "user2@example.com",
            "password" : "password"
        }
    )

    assert register_response.status_code == 200

    login_response = client.post(
        "/auth/login",
        data={
            "username" : "user2@example.com",
            "password" : "password"
        }
    )

    assert login_response.status_code == 200

    user_b_token = login_response.json()["access_token"]
    project_id = project_response.json()["id"]


    project_response = client.get(
        f"/projects/{project_id}",
        headers={
            "Authorization" : f"Bearer {user_b_token}"
        }
    )

    assert project_response.status_code == 404

