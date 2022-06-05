import pymysql.cursors

with open('mysqlsampledatabase', 'r') as file:
    # NOTE: WORKAROUND: mysqlsampledatabase is prepared for read with pymsql;
    #       it has /* BREAK */ comments to break the queries into separate queries in list
    #       For some reason pymysql doesnt run multiline queries,
    #       so they need to be split into separate queries
    #       ; separator is not used because some of the insert rows have ; in them
    reset_db_queries = file.read().split('/* BREAK */')


def reset():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='db-user54093',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor,
                                 autocommit=True)

    with connection:
        with connection.cursor() as cursor:
            for query in reset_db_queries:
                cursor.execute(query)
