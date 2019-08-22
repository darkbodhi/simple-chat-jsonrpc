from flask import Flask, render_template
from flask_jsonrpc import JSONRPC
import requests
import mongoengine
from jsonrpc import JSONRPCResponseManager, dispatcher


app = Flask(__name__, static_folder='/home/bodhi/PycharmProjects/chat_pulsepro/')
app.add_url_rule('/', 'api', api.as_view(), methods=['POST'])
app.config['SECRET_KEY'] = 'my_key'

if __name__ == '__main__':
    jsonrpc = JSONRPC(app, '/api')

@app.route('/')
def chat_room():
    return render_template('chat_room.html')


@dispatcher.add_method
def handle_message(json, methods=['GET', 'POST']):
    user_name_info = requests.form['user_name']
    message_info = requests.form['message']
    add_info = Dialogue(user=user_name_info, message=message_info)
    add_info.save()
    response = JSONRPCResponseManager.handle(
        message_info, dispatcher)
    return Response(response.json, mimetype='application/json')