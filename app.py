from flask import Flask, request, render_template
import os
from line import Circuit
from logzero import logger
from mutator import RandomMutator, UCNOTMutator, QFTMutator

def func(number, method):
    if method == "UCNOT":
        result = generate(number, UCNOTMutator())
    elif method == "IQFT":
        result = generate(number, QFTMutator())
    elif method == "Random":
        result = generate(number, RandomMutator())
    return result

def generate(num_qubits, mutator):
    circuit = Circuit(num_qubits)
    new_circuit = mutator.generate_circuit(circuit)
    return new_circuit.code.qasm()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_number = int(request.form["number"])
        method = request.form['method']
        processed_number = func(selected_number, method)
        return render_template("index.html", selected_number=selected_number, processed_number=processed_number)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port = '30003')
