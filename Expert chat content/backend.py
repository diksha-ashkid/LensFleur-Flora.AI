from flask import Flask , render_template
from flask_socketio import SocketIO, send
import werkzeug

app = Flask(__name__)
app.config['SECRET'] = "secret!123"
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('message')

def handle_message(message):
    print("Received message:"+ message)
    if message != "User connected!":
        send(message,broadcast = True)



@app.route('/')
def index():
    return render_template("index13.html")

if __name__=="__main__":
    socketio.run(app, host="localhost")

