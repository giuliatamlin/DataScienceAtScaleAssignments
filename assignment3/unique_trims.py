import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    sequence_id = record[0]
    nucleotides = record[1]
    trimmed_n = nucleotides[:-10]
    mr.emit_intermediate(trimmed_n,sequence_id)

def reducer(key,value):
    mr.emit(key)


inputdata = open(sys.argv[1])
mr.execute(inputdata,mapper,reducer)