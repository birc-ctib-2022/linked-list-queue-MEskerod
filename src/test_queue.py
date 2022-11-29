"""Testing queues."""

from queue import (Queue)

def test_make_queue(): 
    queue = Queue()
    assert str(queue) == "[]"

def test_enqueue(): 
    assert 2 == 1

def test_is_empty(): 
    queue = Queue()
    assert queue.is_empty == True
    queue.enqueue(1)
    assert queue.is_empty == False


