import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    key = record[1] #the item id
    value = record #the full record
    mr.emit_intermediate(key,value)


def reducer(key, list_of_values):
    #final_list = []
    for v in list_of_values:
        if len(v) == 10:
            for j in list_of_values:
                 if len(j) != 10:
                 #     print type(v)
                 #     print type(v)
                    value = v+ j
                    mr.emit((value))

inputdata = open(sys.argv[1])
mr.execute(inputdata,mapper,reducer)
