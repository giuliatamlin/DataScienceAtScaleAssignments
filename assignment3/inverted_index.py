import MapReduce
import sys

mr = MapReduce.MapReduce()
def mapper(record):
    key = record[0] #the book
    value = record[1] #its content
    words = list(set(value.split()))
    for w in words:
        mr.emit_intermediate(w,key)


def reducer(key, list_of_values):
    mr.emit((key,list_of_values))

inputdata = open(sys.argv[1])
mr.execute(inputdata,mapper,reducer)

