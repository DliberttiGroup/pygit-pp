from flask import Flask

app = Flask("demonio")


@app.route("/")
def say_hello():
    return "Hello pal nothing to see here :^"


app.run()
