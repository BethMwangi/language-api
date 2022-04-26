import os
import logging

log = logging.getLogger()

word_file = "./words"

with open(word_file, "r") as file:
    file_lines = file.read()

def search_words(sentence):
    """
    Input <sentence> to search if words found in the words file.
    """
    log.info('the input sentence is {0}'.format(sentence))
    for word in sentence.split():
        if word not in file_lines:
            return False
    log.info('Words matched in the file dictionary')
    return True