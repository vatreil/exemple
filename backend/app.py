# app.py
from flask import Flask, request, jsonify
from werkzeug.routing import BaseConverter
import redis

app = Flask(__name__)

r = redis.Redis(host='localhost', port='6379')

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

app.url_map.converters['regex'] = RegexConverter

@app.get('/user/')
def get_up():
    user_name = request.args.get('user_name')
    desc = r.get(str(user_name)).decode('utf-8')
    print(desc)
    return {"user_name": user_name, "desc": desc}, 200