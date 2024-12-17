from flask import Flask, render_template, jsonify, request  # Added imports
import webbrowser


app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for generating multiplication table
@app.route('/table/<int:number>', methods=['GET'])
def table(number):
    table = [f"{number} x {i} = {number * i}" for i in range(1, 11)]
    return jsonify({'result': '<br>'.join(table)})

# Route for basic calculations
@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form.get('num1'))
    num2 = float(request.form.get('num2'))
    operation = request.form.get('operation')
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            return jsonify({'error': 'Division by zero is not allowed'})
        result = num1 / num2
    else:
        return jsonify({'error': 'Invalid operation'})
    
    return jsonify({'result': result})



# def open_browser():
#     webbrowser.open('http://127.0.0.1:5000/')


if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=True, use_reloader=False)

