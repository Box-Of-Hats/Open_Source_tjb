from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    pagehtml = """This is the homepage.<br/>
    <a href='http://127.0.0.1:5000/two'>Page Two</a>"""
    return pagehtml


@app.route("/two")
def hellotwo():
    return "Hello World two!"

if __name__ == "__main__":
    app.run(debug=True)