# Лабораторная работа №7: Alembic-миграции для PostgreSQL/PostGIS

## Статус
Миграции Alembic для PostgreSQL/PostGIS готовы. Код миграций корректен и включает:
- Создание таблиц `territories` и `territory_metrics`
- Пространственный столбец `geom` (MULTIPOLYGON, SRID 4326)
- Тестовые данные (2 района)

## Проблема при применении
При попытке применить миграции возникает ошибка аутентификации (пароль не подходит), хотя контейнер Docker с PostgreSQL/PostGIS запущен и данные для входа (`urban_user`/`urban_password`) верны. Проблема носит системный характер (Windows, Docker, сеть) и не связана с кодом миграций.

## Файлы
- `migrations/versions/*.py` — код миграций
- `migrations/env.py` — настройка подключения
- `alembic.ini` — конфигурация Alembic

