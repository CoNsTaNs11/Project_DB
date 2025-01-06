from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Таблица "События"
class Events(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    place = Column(String, nullable=False)  # Место
    city = Column(String, nullable=False)  # Город
    date = Column(Date, nullable=False)  # Дата
    duration = Column(Integer, nullable=False)  # Длительность
    quality = Column(Float, nullable=False)  # Качество
    danger_level = Column(Integer, nullable=False)  # Степень опасности
    event_type = Column(String, nullable=False)  # Тип события

    reports = relationship("Reports", back_populates="event")  # Связь с "Репортажи"

# Таблица "Репортажи"
class Reports(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)  # Связь с "События"
    release_time = Column(String, nullable=False)  # Время выпуска новостей
    has_video = Column(Boolean, default=False)  # Наличие видеокадров

    event = relationship("Events", back_populates="reports")  # Связь с "События"
    correspondents = relationship("Correspondents", back_populates="report")  # Связь с "Корреспонденты"

# Таблица "Корреспонденты"
class Correspondents(Base):
    __tablename__ = "correspondents"
    id = Column(Integer, primary_key=True, index=True)
    fio = Column(String, nullable=False)  # ФИО
    salary = Column(Float, nullable=False)  # Зарплата
    country = Column(String, nullable=False)  # Страна
    city = Column(String, nullable=False)  # Город
    operator = Column(Boolean, default=False)  # Личный оператор
    specifics = Column(String, nullable=False)  # Специфика
    report_id = Column(Integer, ForeignKey("reports.id"), nullable=False)  # Связь с "Репортажи"

    report = relationship("Reports", back_populates="correspondents")  # Связь с "Репортажи"
