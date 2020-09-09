from flask import Flask 
import socket
app = Flask(__name__)

@app.route("/")

def hello():
	return "<br> <br>" + "Name : MirzaCodes" + "<br> <br>" + "A sample flask app showing the Docker Container ID." + "<br> <br>" + "Hostname : " + socket.gethostname()

if __name__ == "__main__":
    app.run()