from database_connection import get_database_connection


def _drop_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        drop table if exists games;
    ''')
    connection.commit()


def _create_table(connection):
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
    _drop_table(connection)
    _create_table(connection)
