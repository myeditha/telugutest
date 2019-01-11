import random
import json

def writetofile(lis, num):
    with open("data/outfile" + str(num) + ".txt", "w+") as w:
        w.write("\n".join(list(map(lambda x: x[0], lis))))

def main():
    numfiles = 16

    with open("data/outfiletest.json", "r") as f:
        lines = f.readlines()
        jsoncontent = list(map(lambda x: json.loads(x)["content"], lines))
        contentmappedtofile = list(map(lambda x: (x, random.randint(1,numfiles)), jsoncontent))
        listoflists = list(enumerate([[] for _ in range(numfiles)], 1))
        print(listoflists)
        listswithcontent = map(lambda x: (list(filter(lambda y: x[0]==y[1], contentmappedtofile)), x[0]), listoflists)
        for x in listswithcontent:
            print(x[1])
            writetofile(x[0], x[1])

main()