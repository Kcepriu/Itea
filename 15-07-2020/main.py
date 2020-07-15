from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

persons =[
    {
        'name': 'Jon',
        'surname': 'Jonson',
        'age':12
    }
]

@app.route('/persons', methods=['GET', 'POST'])
def persons_app():
    template = render_template('index.html', persons=persons)
    if request.method == 'GET':
        return render_template('index.html', persons=persons)
    elif request.method == 'POST':
        persons.append(request.form)
        return redirect(url_for('persons_app'))


app.run(debug=True)