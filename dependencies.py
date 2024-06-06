import logging

from injector import Injector, Module, provider, singleton
from settings import Settings
from sqlalchemy import Engine

# TODO injectors, settings and pytest


class ProductionModule(Module):
    @singleton
    @provider
    def settings(self) -> Settings:
        return Settings()

    @singleton
    @provider
    def make_logger(self, settings: Settings) -> logging.Logger:
        logger = logging.getLogger(settings.app_name)
        default_log_level = logging.INFO
        if settings.cloud_logging_enable:
            pass
        else:
            logging.basicConfig(
                level=default_log_level,
                format="[%(asctime)s] %(levelname)s - %(message)s",
                datefmt="%m/%d/%Y %I:%M:%S %p",
            )
        return logger

    @singleton
    def psql_engine(self, settings: Settings) -> Engine:
        import sqlalchemy as sa

        # return sa.engine_from_config(settings.json)
        return sa.create_engine(
            f"postgresqsl+psycopg2://{settings.postgres_user}:{settings.postgres_pass}@{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_db}"
        )


class GcpEmulatorModule(ProductionModule):
    pass


local_injector = Injector([GcpEmulatorModule])

injectors = {"local": local_injector}
