from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
    #return "<html><body><h1>Menu</h1><p><a href='./contactos'>Contactos</a></p> <p><a href='./servicios'>Servicios</a></p> <p><a href='./estudiantes'>Estudiantes</a></p> <p><a href='./cursos'>Cursos</a></p> <p><a href='./about'>Acerca de</a></p><body></html>"
    return render_template("inicio.html")

@app.route("/contactos")
def contactos():
    return "<html><body><h1>Contactos</h1><ul> <li>Javier</li> <li>Daniel</li> <li>Patricia</li> <li>Simón</li> <li>Juan</li> </ul><p><a href='/'>Regresar</a></p></body></html>"

@app.route("/servicios")
def servicios():
    return "<html><body><h1>Servicios</h1><ul> <li>s1</li> <li>s2</li> <li>s3</li> <li>s4</li> <li>s5</li> </ul><p><a href='/'>Regresar</a></p></body></html>"

@app.route("/estudiantes")
def estudiantes():
    return "<html><body><h1>Estudiantes</h1><ul> <li>e1</li> <li>e2</li> <li>e3</li> <li>e4</li> <li>e5</li> </ul><p><a href='/'>Regresar</a></p></body></html>"

@app.route("/cursos")
def cursos():
    return "<html><body><h1>Cursos</h1><ul> <li>c1</li> <li>c2</li> <li>c3</li> <li>c4</li> <li>c5</li> </ul><p><a href='/'>Regresar</a></p></body></html>"

@app.route("/about")
def about():
    return "<html><body><h1>Acerca de</h1><p>Sitio desarrollado con python+flask.</p><p><a href='/'>Regresar</a></p></body></html>"

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"<html><body><h1>Saludo</h1><p>Hola, {nombre}</p><p><a href='/'>Regresar</a></p></body></html>"

@app.route("/hobbies")
def hobbies():
    #return "<html><body><h1>Menu</h1><p><a href='./contactos'>Contactos</a></p> <p><a href='./servicios'>Servicios</a></p> <p><a href='./estudiantes'>Estudiantes</a></p> <p><a href='./cursos'>Cursos</a></p> <p><a href='./about'>Acerca de</a></p><body></html>"
    return render_template("hobbies.html")

if __name__ == "__main__":
    app.run(debug=True)