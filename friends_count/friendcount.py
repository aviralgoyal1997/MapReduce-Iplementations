import MapReduce
import sys
# Part 1
mr = MapReduce.MapReduce()
# Part 2
def mapper(record):
    # key: user
    # value: friend
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, 1)
# Part 3
def reducer(key, list_of_friends):
    # key: user
    # value: list of friends
    total = 0
    for v in list_of_friends:
        total += v
    mr.emit((key, total))
# Part 4
inputdata = open('friends.json')
mr.execute(inputdata, mapper, reducer)
