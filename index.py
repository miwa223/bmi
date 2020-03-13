from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def input():
    return render_template('input.html')

@app.route('/output', methods=['get'])
def output():
    height = request.args.get('height', '')
    weight = request.args.get('weight', '')

    if height and weight:
        height = float(height)
        weight = float(weight)
        height = height / 100
        bmi = round(weight / height**2, 2)

        if bmi < 18.5:
            body_shape = '低体重（やせ）'
        elif 18.5 <= bmi < 25:
            body_shape = '普通体重'
        else:
            body_shape = '肥満'

    else:
        return render_template('error.html')

    return render_template('output.html', bmi=bmi, body_shape=body_shape)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
