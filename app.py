from flask import Flask, render_template
app=Flask(__name__, static_url_path='')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return 'This is services'

@app.route('/contact')
def contact():
    return 'This is Contact'


if __name__=='__main__':
    app.run('localhost', port=5000, debug=True)


