from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about-us/')
def home():
    return render_template('about-us.html')

@app.route('/careers/')
def careers():
    return render_template('careers.html')

@app.route('/news/')
def news():
    return render_template('news.html')

@app.route('/status-update/')
def status():
    return render_template('status.html')

@app.route('/faq/')
def faq():
    return render_template('faq.html')

if __name__ == '__main__':
    app.run(debug=True)
