from flask import Flask, request, render_template
import os
from line import Circuit
from logzero import logger
from mutator import RandomMutator

def func(number):
    result = generate(number)
    logger.debug(result)
    return result

def generate(num_qubits):
    mutator = RandomMutator()
    circuit = Circuit(num_qubits)
    new_circuit = mutator.generate_circuit(circuit)
    return new_circuit.code.qasm()
