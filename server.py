import os
from bottle import Bottle, request
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://fd79a8d119a44db5a96bc14a0ff65b61@sentry.io/1842359",
    integrations=[BottleIntegration()]
)

app = Bottle()

@app.route('/success')
def success():
    return

@app.route('/fail')
def fail():
    raise RuntimeError("Ошибка!")

app.run(host='localhost', port=8080)
