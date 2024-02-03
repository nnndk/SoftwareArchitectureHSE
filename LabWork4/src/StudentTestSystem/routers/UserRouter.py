from fastapi import APIRouter, status
from databaseTools.DbPostgresConnector import DbPostgresConnector
from models.UserModel import UserModel

UserRouter = APIRouter(
    prefix='/users'
)

user_fields = ['SNILS', 'Login', 'Email', 'HashPassword', 'Name', 'Surname', 'Patronymic', 'RoleId']
user_fields_db = DbPostgresConnector.get_db_fields(user_fields)


def user_exists(cursor: any, snils: str, check_deleted: bool = False) -> bool:
    cursor.execute(
        DbPostgresConnector.get_json_query(f'SELECT {user_fields_db[0]} FROM public."User" '
                                           f'WHERE "SNILS" = \'{snils}\''
                                           + 'and "Deleted" = false' if not check_deleted else '')
    )
    result = cursor.fetchone()

    return result is not None


@UserRouter.get('/', status_code=status.HTTP_200_OK)
def get_all_users():
    # need to add pagination later
    connection = DbPostgresConnector.get_connection()

    with connection.cursor() as cursor:
        cursor.execute(
            DbPostgresConnector.get_json_query(f'SELECT {", ".join(user_fields_db)} FROM public."User" '
                                               f'WHERE "Deleted" = false')
        )
        result = cursor.fetchall()
        result = [item[0] for item in result]

        return result


@UserRouter.get('/{snils}', status_code=status.HTTP_200_OK)
def get_user_by_snils(snils: str):
    if snils is None or not snils.isdigit() or len(snils) != 11:
        return status.HTTP_400_BAD_REQUEST

    connection = DbPostgresConnector.get_connection()

    with connection.cursor() as cursor:
        cursor.execute(
            DbPostgresConnector.get_json_query(f'SELECT {", ".join(user_fields_db)} FROM public."User" '
                                               f'WHERE "SNILS" = \'{snils}\' and "Deleted" = false')
        )
        result = cursor.fetchone()

        if result is None:
            return status.HTTP_404_NOT_FOUND

        return result[0]


@UserRouter.post('/', status_code=status.HTTP_201_CREATED)
def create_user(user: UserModel):
    if user.snils is None or not user.snils.isdigit() or len(user.snils) != 11:
        return status.HTTP_400_BAD_REQUEST

    connection = DbPostgresConnector.get_connection()

    with connection.cursor() as cursor:
        # it is forbidden to have two (and more) users with equal snils even if one of them is deleted (by flag)
        result = user_exists(cursor, user.snils, True)

        if result:
            return status.HTTP_409_CONFLICT

        if (user.login is None or user.email is None or user.hash_password is None or user.name is None or
                user.surname is None or user.role_id is None):
            return status.HTTP_400_BAD_REQUEST

        # place for hashing password
        new_user_data = DbPostgresConnector.get_db_values([user.snils, user.login, user.email, user.hash_password,
                                                           user.name, user.surname])
        new_user_data.append('null' if user.patronymic is None else user.patronymic)
        new_user_data.append(str(user.role_id))

        cursor.execute(
            f'INSERT INTO public."User"({", ".join(user_fields_db)}) '
            f'VALUES ({", ".join(new_user_data)});'
        )
        connection.commit()

        return status.HTTP_201_CREATED


@UserRouter.put('/{snils}', status_code=status.HTTP_200_OK)
def edit_user(snils: str, user: UserModel):
    if snils is None or not snils.isdigit() or len(snils) != 11:
        return status.HTTP_400_BAD_REQUEST

    connection = DbPostgresConnector.get_connection()

    with connection.cursor() as cursor:
        result = user_exists(cursor, snils)

        if not result:
            return status.HTTP_404_NOT_FOUND

        # place for hashing password
        updated_user_data = DbPostgresConnector.get_db_values([user.login, user.email, user.hash_password,
                                                               user.name, user.surname])
        updated_user_data.append('null' if user.patronymic is None else user.patronymic)
        updated_user_data.append(str(user.role_id))

        updated_cols = ''

        for i in range(len(updated_user_data)):
            # skip first because it is snils, it cannot be modified
            updated_cols += user_fields_db[i + 1] + ' = ' + updated_user_data[i] + ', '

        updated_cols = updated_cols.strip()[:-1]

        cursor.execute(
            f'UPDATE public."User" '
            f'SET {updated_cols} '
            f'WHERE "SNILS" = \'{snils}\';'
        )
        connection.commit()

        return status.HTTP_200_OK


@UserRouter.delete('/{snils}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user_by_snils(snils: str):
    if snils is None or not snils.isdigit() or len(snils) != 11:
        return status.HTTP_400_BAD_REQUEST

    connection = DbPostgresConnector.get_connection()

    with connection.cursor() as cursor:
        result = user_exists(cursor, snils)

        if not result:
            return status.HTTP_404_NOT_FOUND

        cursor.execute(
            #f'DELETE FROM public."User" WHERE "SNILS" = \'{snils}\'' # completely delete
            f'UPDATE public."User" '
            f'SET "Deleted" = true '
            f'WHERE "SNILS" = \'{snils}\';'
        )
        connection.commit()

        return status.HTTP_204_NO_CONTENT
