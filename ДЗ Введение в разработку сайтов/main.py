from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def my_website_page():
    return render_template('mywebsite.html')

if __name__ == '__main__':
    app.run()



