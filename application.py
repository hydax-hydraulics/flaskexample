from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return "Hello How you doing?"

if __name__ == '__main__':
    application.run(debug= True, port=5001)