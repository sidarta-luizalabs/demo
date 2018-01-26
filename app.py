from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def slash():
  return "%s - xpto" % socket.gethostname()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
