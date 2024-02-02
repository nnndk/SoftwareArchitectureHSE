from abc import ABC, abstractmethod


class DbConnector(ABC):
    @staticmethod
    @abstractmethod
    def get_connection() -> any:
        # Should return psycopg2.connect(...) object
        pass
