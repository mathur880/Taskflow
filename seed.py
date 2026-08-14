speed.py
"""Populate a development TaskFlow database with representative data."""

from backend.db import SessionLocal, create_tables
from backend.models import Project, Task, User


def seed() -> None:
    create_tables()

    db = SessionLocal()

    try:
        existing_user = db.query(User).filter(
            User.email == "engineer@blinkit.local"
        ).first()

        if existing_user:
            print("Database already contains seed data.")
            return

        alice = User(email="alice@blinkit.local")
        bob = User(email="bob@blinkit.local")

        db.add_all([alice, bob])
        db.flush()

        fulfillment = Project(owner_id=alice.id)
        reliability = Project(owner_id=bob.id)

        db.add_all([fulfillment, reliability])
        db.flush()

        tasks = [
            Task(
                project_id=fulfillment.id,
                title="Fix inventory sync retry logic",
                priority="high",
                due_date="2026-08-15",
            ),
            Task(
                project_id=fulfillment.id,
                title="Add pod health dashboard",
                priority="medium",
                due_date="2026-08-20",
            ),
            Task(
                project_id=reliability.id,
                title="Review Redis connection metrics",
                priority="low",
                due_date=None,
            ),
            Task(
                project_id=reliability.id,
                title="Document deployment rollback",
                priority="medium",
                due_date="2026-08-25",
            ),
        ]

        db.add_all(tasks)
        db.commit()

        print("Seed complete.")
        print(f"Users: {alice.id}, {bob.id}")
        print(f"Projects: {fulfillment.id}, {reliability.id}")

    finally:
        db.close()


if __name__ == "__main__":
    seed()