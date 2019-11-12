from flask import Flask, render_template, request

app = Flask('__name__')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/capture', methods=['POST'])
def capture():
    print('embedding fcn here')
    return 'success'


app.run(debug=True)
