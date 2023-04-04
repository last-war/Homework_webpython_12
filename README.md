# Homework_webpython_11

Домашнее задание #11

Цель этого домашнего задания — создать REST API для хранения и управления контактами. API должен быть построен с использованием инфраструктуры FastAPI и использовать SQLAlchemy для управления базой данных.

Контакты должны храниться в базе данных и должны включать следующую информацию:

    Имя
    Фамилия
    Электронный адрес
    Номер телефона
    День рождения
    Дополнительные данные (необязательно)

API должен иметь возможность выполнять следующие действия:

    Создать новый контакт
    Получить список всех контактов
    Получить один контакт по идентификатору
    Обновите существующий контакт
    Удалить контакт

В дополнение к базовой функциональности CRUD API также должен иметь следующие функции:

    Контакты должны быть доступны для поиска по имени, фамилии или адресу электронной почты (Query).
    API должен быть в состоянии получить список контактов с предстоящими днями рождения в течение следующих 7 дней.

Общие требования

    Использование фреймворка FastAPI для создания API
    Использование ORM SQLAlchemy для работы с базой данных
    В качестве базы данных должна использоваться PostgreSQL.
    Поддержка CRUD операций для контактов
    Поддержка хранения даты рождения контакта
    Предоставление документации для API
    Использование модуля валидации данных Pydantic
 
