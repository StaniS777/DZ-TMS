from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db import DBrepository
from menu import Menu


def main(username, password, host, port, database):
    connection_string = f'postgresql://{username}:{password}@{host}:{port}/{database}'
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()
    repo = DBrepository(session=session)
    menu = Menu(repo)
    while True:
        menu.show_menu()


if __name__ == "__main__":
    main("postgres", "Qawsedr5", "localhost", "5432", "stanis")