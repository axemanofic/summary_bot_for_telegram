import sqlite3


def connection(operation):
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        connect = sqlite3.connect('db_users.db')
        cursor = connect.cursor()

        result = operation(*args, cursor)

        connect.commit()

        cursor.close()
        connect.close()

        return result
    return wrapper


@connection
def insert_data(values, cursor=None):
    try:
        cursor.execute("INSERT INTO users VALUES (?, ?)", values)
    except Exception as e:
        print(e)
        return False
    else:
        return True

@connection
def count_data(cursor=None):
    try:
        cursor.execute("SELECT COUNT(*) FROM users")
    except Exception as e:
        print(e)
        return False
    else:
        result = cursor.fetchone()[0]
        return result
