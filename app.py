from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate():
    result = None
    if request.method == "POST":
        a = float(request.form['a'])
        b = float(request.form['b'])
        op = request.form['operation']
        try:
            if op == "+":
                result = a + b
            elif op == "-":
                result = a - b
            elif op == "*":
                result = a * b
            elif op == "/":
                result = a / b
        except Exception as e:
            result = f"Error: {e}"
    return render_template("calc.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)