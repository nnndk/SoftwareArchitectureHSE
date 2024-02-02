import psycopg2
from databaseTools.DbConnector import DbConnector
from config.config import Config


class DbPostgresConnector(DbConnector):
    _CONFIG_DB_SECTION_NAME = 'POSTGRES'

    @staticmethod
    def get_connection():
        connection = psycopg2.connect(
            host=Config.get_config_item(DbPostgresConnector._CONFIG_DB_SECTION_NAME, 'HOST'),
            user=Config.get_config_item(DbPostgresConnector._CONFIG_DB_SECTION_NAME, 'USER'),
            password=Config.get_config_item(DbPostgresConnector._CONFIG_DB_SECTION_NAME, 'PASSWORD'),
            database=Config.get_config_item(DbPostgresConnector._CONFIG_DB_SECTION_NAME, 'DATABASE')
        )

        return connection

    @staticmethod
    def get_db_fields(fields: list[str]) -> list[str]:
        return ['"' + field + '"' for field in fields]

    @staticmethod
    def get_db_values(values: list[str]) -> list[str]:
        return ['\'' + val + '\'' for val in values]

    @staticmethod
    def get_json_query(query: str) -> str:
        return f'SELECT row_to_json(row) FROM ({query}) row;'
