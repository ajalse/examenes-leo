from flask import Flask, render_template, request

app = Flask(__name__)

# Aquí defines las respuestas correctas
RESPUESTAS = {
    "p1": "b",
    "p2": "a",
    "p3": "c"
}

@app.route("/", methods=["GET"])
def examen():
    return render_template("examen.html")

@app.route("/corregir", methods=["POST"])
def corregir():
    puntuacion = 0
    for pregunta, correcta in RESPUESTAS.items():
        if request.form.get(pregunta) == correcta:
            puntuacion += 1
    return f"Tu puntuación es: {puntuacion}"

if __name__ == "__main__":
    app.run()

