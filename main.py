# This is a coding sample for the Lyft 2022 Software Engineering Apprenticeship
# Overview: A simple web application that handles POST and GET requests built in Python to return every 3rd character in a string
# Dependencies: Flask

from flask import Flask, request
import requests
import json

# Flask initialization
app = Flask(__name__)

@app.route('/test', methods=["POST"]) # binds function to the route '/test' and allows for POST requests
def post_handler(): # takes in incoming string via POST, returns JSON data containing every 3rd char of initial string
	
    incoming_data = request.json["string_to_cut"] #unpack json data from POST
    
    if type(incoming_data) == str: # check to make sure data is a string
        string_to_return = every_third(incoming_data) # use helper function for compute
        json_to_return = {"return_string": string_to_return} # pack string back into json format
    else: # otherwise prompt user to correct their request
        json_to_return = {"return_string": "Please enter a string. Ex: iamyourlyftdriver"}
    
    return json_to_return
	
def every_third(string): # takes a string as input and returns every 3rd char
    new_string = "" 
    for index in range(len(string)):
        if (index + 1) % 3 == 0:
            new_string += string[index]
    return new_string
	
if __name__ == '__main__':
    app.run()
