import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # key  : person
    # value: friend
    person = record[0]
    friend = record[1]
    mr.emit_intermediate(person, friend)

def reducer(key, list_of_friends):
    # key: person
    # value: list of his friends
    for friend in list_of_friends: # look of 
        try: 
            friends_list = mr.intermediate[friend]
            if (key not in friends_list):
                mr.emit((key, friend))
                mr.emit((friend, key))
        except KeyError:
                mr.emit((key, friend))
                mr.emit((friend, key))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)