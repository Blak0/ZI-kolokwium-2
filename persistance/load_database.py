from typing import Callable, Tuple

import pymysql.cursors

from entities import *
from persistance.repos import *

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='db-user54093',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


tables_to_class_maps: Tuple[str, Entity] = [
    ('customers', Customer),
    ('payments', Payment),
    ('orders', Order),
    ('orderdetails', OrderDetails)
]


def load_database_into_repo(load_entities_repo: Callable[[str, List[Entity]], None]):
    with connection:
        for table_name, entity_class in tables_to_class_maps:
            with connection.cursor() as cursor:
                current_entities = []
                sql = f"SELECT * FROM {table_name}"
                cursor.execute(sql)
                result = cursor.fetchall()

                for row in result:
                    customer = entity_class.from_dict(row)
                    current_entities.append(customer)
                load_entities_repo(table_name, current_entities)
