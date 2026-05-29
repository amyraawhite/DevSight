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

# Post Routes
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

# get routes
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

# patch routes 
def test_update_project_success(client): 
    token = get_auth_token(client)

    project_response = client.post(
        "/projects",
        json={
            "name" : "DevSight",
            "description" : "Security platform"
        },
        headers = {
            "Authorization" : f"Bearer {token}"
        }
    )

    assert project_response.status_code == 200

    project_id = project_response.json()["id"]

    update_response = client.patch(
        f"/projects/{project_id}",
        json={
            "name" : "DevSight V2"
        },
        headers = {
            "Authorization" : f"Bearer {token}"
        }
    )

    assert update_response.status_code == 200

    update_response = client.patch(
        f"/projects/{project_id}",
        json={
            "description" : "Upgrade Security platform"
        },
        headers = {
            "Authorization" : f"Bearer {token}"
        }
    )

    assert update_response.status_code == 200

    update_response = client.patch(
        f"/projects/{project_id}",
        json={
            "name" : "DevSight V3",
            "description": "Highest level of security"
        },
        headers = {
            "Authorization" : f"Bearer {token}"
        }
    )

    assert update_response.status_code == 200

def test_update_project_invalid_id(client):
    token = get_auth_token(client)

    update_response = client.patch(
        "/projects/9000",
        json={
            "name" : "DevSight V2"
        },
        headers = {
            "Authorization" : f"Bearer {token}"
        }
    )

    assert update_response.status_code == 404

def test_update_project_duplicate_name(client): 
    token = get_auth_token(client)

    project_a_response = client.post(
        "/projects",
        json={
            "name" : "DevSight",
            "description" : "Security platform"
        },
        headers = {
            "Authorization" : f"Bearer {token}"
        }
    )

    assert project_a_response.status_code == 200

    project_b_response = client.post(
        "/projects",
        json={
            "name" : "DevSight V2",
            "description" : "Better security platform"
        },
        headers = {
            "Authorization" : f"Bearer {token}"
        }
    )


    assert project_b_response.status_code == 200

    project_id = project_a_response.json()["id"]
    update_response = client.patch(
        f"/projects/{project_id}",
        json={
            "name" : "DevSight V2"
        },
        headers = {
            "Authorization" : f"Bearer {token}"
        }
    )

    assert update_response.status_code == 400

def test_update_project_no_jwt(client): 
    token = get_auth_token(client)

    project_response = client.post(
        "/projects",
        json={
            "name" : "DevSight",
            "description" : "Security platform"
        },
        headers = {
            "Authorization" : f"Bearer {token}"
        }
    )
    assert project_response.status_code == 200
    project_id = project_response.json()["id"]

    response = client.patch(
        f"/projects/{project_id}",
        json={
            "name" : "DevSight V2"
        }
    )

    assert response.status_code == 401

def test_update_project_not_owner(client): 
    token_a = get_auth_token(client)

    project_response = client.post(
        "/projects",
        json={
            "name" : "DevSight",
            "description" : "Security platform"
        },
        headers = {
            "Authorization" : f"Bearer {token_a}"
        }
    )
    assert project_response.status_code == 200
    project_id = project_response.json()["id"]

    user_b = client.post(
        "/auth/register",
        json={
            "username" : "user2",
            "email" : "user2@example.com",
            "password" : "password"
        }
    )

    assert user_b.status_code == 200

    user_b = client.post(
        "/auth/login",
        data={
            "username" : "user2@example.com",
            "password" : "password"
        }
    )

    assert user_b.status_code == 200

    user_b_token = user_b.json()["access_token"]

    update_response = client.patch(
        f"/projects/{project_id}",
        json={
            "name" : "DevSight V2"
        }, 
        headers={
            "Authorization" : f"Bearer {user_b_token}"
        }
    )

    assert update_response.status_code == 404

# delete routes
def test_delete_project_success(client): 
    token = get_auth_token(client)

    project_response = client.post(
        "/projects",
        json = {
            "name" : "DevSight",
            "description" : "Security Monitoring Platform"
        },
        headers = {
            "Authorization" : f"Bearer {token}"
        }
    )

    assert project_response.status_code == 200

    project_id = project_response.json()["id"]
    delete_response = client.delete(
        f"/projects/{project_id}",
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )

    assert delete_response.status_code == 200

def test_delete_project_invalid_id(client):
    token = get_auth_token(client)

    delete_response = client.delete(
        "/projects/9000",
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )

    assert delete_response.status_code == 404

def test_delete_project_no_jwt(client): 
    token = get_auth_token(client)

    project_response = client.post(
        "/projects",
        json={
            "name" : "DevSight",
            "description" : "Security platform"
        },
        headers = {
            "Authorization" : f"Bearer {token}"
        }
    )
    assert project_response.status_code == 200
    project_id = project_response.json()["id"]

    response = client.delete(
        f"/projects/{project_id}",
    )

    assert response.status_code == 401

def test_delete_project_not_owner(client): 
    token_a = get_auth_token(client)

    project_response = client.post(
        "/projects",
        json={
            "name" : "DevSight",
            "description" : "Security platform"
        },
        headers = {
            "Authorization" : f"Bearer {token_a}"
        }
    )
    assert project_response.status_code == 200
    project_id = project_response.json()["id"]

    user_b = client.post(
        "/auth/register",
        json={
            "username" : "user1",
            "email" : "user2@example.com",
            "password" : "password"
        }
    )

    assert user_b.status_code == 200

    user_b = client.post(
        "/auth/login",
        data={
            "username" : "user2@example.com",
            "password" : "password"
        }
    )

    assert user_b.status_code == 200

    user_b_token = user_b.json()["access_token"]

    update_response = client.delete(
        f"/projects/{project_id}",
        headers={
            "Authorization" : f"Bearer {user_b_token}"
        }
    )

    assert update_response.status_code == 404

