from flask import Flask, render_template, request


app = Flask(__name__, template_folder='.')


def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m * height_m)


def bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    if bmi < 25:
        return 'Normal weight'
    if bmi < 30:
        return 'Overweight'
    return 'Obesity'


@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    bmi = None
    category = None
    error = None
    weight = ''
    height = ''

    if request.method == 'POST':
        weight = request.form.get('weight', '').strip()
        height = request.form.get('height', '').strip()

        try:
            weight_kg = float(weight)
            height_m = float(height)

            if weight_kg <= 0 or height_m <= 0:
                raise ValueError

            bmi = calculate_bmi(weight_kg, height_m)
            category = bmi_category(bmi)
        except ValueError:
            error = 'Please enter valid positive numbers for weight and height.'

    return render_template(
        'BMIcalculator.html',
        bmi=bmi,
        category=category,
        error=error,
        weight=weight,
        height=height,
    )


if __name__ == '__main__':
    app.run(debug=True, port=5001)