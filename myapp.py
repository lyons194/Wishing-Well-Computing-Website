from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('about.html')

@app.route('/contribute/')
def contribute():
    return render_template('contribute.html')

@app.route('/help/')
def help():
    return render_template('help.html')

@app.route('/news/')
def news():
    return render_template('news.html')

if __name__ == '__main__':
    app.run(debug=True)
