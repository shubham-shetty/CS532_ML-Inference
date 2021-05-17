from flask import Flask, jsonify, request
import infer


APP_NAME = 'densenet-inference'
app = Flask(APP_NAME)

pred_endpoint = f'/v1/{APP_NAME}/prediction'

@app.route('/')
def landing():
    return f'''
<pre>
<h2>CS 532 21S - Project 2: ML Inference: Team 7</h3>
<b>POST</b> {pred_endpoint} :
    curl -F "query=@&lt;path/to/img/file&gt;" http://localhost:5000/v1/densenet-inference/prediction
</pre>
'''

@app.route(pred_endpoint, methods=['POST'])
def predict():
    img_file = request.files['query']
    class_id, class_name = infer.get_prediction(image_bytes=img_file.read())
    return jsonify({'id': class_id, 'label': class_name})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

"""

Test snippets:
--------------

CURL:
    curl -F "query=@../data/images/zeppelin.jpg" http://localhost:5000/v1/densenet-inference/prediction

Python:
    import requests
    print((requests.post("http://localhost:5000/v1/densenet-inference/prediction", files={"query": open('../data/images/zeppelin.jpg', 'rb')})).json())

"""
