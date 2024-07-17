from health_app.orm_files.connection import create_connection, database

def create_table(conn, sql_path):
    with open(sql_path) as file:
        sql_expr = file.read()
        cur = conn.cursor()
        cur.executescript(sql_expr)
        conn.commit()




def main():
    with create_connection(database) as conn:
        create_table(conn, '../sql_files/create_tables.sql')


if __name__ == "__main__":
    main()
