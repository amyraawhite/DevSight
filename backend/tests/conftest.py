import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)


from app.database import Base
from app.main import app
from app.routers.auth import get_db

# =========================
# Test Database URL
# =========================

import os
from dotenv import load_dotenv

load_dotenv()

TEST_DATABASE_URL = os.getenv("DATABASE_URL")


# =========================
# Engine + Session
# =========================

engine = create_engine(TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# =========================
# Create Tables ONCE
# =========================

Base.metadata.create_all(bind=engine)

# =========================
# Pytest Fixture
# =========================

@pytest.fixture()
def client():

    # Open connection
    connection = engine.connect()

    # Begin transaction
    transaction = connection.begin()

    # Bind session to transaction
    db = TestingSessionLocal(bind=connection)

    # Override dependency
    def override_get_db():

        try:
            yield db

        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    # Test client
    client = TestClient(app)

    yield client

    # Cleanup
    db.close()

    # Rollback ALL changes
    transaction.rollback()

    # Close connection
    connection.close()
    