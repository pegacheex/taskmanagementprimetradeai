"""
Database initialization script
Run this once to create all tables
"""
from app.core.database import engine, Base
from app.models import User, Task

def init_db():
    """Create all database tables"""
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

if __name__ == "__main__":
    init_db()

