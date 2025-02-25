from flask import Flask, g, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect
import forms 

app = Flask(__name__)
app.secret_key="Esta es la clave secreta"
csrf = CSRFProtect()

@app.errorhandler(400)
def page_not_found(e):
        return render_template('400.html'), 404
    
@app.before_request
def before_request():
     g.nombre="Mario"
     print('Before request 1')
    
@app.after_request
def after_request(response):
    print(' After request 3')
    return response


@app.route('/')
def index():
    grupo = "IDGS803"
    lista = ["Juan", "Pedro", "mario"]
    print("Index 2")
    print("Hola {}".format(g.nombre))
    return render_template('index.html', grupo=grupo, lista=lista)


@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
    mat=''
    nom=''
    edad=''
    correo=''
    ape=''
    alumno_class=forms.UserForm(request.form)
    if request.method=='POST' and alumno_class.validate():
        mat=alumno_class.matricula.data
        nom=alumno_class.nombre.data
        ape=alumno_class.apellidos.data
        edad=alumno_class.edad.data
        correo=alumno_class.email.data
        mensaje='Bienvenidos {}'.format(nom)
        flash(mensaje)
    return render_template("alumnos.html", form=alumno_class, mat=mat, nom=nom, ape=ape, edad=edad, correo=correo)

    


@app.route('/OperasBas')
def operas():
    return render_template('OperasBas.html')


@app.route('/resultado', methods=['GET', 'POST'])
def resultado():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "La suma de {} + {} es: {}".format(num1, num2, int(num1)+int(num2))

@app.route('/ejemplo1')
def ejemplo1():
    return render_template('ejemplo1.html')

@app.route('/ejemplo2')
def ejemplo2():
    return render_template('ejemplo2.html')

@app.route("/hola")
def hola():
    return "Hola!!!!"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola {user}!!!"

@app.route("/numero/<int:n>")
def numero(n): 
    return f"Numero {n}"

@app.route("/user/<string:user>/<int:id>")
def username(user, id):
    return f"Nombre; {user} ID: {id}!!!"
 
@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma es: {}!!".format(n1+n2)

@app.route("/form1")
def form1():
    return '''
        <form>
            <label>Nombre:</label>
            <input type="text" name="nombre" placeholder="Nombre">
            </br>
            <label>Apellido</label>
            <input type="text" name="nombre" placeholder="Nombre">
            </br>
        </form>
    '''

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True) 