import psutil;
from flask import Flask , render_template
import os

app = Flask(__name__)
@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    Message = None 
    if cpu_percent > 80 or mem_percent >80:
        Message = " High CPU / Memory utilization "
    return render_template("index.html" , cpu_metric = cpu_percent , mem_metric=mem_percent, message=Message)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')