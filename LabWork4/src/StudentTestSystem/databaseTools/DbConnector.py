from abc import ABC, abstractmethod


class DbConnector(ABC):
    @staticmethod
    @abstractmethod
    def get_connection() -> any:
        # Example: it returns psycopg2.connect(...) object for postgres
        pass

    @staticmethod
    @abstractmethod
    def get_db_fields(fields: list[str]) -> list[str]:
        pass

    @staticmethod
    @abstractmethod
    def get_db_values(values: list[str]) -> list[str]:
        pass

    @staticmethod
    @abstractmethod
    def get_json_query(query: str) -> str:
        pass
