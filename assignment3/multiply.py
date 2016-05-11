import MapReduce
import sys

mr = MapReduce.MapReduce()

nrowsa = 5
ncolsb = 5
def mapper(record):
    matrix = record[0]
    row = record[1]
    column = record[2]
    value = record[3]

    # extract 1 row from matrix a for each column of b
    # and 1 column from matrix b for each row of a
    if matrix =='a':
        for i in range(0,ncolsb):
            key = (row,i)
            val = [matrix,column,value]
            mr.emit_intermediate(key,val)
    if matrix == 'b':
        for i in range(0,nrowsa):
            key = (i,column)
            val = [matrix,row,value]
            mr.emit_intermediate(key,val)



def reducer(key,list_of_values):
    a = []
    b = []
    tot = 0
    for v in list_of_values:
         el = (v[1],v[2])
         if v[0] == 'a':
            a.append(el)
         else:
            b.append(el)

    for i in a:
        for j in b:
            if i[0] == j[0]:
                tot += i[1]*j[1]
                break
    result = (key[0],key[1],tot)
    mr.emit(result)

inputdata = open(sys.argv[1])
mr.execute(inputdata,mapper,reducer)