import sqlite3


def connection(operation):
    def wrapper(*args, **kwargs):
        connect = sqlite3.connect('db_users.db')
        cursor = connect.cursor()

        result = operation(args[0], cursor)

        connect.commit()

        cursor.close()
        connect.close()

        return result
    return wrapper


@connection
def insert_data(values, cursor=None):
    print(values, cursor)
    try:
        cursor.execute("INSERT INTO users VALUES (?, ?, ?)", values)
    except Exception as e:
        print(e)
        return False
    else:
        return True
