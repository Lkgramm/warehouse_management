## 📦 warehouse-management

**Система управления складом**, реализованная с использованием принципов **Чистой архитектуры** и SQLAlchemy.

Позволяет управлять товарами, заказами и клиентами через интерфейс командной строки (CLI).

---

### 🧩 Возможности

- **Добавление товаров**
- **Создание заказов на основе товаров**
- **Регистрация клиентов и привязка к ним заказов**
- **Просмотр списка клиентов с информацией о заказах**
- **Защита от некорректного ввода пользователя**


---

### 🚀 Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/yourname/warehouse-management.git
cd warehouse-management
```

2. Установите зависимости:

```bash
make install
```

3. Запустите приложение:

```bash
make run
```

---

### 🖥 Интерфейс командной строки

После запуска вы увидите главное меню:

```
Welcome to Warehouse Management System!

Choose operation:
1 - Add product
2 - Add order
3 - Add customer
4 - Get customers list
5 - Exit
```

#### 1. Добавление товара

Выберите пункт `1`.

Пример:

```
Product name: Laptop
Product quantity: 10
Product price: 1500
```

Результат:

```
Product created: Product(id=None, name='Laptop', quantity=10, price=1500.0)
```

#### 2. Создание заказа

Выберите пункт `2`.  
Введите ID продуктов, разделённые запятыми:

```
Enter product IDs separated by commas: 1
```

Результат:

```
Order created: Order(id=1, products=[Product(id=1, name='Laptop', quantity=10, price=1500.0)])
```

#### 3. Добавление клиента

Выберите пункт `3`.

Пример:

```
Customer name: Alice
Order ids (separate by comma): 1
```

Результат:

```
New customer created: Customer(id=1, name='Alice', orders=[Order(id=1, ...)])
```

#### 4. Вывод списка клиентов

Выберите пункт `4`.

Пример вывода:

```
<Customer(id=1, name='Alice', orders=[Order(id=1, ...)])
```

#### 5. Выход из программы

Выберите пункт `5`.

---

### 🛠 Makefile: основные команды

| Команда         | Описание |
|----------------|----------|
| `make install` | Установка зависимостей |
| `make dev`     | Установка dev-зависимостей |
| `make test`    | Запуск тестов |
| `make lint`    | Проверка стиля кода |
| `make format`  | Форматирование кода |
| `make typecheck` | Проверка типов через `mypy` |
| `make run`     | Запуск CLI-приложения |

---

### ✅ Требования

- Python 3.11+
- Poetry
- SQLite (используется по умолчанию)

---

### 🧪 Тестирование

Проект покрыт юнит-тестами:

- Создание продуктов
- Получение объектов из БД
- Работа с клиентами и заказами

Запуск тестов:

```bash
make test
```

---

### 📁 Архитектура проекта

- **`domain/`** — бизнес-логика, модели домена, интерфейсы репозиториев
- **`infrastructure/`** — реализация через SQLAlchemy
- **`tests/`** — модульные и интеграционные тесты
- **`main.py`** — точка входа, CLI-интерфейс
- **`Makefile`** — автоматизация задач

---

