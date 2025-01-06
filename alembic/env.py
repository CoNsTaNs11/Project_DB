from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from app.database import Base  # импорт вашей базы данных (моделей)

# Эта строка будет подключать ваши модели в Alembic
target_metadata = Base.metadata

# Открытие конфигурационного файла Alembic
config = context.config

# Настройка соединения с базой данных
config.set_main_option('sqlalchemy.url', 'postgresql://postgres:your_password@localhost/your_database')

# Конфигурация логирования
fileConfig(config.config_file_name)

# Создание подключения и миграций
engine = engine_from_config(config.get_section(config.config_ini_section), prefix='sqlalchemy.')
connection = engine.connect()
context.configure(
    connection=connection,
    target_metadata=target_metadata
)

# Генерация миграций
with context.begin_transaction():
    context.run_migrations()
