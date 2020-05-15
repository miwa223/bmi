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

        bodyshapeList = ['低体重（やせ）', '普通体重', '肥満']

        if bmi < 18.5:
            body_shape = bodyshapeList[0]
            return render_template('output.html', bmi=bmi, body_shape=body_shape)
        elif 18.5 <= bmi < 25:
            body_shape2 = bodyshapeList[1]
            return render_template('output.html', bmi=bmi, body_shape2=body_shape2)
        else:
            body_shape3 = bodyshapeList[2]
            return render_template('output.html', bmi=bmi, body_shape3=body_shape3)

    else:
        return render_template('error.html')

if __name__ == "__main__":
    app.run(debug=True, port=8080)
