from app.database import Base, engine # Fix app routing
import app.models # noqa: F401

print("Dropping all tables...")
Base.metadata.drop_all(bind=engine)

print("Creating all tables")
Base.metadata.create_all(bind=engine)
