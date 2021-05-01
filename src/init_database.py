from database_connection import get_database_connection


def drop_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        drop table if exists games;
    ''')
    connection.commit()


def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        create table games ( 
            id INTEGER PRIMARY KEY,
            timestamp text,
            win_loss text
        );
    ''')

    connection.commit()


def init_database():
    connection = get_database_connection()
    drop_table(connection)
    create_table(connection)
