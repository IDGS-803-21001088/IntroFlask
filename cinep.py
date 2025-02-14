from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/cinepolis', methods=['GET', 'POST'])
def cine():
    if request.method == 'POST':
        nombre = request.form.get("n1")
        cantidad_compradores = int(request.form.get("cantidadc"))
        cantidad_boletos = int(request.form.get("cantidadb"))
        tarjeta = request.form.get("tarjeta")
        
        precio_boleta = 12.000
        total_sin_descuento = cantidad_boletos * precio_boleta
        if cantidad_boletos > 5:
            descuento = 0.15
        elif 3 <= cantidad_boletos <= 5:
            descuento = 0.10
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento * (1 - descuento)

        if tarjeta == "opcion1":  
            total_con_descuento *= 0.90

        return render_template('Cinepolis.html', total=total_con_descuento, nombre=nombre)
    return render_template('Cinepolis.html', total=None)

if __name__ == '__main__':
    app.run(debug=True)
