from flask import Flask, request, render_template
import os
from line import Circuit
from mutator import RandomMutator

def func(number):
    return generate(number)

def generate(num_qubits):
    mutator = RandomMutator()
    circuit = Circuit(num_qubits)
    new_circuit = mutator.generate_circuit(circuit)
    return new_circuit.code.qasm()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_number = int(request.form["number"])
        processed_number = func(selected_number)
        return render_template("return.html", selected_number=selected_number, processed_number=processed_number)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port = '30001', debug=True)
