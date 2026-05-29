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
   
    assert register_response.status_code == 200

    # Login
    login_response = client.post(
        "/auth/login",
        data={
            "username" : "amyra@test.com",
            "password" : "test123"
        }
    )


    assert login_response.status_code == 200

    # Token extraction
    token = login_response.json()["access_token"]

    project = client.post(
        "/projects",
        json={
            "name" : "DevSight",
            "description" : "Security Monitoring Platform"
        },
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )

    assert project.status_code == 200

    project_id = project.json()["id"]

    return token, project_id

def test_create_task_success(client):
    token, project_id = get_auth_token(client)

    response = client.post(
        f"/projects/{project_id}/tasks",
        json={
            "title" : "Task Title",
            "description" : "Some Description",
            "priority" : "None",
            "status" : "None"
        },
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )

    assert response.status_code == 200

def test_duplicate_task(client):
    token, project_id = get_auth_token(client)

    response = client.post(
        f"/projects/{project_id}/tasks",
        json={
            "title" : "Task Title",
            "description" : "Some Description",
            "priority" : "None",
            "status" : "None"
        },
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    

    response = client.post(
        f"/projects/{project_id}/tasks",
        json={
            "title" : "Task Title",
            "description" : "Some Description",
            "priority" : "None",
            "status" : "None"
        },
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )

    assert response.status_code == 400

def test_get_tasks(client):
    token, project_id = get_auth_token(client)

    response = client.post(
        f"/projects/{project_id}/tasks",
        json={
            "title" : "Task Title",
            "description" : "Some Description",
            "priority" : "None",
            "status" : "None"
        },
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    response = client.get(
        f"/projects/{project_id}/tasks",
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )


    assert response.status_code == 200  

    tasks = response.json()

    assert len(tasks) == 1
    assert tasks[0]["title"] == "Task Title"

def test_get_task_by_id(client):
    token, project_id = get_auth_token(client)

    response = client.post(
        f"/projects/{project_id}/tasks",
        json={
            "title" : "Task Title",
            "description" : "Some Description",
            "priority" : "None",
            "status" : "None"
        },
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    task_id = response.json()["id"]

    response = client.get(
        f"/tasks/{task_id}",
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )


    assert response.status_code == 200  

def test_patch_task(client):
    token, project_id = get_auth_token(client)

    response = client.post(
        f"/projects/{project_id}/tasks",
        json={
            "title" : "Task Title",
            "description" : "Some Description",
            "priority" : "None",
            "status" : "None"
        },
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    task_id = response.json()["id"]

    patch_response = client.patch(
        f"/tasks/{task_id}",
        json={
            "title" : "New Task Title",
            "description" : "New Description",
            "priority" : "low",
            "status" : "todo"
        },
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )

    assert patch_response.status_code == 200

    title = patch_response.json()["title"]
    desc = patch_response.json()["description"]
    priority = patch_response.json()["priority"]
    status = patch_response.json()["status"]

    assert title == "New Task Title"
    assert desc == "New Description"
    assert priority == "low"
    assert status == "todo"

def test_delete_task(client):
    token, project_id = get_auth_token(client)

    response = client.post(
        f"/projects/{project_id}/tasks",
        json={
            "title" : "Task Title",
            "description" : "Some Description",
            "priority" : "None",
            "status" : "None"
        },
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    task_id = response.json()["id"]

    delete_response = client.delete(
        f"/tasks/{task_id}",
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )

    assert delete_response.status_code == 200

def test_task_ownership(client):
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

    token, project_id = get_auth_token(client)

    response = client.post(
        f"/projects/{project_id}/tasks",
        json={
            "title" : "Task Title",
            "description" : "Some Description",
            "priority" : "None",
            "status" : "None"
        },
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    task_id = response.json()["id"]

    response = client.get(
    f"/tasks/{task_id}",
        headers={
            "Authorization": f"Bearer {user_b_token}"
        }
    )

    assert response.status_code == 404 

def test_task_no_jwt(client):
    project_id = get_auth_token(client)[1]

    response = client.post(
        f"/projects/{project_id}/tasks",
        json={
            "title" : "Task Title",
            "description" : "Some Description",
            "priority" : "None",
            "status" : "None"
        },
    )

    assert response.status_code == 401

def test_get_task_invalid_id(client):
    token = get_auth_token(client)[0]

    response = client.get(
        "/tasks/9000",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 404

def test_patch_task_invalid_id(client):
    token = get_auth_token(client)[0]

    response = client.patch(
        "/tasks/9000",
        json={
            "title" : "New title"
        }, 
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 404

def test_delete_task_invalid_id(client):
    token = get_auth_token(client)[0]

    response = client.delete(
        "/tasks/9000",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 404

def test_patch_task_no_jwt(client):
    token, project_id = get_auth_token(client)

    response = client.post(
        f"/projects/{project_id}/tasks",
        json={
            "title" : "Task Title",
            "description" : "Some Description",
            "priority" : "None",
            "status" : "None"
        },
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    task_id = response.json()["id"]

    response = client.patch(
        f"/tasks/{task_id}",
        json={
            "title" : "New Title"
        }
    )

    assert response.status_code == 401

def test_patch_task_no_jwt(client):
    token, project_id = get_auth_token(client)

    response = client.post(
        f"/projects/{project_id}/tasks",
        json={
            "title" : "Task Title",
            "description" : "Some Description",
            "priority" : "None",
            "status" : "None"
        },
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    task_id = response.json()["id"]

    response = client.delete(
        f"/tasks/{task_id}",
    )

    assert response.status_code == 401

def test_patch_task_no_ownership(client): 
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

    token, project_id = get_auth_token(client)

    response = client.post(
        f"/projects/{project_id}/tasks",
        json={
            "title" : "Task Title",
            "description" : "Some Description",
            "priority" : "None",
            "status" : "None"
        },
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    task_id = response.json()["id"]

    response = client.patch(
        f"/tasks/{task_id}",
        json={
            "title" : "New Title"
        },
        headers={
            "Authorization": f"Bearer {user_b_token}"
        }
    )

    assert response.status_code == 404 

def test_delete_task_no_ownership(client): 
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

    token, project_id = get_auth_token(client)

    response = client.post(
        f"/projects/{project_id}/tasks",
        json={
            "title" : "Task Title",
            "description" : "Some Description",
            "priority" : "None",
            "status" : "None"
        },
        headers={
            "Authorization" : f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    task_id = response.json()["id"]

    response = client.delete(
        f"/tasks/{task_id}",
        headers={
            "Authorization": f"Bearer {user_b_token}"
        }
    )

    assert response.status_code == 404 