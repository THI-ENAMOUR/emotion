#!/usr/bin/env python3

from sys import argv

import flask

from media_queue import MediaQueue
from wsgi_server import WSGIServer

app = flask.Flask(__name__, static_folder="static")
sound_queue = MediaQueue()
display_queue = MediaQueue()


@app.route("/", methods=["GET"])
def index():
    return flask.render_template("index.html")


@app.route("/favicon.ico", methods=["GET"])
def fav():
    return flask.url_for("static", filename="favicon.ico")


# Set next facial expression
@app.route("/sound", methods=["POST"])
def post_sound():
    try:
        data = flask.request.get_json()
        sound_queue.publish(msg=data)
        return {}, 200
    except Exception as e:
        print(e)
        print("error")
        return {}, 400


@app.route("/display", methods=["POST"])
def post_display():
    try:
        data = flask.request.get_json()
        display_queue.publish(msg=data)
        return {}, 200
    except Exception as e:
        print(e)
        print("error")
        return {}, 400


# Get next facial expression
@app.route("/next-sound", methods=["GET"])
def listen_sound():
    def stream():
        messages = sound_queue.subscribe()  # returns a queue.Queue
        while True:
            msg = messages.get()  # blocks until a new message arrives
            yield msg

    return flask.Response(stream(), mimetype="text/event-stream")


@app.route("/next-display", methods=["GET"])
def listen_display():
    def stream():
        messages = display_queue.subscribe()  # returns a queue.Queue
        while True:
            msg = messages.get()  # blocks until a new message arrives
            yield msg

    return flask.Response(stream(), mimetype="text/event-stream")


if __name__ == "__main__":
    default_config = {"bind": "127.0.0.1:5000", "workers": 1, "threads": 8, "k": "gevent"}
    server = WSGIServer(app)
    server.init(opts=default_config, args=argv)
    server.run()
