from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from requests.exceptions import ConnectionError
from wtforms import IntegerField, SelectField, StringField
from wtforms.validators import DataRequired

import urllib.request
import json

class ClientDataForm(FlaskForm):
    recency = StringField('Recency', validators=[DataRequired()])
    frequency = StringField('Frequency', validators=[DataRequired()])
    time_ = StringField('Time', validators=[DataRequired()])


app = Flask(__name__)
app.config.update(
    CSRF_ENABLED=True,
    SECRET_KEY='you-will-never-guess',
)

def get_prediction(recency, frequency, time_):
    body = {
        'recency': recency,
        'frequency': frequency,
        'time': time_
    }

    myurl = "http://0.0.0.0:8180/predict"
    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = urllib.request.urlopen(req, jsondataasbytes)
    return json.loads(response.read())['predictions']

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/predicted/<response>')
def predicted(response):
    response = json.loads(response)
    print(response)
    return render_template('predicted.html', response=response)


@app.route('/predict_form', methods=['GET', 'POST'])
def predict_form():
    form = ClientDataForm()
    data = dict()
    if request.method == 'POST':

        try:
            data['recency'] = int(request.form.get('recency'))
            data['frequency'] = int(request.form.get('frequency'))
            data['time'] = int(request.form.get('time_'))

            response = str(get_prediction(
                data['recency'],
                data['frequency'],
                data['time']
            ))
            print(response)
        except ValueError:
            response = json.dumps({"error": "ValueError"})
        except ConnectionError:
            response = json.dumps({"error": "ConnectionError"})
        return redirect(url_for('predicted', response=response))
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181, debug=True)
