# Starting the application
1. Run ```pip install -r requirements.txt```
2. Run ```gunicorn --bind 0.0.0.0:8000 api:app```

# API Endpoint
```POST``` API will be serving on port ```8000``` and with an endpoint ```<host>:8000/ner```. The request data should be sent with ```body``` as ```{"text": <text>}```
