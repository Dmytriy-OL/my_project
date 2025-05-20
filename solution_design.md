markdown_content = """
# 📄 Solution Design Document: Flask Online Shop

## 1. Project Overview

Цей проєкт є простим інтернет-магазином, створеним з використанням Flask. Користувачі можуть реєструватися, авторизовуватись, додавати товари в кошик, оформлювати замовлення та переглядати історію покупок.

## 2. Architecture Overview

- **Тип архітектури**: MVC (Model-View-Controller)
- **Frontend**: HTML, CSS (можливо Bootstrap)
- **Backend**: Python (Flask)
- **База даних**: Mongodb / MySQL (в залежності від розгортання)
- **ORM**: SQLAlchemy

## 3. Technological Stack

| Компонент      | Технологія      |
|----------------|-----------------|
| Framework      | Flask           |
| ORM            | SQLAlchemy      |
| СУБД           | Mongodb / MySQL |
| Мова           | Python 3.10+    |
| Frontend       | HTML/CSS        |

## 4. Data Model Design

### User

- `id`: Integer, Primary Key  
- `username`: String, Unique  
- `email`: String, Unique  
- `password_hash`: String  
- 🔁 Relationships:
  - `orders`: One-to-Many
  - `cart`: One-to-One

### Product

- `id`: Integer, Primary Key  
- `name`: String  
- `description`: Text  
- `price`: Float  
- `stock_quantity`: Integer  

### Cart

- `id`: Integer, Primary Key  
- `user_id`: Foreign Key → User.id  
- 🔁 Relationships:
  - `items`: One-to-Many with CartItem

### CartItem

- `id`: Integer, Primary Key  
- `cart_id`: Foreign Key → Cart.id  
- `product_id`: Foreign Key → Product.id  
- `quantity`: Integer  

### Order

- `id`: Integer, Primary Key  
- `user_id`: Foreign Key → User.id  
- `created_at`: DateTime  
- `total_price`: Float  
- 🔁 Relationships:
  - `order_items`: One-to-Many with OrderItem

### OrderItem

- `id`: Integer, Primary Key  
- `order_id`: Foreign Key → Order.id  
- `product_id`: Foreign Key → Product.id  
- `quantity`: Integer  
- `price_at_purchase`: Float  

## 5. Component Design

### User Management

- Реєстрація, логін, лог-аут  
- Перевірка авторизації  

### Product Management

- Перегляд каталогу товарів  
- Адміністрування (додавання/редагування)  

### Cart

- Додавання/видалення товарів  
- Оновлення кількості  

### Order

- Створення замовлення з кошика  
- Перегляд історії замовлень  

## 6. API Design

| Метод | Шлях              | Опис                      |
|-------|-------------------|---------------------------|
| GET   | `/products`       | Отримати всі товари       |
| POST  | `/cart/add`       | Додати товар до кошика    |
| POST  | `/order/checkout` | Оформити замовлення       |
| GET   | `/orders`         | Переглянути замовлення    |

## 7. Security Considerations

- Зберігання паролів через `werkzeug.security`  
- CSRF protection (наприклад, через Flask-WTF)  
- Валідація даних форм  
- Захищені сесії  

## 8. Future Improvements

- Email-підтвердження реєстрації  
- Ролі користувачів (admin/customer)  
- Пошук і фільтрація товарів  
"""