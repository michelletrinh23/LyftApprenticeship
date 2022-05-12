# Lyft Apprenticeship Coding Sample
This is my coding assignment for the 2022 Lyft Apprenticeship

## Task

Please write a small web application in one of the above languages (Python/Ruby/Javascript). The application only needs to do the following:
  - Accept a POST request to the route “/test”, which accepts one argument “string_to_cut”
  - Return a JSON object with the key “return_string” and a string containing every third letter from the original string
  - (e.g.) If you POST {"string_to_cut": "iamyourlyftdriver"}, it will return: {"return_string": "muydv"}.

## How to run

1. First install dependencies in your terminal

```
pip install flask
```

2. Then run the python script

```
python main.py
```

3. Then run this curl command in a seperate terminal window

```
curl -X POST http://127.0.0.1:5000/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'
```
