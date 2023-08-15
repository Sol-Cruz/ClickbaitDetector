"""This module connect front-end and back-end."""
import subprocess
import flask
import requests
import shutil

app = flask.Flask(__name__)

@app.route("/")
def hello_route():
    return flask.send_from_directory("templates/", "clickbaitHome.html")

@app.route("/about")
def about_route():
    return flask.send_from_directory("templates/", "clickbaitAbout.html")

@app.route("/api/v1/classify", methods=["POST"])
def classify_api():
    request = flask.request.get_json(silent=True)
    if isinstance(request, str):
        result = subprocess.check_output(['python', 'clickbait_test_real.py', '-u=' + request])
        prediction = result.decode("utf-8") 
        print(prediction)
        prob, title, url = prediction.split('\n')[:-1]
        response = flask.jsonify(predictions=prob, title=title, thumbnail=url,videolink=request)
        return response
        
    else:
        response = {
            "error": "Bad input"
        }
    #return prediction from backend
    return flask.jsonify(request)



if __name__ == "__main__":
    app.run()
