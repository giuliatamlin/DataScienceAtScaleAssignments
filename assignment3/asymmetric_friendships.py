import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key,value)

def reducer(person,friends):
    for friend in friends:
        if friend not in mr.intermediate.keys():
            ans = (friend,person)
            mr.emit(ans)
            mr.emit((person,friend))
        else:
            if person not in mr.intermediate[friend]:
               ans = (friend,person)
               mr.emit(ans)
               mr.emit((person,friend))

inputdata = open(sys.argv[1])
mr.execute(inputdata,mapper,reducer)