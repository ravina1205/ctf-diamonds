from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return """
    <h1 style='color: red;'>Welcome to the Challenge </h1>
    <h2>Hint:</h2><h3>You need to download the pcap file to search for your favourite flag</h3>
    <p>All the best...!!</p>
    """

@app.route("/index")
def index():

    app.logger.debug(app.config.get("ENV"))

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
