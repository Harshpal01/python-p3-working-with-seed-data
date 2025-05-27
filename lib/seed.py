#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Game  # Make sure Base is imported from models

fake = Faker()

if __name__ == '__main__':
    # Define engine
    engine = create_engine('sqlite:///seed_db.db')

    # Create tables in database
    Base.metadata.create_all(engine)

    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    print("Seeding games...")

    games = [
        Game(
            title=fake.name(),
            genre=fake.word(),
            platform=fake.word(),
            price=random.randint(0, 60)
        )
        for _ in range(50)
    ]

    session.bulk_save_objects(games)
    session.commit()
    print("Done seeding.")
