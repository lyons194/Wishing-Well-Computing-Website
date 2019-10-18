from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/careers/')
def careers():
    return render_template('careers.html')

@app.route('/news/')
def news():
    return render_template('news.html')

if __name__ == '__main__':
    app.run(debug=True)
