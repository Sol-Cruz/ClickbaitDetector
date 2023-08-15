# YouTube Clickbait Project
CS121 Spring 2019
Webpage: https://clickbait-prediction.herokuapp.com/



### Python script

* clickbait_test_real.py script: We used YouTube API and combined both models to make prediction. Provide the script with the youtube url to analyze. The script will print the model prediction: a number between 1 and 0, 1 is the video is 100% clickbait, 0 means the video is 0% clickbait.

Usage:
```python 
clickbait_test_real.py --url URL
```
* The predict.py script: If you don't want to install YouTube API related dependencies, you can use this script instead. Note that you will need to provide all the video information by yourself.


Usage: 
``` python
predict.py [-h] --title TITLE [--views VIEWS] [--likes LIKES]
           [--dislikes DISLIKES] [--comments COMMENTS] [--imagepath IMAGEPATH]
```


###  JSON files

* credential_sample.json: This file allows the script to work without retrieving the authentication code every time.
* client_secret_3.json: The client_secrets.json file format is a JSON formatted file containing the client ID, client secret, and other OAuth 2.0 parameters. Here is an example client_secrets.json file for a web application:

### Models
* Metada model: saved as `svm`. It's a support vector machine model based on alessiovierti/youtube-clickbait-detector
* Thumbnail model: saved as `models/clickbait-model-2.pth`R. It's a ResNet34 model, trained with fastai library.


### Web app
* `app.py`: A Flask application to connect front-end and back-end.
* `clickbaitHome.html`: HTML of the home web page.
