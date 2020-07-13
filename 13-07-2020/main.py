from flask import Flask, render_template, abort

app = Flask(__name__)

products_db = {
    'tomato': {'price':30, 'description':'Tomato description',
               'available_in':['ATB', 'Fora']},

    'potato': {'price': 200, 'description': 'Potato description',
               'available_in': ['Silpo', 'Megamarket']}

}
@app.route('/hello')
@app.route('/')
def hello():
    info = {'a':'Test ttttttt'}
    # {info["a"]}
    return render_template('index.html', info=info)

@app.route('/products')
def products():
    return render_template('products_list.html', products=products_db)

@app.route('/products/<product_name>')
def product(product_name):
    try:
        product_info = products_db[product_name]
    except KeyError:
        abort(404)
    else:
        return render_template('product_page.html', product_name=product_name, product_info=product_info)




app.run(debug=True)