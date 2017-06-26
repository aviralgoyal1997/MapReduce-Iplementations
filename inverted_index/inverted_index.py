import MapReduce
import sys
# Part 1
mr = MapReduce.MapReduce()
# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
        mr.emit_intermediate(w, key)
# Part 3
def reducer(key, list_of_docs):
    # key: word
    # value: list of documents word occured in
    total = []
    for v in list_of_docs:
        total.append(v)
    mr.emit((key, total))
# Part 4
inputdata = open('books.json')
mr.execute(inputdata, mapper, reducer)
