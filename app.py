import logging
from urllib import response
from flask import Flask, request, abort, json
from langdetect import detect

from helpers import  search_words

app = Flask(__name__)

logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
 
@app.route('/', methods=['POST'])
def query_sentence():
    my_str = request.data
    new_str = my_str.decode('utf-8')
    sentence_check = json.loads(new_str)
    words = sentence_check.get('input')
    check_words = search_words(words)
    if check_words == True:
        app.logger.info('the sentence input is {0}'.format(words))
        resp = detect(words)
    else:
        app.logger.info('the word(s) were not found in word file')
        abort(400)

    return resp

        
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)