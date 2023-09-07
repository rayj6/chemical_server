from flask import Flask, request, jsonify
from chempy import balance_stoichiometry
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/balance', methods=['POST'])
def balance():
    # Get the chemical equation from the POST request
    data = request.json  # Assuming data is sent in JSON format

    equation = data.get('equation')  # Assuming 'equation' is the key for the equation in the JSON data
    print(equation)
    # return(equation)

    # Split the equation into reactants and products
    reactants, products = equation.split('=')

    # Parse and clean up reactants and products
    def parse_compounds(compound_str):
        compounds = compound_str.strip().split('+')
        return {c.strip(): 1 for c in compounds}

    reactants = parse_compounds(reactants)
    products = parse_compounds(products)

    # Balance the equation
    coefficients = balance_stoichiometry(reactants, products)

    # Prepare the balanced equation
    reactant_str = ' + '.join(f"{coeff} {compound}" for compound, coeff in coefficients[0].items())
    product_str = ' + '.join(f"{coeff} {compound}" for compound, coeff in coefficients[1].items())
    balanced_equation = f"{reactant_str} = {product_str}"

    return jsonify({"balanced_equation": balanced_equation})


@app.route('/')
def home():
    return ("This is the chemical equation balance server")

if __name__ == '__main__':
    os.system("clear")
    app.run(debug=True,  use_reloader=False)
