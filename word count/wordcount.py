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
        mr.emit_intermediate(w, 1)
# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    for v in list_of_values:
        total += v
    mr.emit((key, total))
# Part 4
inputdata = open('books.json')
mr.execute(inputdata, mapper, reducer)
