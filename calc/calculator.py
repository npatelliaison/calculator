from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def input():
    return render_template('input.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    return render_template('result.html', n1=num1, n2=num2)
    
if __name__ == '__main__':
    app.run(debug=True)