import logging
from housing.logger import logging
from flask import Flask
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def index():
    logging.info("hello")
    return "My first project got deployed"
if __name__=="__main__":
    app.run(debug=True)