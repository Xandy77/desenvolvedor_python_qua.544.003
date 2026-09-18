from flask import Flask, render_template, request 
import pyautogui as auto
import webview

from datetime import date
import os
import sys


if getattr(sys, 'frozen', False):
    # Se o aplicativo estiver empacotado com PyInstaller
    template_folder = os.path.join(sys._MEIPASS, 'templates')

    app = Flask(__name__, template_folder=template_folder)
else:
    app = Flask(__name__)
    
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/commitar", methods = ["POST"])
def commitar():
    hoje = date.today().strftime("%d/%m/%Y")
    msg = None
    repositorio = None
    if request.method == "POST":
        repositorio = request.form.get("repositorio","")
    if repositorio:
        auto.PAUSE = 1
        auto.hotkey("win", "r")
        auto.write("cmd")
        auto.press("enter")
        auto.write(f"cd {repositorio}")
        auto.press("enter")
        auto.write("git add .")
        auto.press("enter")
        auto.write(f'git commit -m "Commit automático - {hoje}"')
        auto.press("enter")
        auto.write("git push")
        auto.press("enter")
        auto.sleep(3)
        auto.write("exit")
        auto.press("enter")    
    return render_template("index.html")

if __name__ == '__main__':
   # app.run(debug=True)
   window = webview.create_window(
        title = "PolterGit",
        url = app,
        width = 1000,
        height = 700
    )
   
   webview.start()