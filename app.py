from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        x = float(request.form['x'])
        y = float(request.form['y'])
        operation = request.form['operation']

        if operation == 'add':
            result = add(x, y)
        elif operation == 'subtract':
            result = subtract(x, y)
        elif operation == 'multiply':
            result = multiply(x, y)
        elif operation == 'divide':
            result = divide(x, y)
        else:
            result = "Invalid operation"
        
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
