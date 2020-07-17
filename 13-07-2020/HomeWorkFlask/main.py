from flask import Flask, render_template, abort,  request, redirect, url_for
from db_connecn import Databases
import sqlite3

app = Flask(__name__)
databases = Databases('db_tovars2.db')

@app.route('/')
def root():
    text_sql = databases.dict_query.get('select_all_categories', '')
    categories = databases.execute_sql(text_sql, fetch_all=True)
    return render_template('index.html', categories=categories)

@app.route('/categories/<name_categiry>')
def product_list(name_categiry):
    print(name_categiry)
    text_sql = databases.dict_query.get('select_product_from_name_category', '')
    products = databases.execute_sql(text_sql, [name_categiry], fetch_all=True)
    if not products:
        text_sql = databases.dict_query.get('select_categories_from_name', '')
        if not databases.execute_sql(text_sql, [name_categiry]):
            abort(404)

    return render_template('categories_page.html', name_categiry=name_categiry, products=products)

@app.route('/product/<id>')
def product(id):
    text_sql = databases.dict_query.get('select_product_from_id', '')
    product = databases.execute_sql(text_sql, [id])
    if not product:
        abort(404)
    return render_template('product_page.html', product=product)


@app.route('/new_categories',  methods=['GET', 'POST'])
def new_categories(texts=''):

    template = render_template('new_categories.html', texts=texts)

    if request.method == 'GET':
        return render_template('new_categories.html', texts=texts)
    elif request.method == 'POST':
        name_categiry = request.form['name_categiry']

        if name_categiry:
            text_sql = databases.dict_query.get('insert_categories', '')

            try:
                databases.execute_sql(text_sql, [name_categiry], commit=True)
            except sqlite3.IntegrityError:
                return render_template('new_categories.html', texts=f'{name_categiry} - вже є така категорія')
        else:
            return render_template('new_categories.html', texts='Введіть імʼя нової категорії')
        return redirect(url_for('root'))

@app.route('/new_tovar/<name_categiry>',  methods=['GET', 'POST'])
def new_tovar(name_categiry):
    text_sql = databases.dict_query.get('select_categories_from_name', '')
    result_sql = databases.execute_sql(text_sql, [name_categiry])
    if result_sql:
        id_catgory = result_sql['id']
    else:
        abort(404)

    template = render_template('add_tovar.html', name_categiry=name_categiry)

    if request.method == 'GET':
        return render_template('add_tovar.html', name_categiry=name_categiry)
    elif request.method == 'POST':
        text_sql = databases.dict_query.get('insert_product', '')
        try:
            databases.execute_sql(text_sql, [request.form['name'], id_catgory, request.form['price'],
                                                      request.form['quantity'], request.form.get('on_the_market', 0)],
                                           commit=True)
        except sqlite3.DatabaseError:
                return render_template('add_tovar.html', name_categiry=name_categiry, text='Помилка запиту до бази')

    return product_list(name_categiry)

app.run(debug=True)










