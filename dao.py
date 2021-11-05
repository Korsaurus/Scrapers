import psycopg2


def getConnection():
    conn = psycopg2.connect(
        host="",
        database="People",
        user="postgres",
        password=["sql_pass"]
    )
    return conn


def insertData(email_list, tableName):

    conn = getConnection()
    cur = conn.cursor()


    insertSql = f"""
    insert into public.people()
    values()
    """

    cur.execute(insertSql)
    conn.commit()
    cur.close()
    conn.close()