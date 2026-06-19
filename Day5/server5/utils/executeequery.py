import utils.dbconnection as dbconn


def execute_select_query(query):
    conn = dbconn.get_dbconnection()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def execute_query(query):
    conn = dbconn.get_dbconnection()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()