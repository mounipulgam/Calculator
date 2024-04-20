from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    # Initialize the expression
    expression = ""

    if request.method == 'POST':
        # Get the button value from the form
        button_value = request.form.get('button')
        
        # Get the current expression from the form
        current_expression = request.form.get('expression', '')

        # Calculate the result
        if button_value == 'C':
            # Clear the expression
            expression = ""
        elif button_value == '=':
            # Evaluate the expression
            try:
                expression = str(eval(current_expression))
            except Exception as e:
                expression = "Error"
        else:
            # Append button value to the current expression
            if button_value is not None:
                expression = current_expression + button_value

    return render_template('calculator.html', expression=expression)

if __name__ == '__main__':
    app.run(debug=True)
