import MapReduce
import sys
# Part 1
mr = MapReduce.MapReduce()
# Part 2
def mapper(record):
    # key: id
    # value: attributes
    key = record[1]
    value = record[2:]
    mr.emit_intermediate(key,value)
# Part 3
def reducer(key,attributes):
    # key: id
    # value: list of attributes
    total = []
    for v in attributes:
        total.append(v)
    mr.emit((key, total))
# Part 4
inputdata = open('records.json')
mr.execute(inputdata, mapper, reducer)
