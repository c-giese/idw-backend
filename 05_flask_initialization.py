from flask import Flask


app = Flask(__name__)
app.run(debug=True)

# First simple implementation of the Flask API

@app.route('/test', methods=['GET'])
def hello():
    return {"response": "Test was successful!"}


# First simple logic to test the Flask API

# counter = 0

# @app.route('/test', methods=['GET'])
# def hello():
#     global counter
#     counter += 1
#     response = {"response": f"Test was successful! Counter: {counter}"}
#     return response


