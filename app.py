import numpy as np
import pickle
from flask import Flask,request,render_template

#create Flask app
app =  Flask(__name__)

#load the pickle model
model=pickle.load(open("Model.pkl","rb"))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict",methods = ["POST"])
def predict():
    float_features = [float(X) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)

    return render_template("index.html",prediction_text = "The float species is {}".format(prediction))

if __name__ == "__main__":
    app.run(debug=True)