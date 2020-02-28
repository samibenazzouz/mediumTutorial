from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def hello():
    if request.method == 'POST':
        firstInput = request.form['pythonFirstInput']
        secondInput = request.form['pythonSecondInput']
        print(firstInput,secondInput)
        myOutput=firstInput+secondInput
        return render_template("result.html",myHtmlOutput=myOutput)
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
