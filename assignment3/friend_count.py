import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
	key = record[0]
	value = record[1]
	mr.emit_intermediate(key,value)

def reducer(key,list_of_values):
	value = len(list_of_values)
	answer = (key,value)
	mr.emit(answer)

inputdata = open(sys.argv[1])
mr.execute(inputdata,mapper,reducer)