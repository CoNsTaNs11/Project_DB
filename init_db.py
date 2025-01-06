from sqlalchemy import create_engine
from app.models import Base

# Укажите настройки подключения к базе данных
DATABASE_URL = "postgresql://postgres:23042004@localhost:5411/variant_13_db"

# Создаем объект подключения к базе данных
engine = create_engine(DATABASE_URL)

def init_database():
    """
    Функция для инициализации базы данных:
    - Создает таблицы, определенные в models.py.
    """
    Base.metadata.create_all(bind=engine)
    print("База данных успешно инициализирована!")

if __name__ == "__main__":
    init_database()
