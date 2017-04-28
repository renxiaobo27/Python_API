from flask import Flask,request
from search_engine import elastic
import json
import logging.config
from logging_config import LOGGING

app = Flask(__name__)
engine = elastic.ElasticEngine()

logging.config.dictConfig(LOGGING)
log = logging.getLogger(__name__)

@app.route('/api/text_to_services',methods=['POST'])
def text_search():
    context = request.json
    res = engine.search(context)
    return json.dumps(res)


@app.route('/api/services', methods=['POST'])
def service_predict():
    context = request.json
    print context
    return 'pass_post'


if __name__ == '__main__':

    print 'running'
    app.run(host="0.0.0.0")