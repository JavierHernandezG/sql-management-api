# from injector import Injector
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    environment: str = "local"

    # service-to-service token timeout
    s2s_timeout: float = None

    cloud_logging_enable: bool = False

    # db config
    postgres_user: str
    postgres_pass: str
    postgres_host: str
    postgres_port: int
    postgres_db: str

    # TODO
    # @property
    # def injector(self) -> Injector:
    #    from dependencies import injectors
    #    return injectors[self.environment]

    class Config:
        env_prefix = "sql_manager_"
