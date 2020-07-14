from flask import Flask, render_template, abort
from db_connecn import Databases

app = Flask(__name__)
databases = Databases('db_tovars1.db')

@app.route('/')
def root():
    text_sql = databases.dict_query.get('select_all_categories', '')
    categories = databases.execute_sql(text_sql, fetch_all=True)
    return render_template('index.html', categories=categories)

@app.route('/categories/<name_categiry>')
def product_list(name_categiry):
    text_sql = databases.dict_query.get('select_product_from_name_category', '')
    products = databases.execute_sql(text_sql, [name_categiry], fetch_all=True)
    if not products:
        text_sql = databases.dict_query.get('select_categories_from_name', '')
        if not databases.execute_sql(text_sql, [name_categiry]):
            abort(404)

    return render_template('products.html', name_categiry=name_categiry, products=products)

@app.route('/product/<id>')
def product(id):
    text_sql = databases.dict_query.get('select_product_from_id', '')
    product = databases.execute_sql(text_sql, [id])
    if not product:
        abort(404)
    return render_template('product_page.html', product=product)


app.run(debug=True)










