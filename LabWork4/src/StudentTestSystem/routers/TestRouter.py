from fastapi import APIRouter, status
from datetime import datetime
from databaseTools.DbPostgresConnector import DbPostgresConnector
from models.TestModel import TestModel

TestRouter = APIRouter(
    prefix='/tests'
)

test_fields = ['Id', 'Name', 'CreationDate']
test_fields_db = DbPostgresConnector.get_db_fields(test_fields)


def test_exists(cursor: any, id: int) -> bool:
    cursor.execute(
        DbPostgresConnector.get_json_query(f'SELECT {test_fields_db[0]} FROM public."Test" '
                                           f'WHERE "Id" = \'{id}\' and "Deleted" = false')
    )
    result = cursor.fetchone()

    return result is not None


@TestRouter.get('/', status_code=status.HTTP_200_OK)
def get_all_tests():
    # need to add pagination later
    connection = DbPostgresConnector.get_connection()

    with connection.cursor() as cursor:
        cursor.execute(
            DbPostgresConnector.get_json_query(f'SELECT {", ".join(test_fields_db)} FROM public."Test" '
                                               f'WHERE "Deleted" = false')
        )
        result = cursor.fetchall()
        result = [item[0] for item in result]

        return result


@TestRouter.get('/{id}', status_code=status.HTTP_200_OK)
def get_test_by_id(id: str):
    if id is None or not id.isdigit():
        return status.HTTP_400_BAD_REQUEST

    connection = DbPostgresConnector.get_connection()

    with connection.cursor() as cursor:
        cursor.execute(
            DbPostgresConnector.get_json_query(f'SELECT {", ".join(test_fields_db)} FROM public."Test" '
                                               f'WHERE "Id" = \'{id}\' and "Deleted" = false')
        )
        result = cursor.fetchone()

        if result is None:
            return status.HTTP_404_NOT_FOUND

        return result[0]


@TestRouter.post('/', status_code=status.HTTP_201_CREATED)
def create_test(test: TestModel):
    connection = DbPostgresConnector.get_connection()

    with connection.cursor() as cursor:
        if test.name is None or test.name == '':
            return status.HTTP_400_BAD_REQUEST

        new_test_data = DbPostgresConnector.get_db_values([test.name])
        #new_test_data.append(str(datetime.now()))

        cursor.execute(
            f'INSERT INTO public."Test"({", ".join(test_fields_db[1:len(test_fields_db) - 1])}) '
            f'VALUES ({", ".join(new_test_data)});'
        )
        connection.commit()

        return status.HTTP_201_CREATED


@TestRouter.put('/{id}', status_code=status.HTTP_200_OK)
def edit_test(id: str, test: TestModel):
    if id is None or not id.isdigit():
        return status.HTTP_400_BAD_REQUEST

    connection = DbPostgresConnector.get_connection()

    with connection.cursor() as cursor:
        result = test_exists(cursor, int(id))

        if not result:
            return status.HTTP_404_NOT_FOUND

        updated_test_data = DbPostgresConnector.get_db_values([test.name])
        updated_cols = ''

        for i in range(len(updated_test_data)):
            # skip first because it is snils, it cannot be modified
            updated_cols += test_fields_db[i + 1] + ' = ' + updated_test_data[i] + ', '

        updated_cols = updated_cols.strip()[:-1]

        cursor.execute(
            f'UPDATE public."Test" '
            f'SET {updated_cols} '
            f'WHERE "Id" = \'{id}\';'
        )
        connection.commit()

        return status.HTTP_200_OK


@TestRouter.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user_by_snils(id: str):
    if id is None or not id.isdigit():
        return status.HTTP_400_BAD_REQUEST

    connection = DbPostgresConnector.get_connection()

    with connection.cursor() as cursor:
        result = test_exists(cursor, int(id))

        if not result:
            return status.HTTP_404_NOT_FOUND

        cursor.execute(
            #f'DELETE FROM public."Test" WHERE "Id" = \'{id}\'' # completely delete
            f'UPDATE public."Test" '
            f'SET "Deleted" = true '
            f'WHERE "Id" = \'{id}\';'
        )
        connection.commit()

        return status.HTTP_204_NO_CONTENT
