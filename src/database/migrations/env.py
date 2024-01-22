from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

from src.database.connection import database_url, Base
from src.database.models.apps import App, AppCurrent
from src.database.models.arp_table import ArpTable, ArpTableCurrent
# from src.database.models.count_packet import CountPacketsAll, CountPacketsInput, CountPacketsOutput
from src.database.models.hosts import Hosts, HostsCurrent
from src.database.models.interfaces import NetworkInterfaces, NetworkInterfacesCurrent
from src.database.models.monitor_resources import MonitorResources
from src.database.models.ports import Ports, PortsCurrent
from src.database.models.sfc import SFC, SFCCurrent
from src.database.models.system_services import SystemServices, SystemServicesCurrent
from src.database.models.connections import Connections, ConnectionsCurrent

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

config.set_main_option("sqlalchemy.url", database_url)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_server_default=True
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
