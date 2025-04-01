from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import database
from flasgger import Swagger
import classes

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Додайте свій секретний ключ
swagger = Swagger(app)

@app.route('/add_review', methods=['POST'])
def add_review_route():
    user = session.get('user')
    if user:
        text = request.form['text']
        user_info = database.users.searching_user(user)  # Використовуємо ім'я користувача з сесії
        database.review.add_review(user_info['name'], user_info['surname'], text)
    return redirect(url_for('reviews_page'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('shop'))

@app.route('/update_profile', methods=['POST'])
def update_profile():
    user = session.get('user')
    if not user:
        return redirect(url_for('login'))

    surname = request.form['surname']
    name = request.form['name']
    email = request.form['email']
    login = request.form['login']
    password = request.form['password']

    # Оновлення інформації користувача в базі даних
    new_data = {
        "surname": surname,
        "name": name,
        "email": email,
        "login": login,
        "password": password
    }
    database.users.update_user(user, new_data)

    # Перенаправлення на сторінку профілю після оновлення
    return redirect(url_for('shop'))

@app.route('/profile', methods=['GET'])
def profile():
    user = session.get('user')
    if not user:
        return redirect(url_for('login'))

    user_information = database.users.searching_user(user)
    return render_template('profile.html', user=user_information)

def process_login(template_name):
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        if database.users.password_verification(login, password):
            session['user'] = login
            return redirect(url_for('shop'))
        error_message = "Неправильний логін або пароль. Спробуйте ще раз."
        return render_template(template_name, error_message=error_message)

    return render_template(template_name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return process_login('login.html')

@app.route('/meny_login', methods=['GET', 'POST'])
def meny_login():
    return process_login('meny_login.html')

def handle_registration():
    surname = request.form['surname']
    name = request.form['name']
    email = request.form['email']
    login = request.form['login']
    password = request.form['password']

    if not database.users.register_user(email, login):
        database.users.create_user(name, surname, email, login, password)
        session['user'] = login  # Зберігаємо логін як поточного користувача
        return redirect(url_for('shop'))
    else:
        return 'Користувач вже існує'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return handle_registration()
    return render_template('register.html')

@app.route('/meny_register', methods=['GET', 'POST'])
def meny_register():
    if request.method == 'POST':
        return handle_registration()
    return render_template('meny_register.html')

@app.route('/', methods=['GET'])
def shop():
    user = session.get('user')
    return render_template('shop.html', user=user)

@app.route('/commodity', methods=['GET'])
def commodity():
    category = request.args.get('category', '')
    products = database.product.viewing_clothes(category)
    cards_html = ""
    for i, product in enumerate(products, start=1):
        name = product['name']
        category = product['category']
        gender = product['gender']
        photo = product['photo']
        price = product['price']
        number = product['number']

        card_html = f"""
            <div class="col-md-3">
                <div class="card mb-4">
                    <img src="{photo}" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">{name}</h5>
                        <p class="card-text">Категорія: {category}</p>
                        <p class="card-text">Стать: {gender}</p>
                        <p class="card-text">Ціна: {price}</p>
                        <p class="card-text">Кількість: {number}</p>
                        <form action="/order" method="post">
                            <input type="hidden" name="category" value="{category}">
                            <input type="hidden" name="name" value="{name}">
                            <input type="hidden" name="price" value="{price}">
                            <input type="submit" value="Замовити" class="btn btn-primary">
                        </form>
                    </div>
                </div>
            </div>
        """
        cards_html += card_html
        if i % 4 == 0:
            cards_html += '</div><div class="row">'

    return render_template('commodity.html', cards_html=cards_html)

@app.route('/order', methods=['POST'])
def order():
    user = session.get('user')
    if user is None:
        category = request.form['category']
        return redirect(url_for('register'))
    else:
        category = request.form['category']
        name = request.form['name']
        price = request.form['price']
        return render_template('order.html', category=category, name=name, price=price)


@app.route('/reviews', methods=['GET'])
def reviews_page():
    """
    Отримати список відгуків
    ---
    tags:
      - Відгуки
    responses:
      200:
        description: Успішно отримано список відгуків
        schema:
          type: object
          properties:
            reviews:
              type: array
              items:
                type: object
                properties:
                  name:
                    type: string
                    description: Ім'я користувача
                  surname:
                    type: string
                    description: Прізвище користувача
                  text:
                    type: string
                    description: Текст відгуку
    """
    user = session.get('user')
    reviews = database.review.get_all_reviews()
    return render_template('reviews.html', reviews=reviews, user=user)

@app.route('/like_review', methods=['POST'])
def like_review_route():
    """
    Лайк відгуку
    ---
    tags:
      - Відгуки
    parameters:
      - name: review_id
        in: body
        type: integer
        required: true
        description: ID відгуку
    responses:
      200:
        description: Успішно лайкнуто відгук
        schema:
          type: object
          properties:
            likes:
              type: integer
              description: Новий кількість лайків
      401:
        description: Користувач не авторизований
    """
    user = session.get('user')
    if user:
        review_id = request.json.get('review_id')
        likes = database.review.like_review(review_id)
        return jsonify({'likes': likes})
    return jsonify({'error': 'Unauthorized'}), 401


if __name__ == '__main__':
    print("Запустіть додаток і перегляньте API-документацію за адресою: http://127.0.0.1:5000/apidocs/")
    app.run(debug=True)
