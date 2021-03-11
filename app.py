
import numpy as np

from flask import Flask, request, jsonify, render_template
import detect_features
import pickle
# nltk.download('stopwords')



#----------FLASK-----------------------------#

app = Flask(__name__)
model = pickle.load(open('decisiontree_pickle_model','rb'))
@app.route('/predict',methods = ['POST'])
def predict():
    url = request.form['url']
    res=detect_features.generate_data_set(url)
    res = np.array(res).reshape(1,-1)
    pred= model.predict(res)
    
    isphishing=pred[0]
    if isphishing==1:
        prediction="not a phishing site"
    else:
        prediction="a phishing site"
    
    
#     prediction="a phishing site"
    #output = round(prediction[0], 2)
    return render_template('index1.html', prediction_text=prediction)

@app.route('/')
def homepage():
	title = "TEXT summarizer"
	return render_template('index1.html')

if __name__ == "__main__":
	app.debug = True
	app.run()
