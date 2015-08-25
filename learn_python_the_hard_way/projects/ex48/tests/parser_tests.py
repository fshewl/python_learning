from nose.tools import *
from ex48.parser import *

def test_player():
    word_list = [('verb', 'run'), ('direction', 'north')]
    sentence = parse_sentence(word_list)
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'run')
    assert_equal(sentence.obj, 'north')

def test_all():
    word_list = [('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'),
                 ('noun', 'honey')]
    sentence = parse_sentence(word_list)
    assert_equal(sentence.subject, 'bear')
    assert_equal(sentence.verb, 'eat')
    assert_equal(sentence.obj, 'honey')

def test_exception():
    word_list = []

    try:
        sentence = parse_sentence(word_list)
        assert False
    except:
        assert True
        

    
