from flask import Flask, app, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/imc", methods = ['GET', 'POST'])
def calcular_imc():
    nome = None    
    massa = None
    altura = None
    imc = None
    diagnostico = None
    result = ""
    if request.method == "POST":
        nome = request.form.get("nome", "")
        massa = float(request.form.get("massa", 0.0).replace(",","."))
        altura = float(request.form.get("altura", 0.0).replace(",","."))
        imc = massa / (altura ** 2)
        

        if imc < 18.5:
            diagnostico = "Vc está abaixo do peso ideal."
        elif imc < 25:
            diagnostico = "Vc está com peso ideal."
        elif imc < 30:
            diagnostico = "Vc está acima do peso ideal."
        elif imc < 35:
            diagnostico = "Vc está obeso."
        elif imc < 40:
            diagnostico = "Vc está com obesidade nivel 2."
        else:
            diagnostico = "Vc está com obesidade nivel 3."
        result = f"{nome}, seu IMC é: {imc:.2f}. {diagnostico}"      

    return render_template("index.html", nome=nome, imc=imc, result=result, diagnostico=diagnostico)

if __name__ == "__main__":
    app.run(debug=True)