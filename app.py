from flask import Flask, request, redirect, render_template

app = Flask(__name__, static_folder='styles', static_url_path='/styles')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    if email == 'admin' and password == '1234':
        return redirect('/inicio_admin')
    else:
        return "<h2>Acceso denegado</h2><a href='/'>Volver al inicio</a>"

@app.route('/inicio_admin')
def inicio_admin():
    return render_template('inicio_admin.html')

if __name__ == '__main__':
    app.run(debug=True)