#!/usr/bin/env python3
import json
import argparse
import string
import re

def checkformistakes(line, nline):
    incorrect = input("enter space-separated incorrect words\n")
    print("entering correction mode: enter \'skip\' to skip current word, and \'end\' to exit correction mode")
    inclist = incorrect.split(" ")
    for inc in inclist:
        if inc in line:
            inp = input("Classify: " + inc + "\n")
            if(inp=='skip'):
                continue
            elif(inp=='end'):
                break
            nline = map(lambda x: inc + "\\" + inp if x.split('\\')[0] == inc else x, nline)
        else:
            print("word not in line; skipping")
    print("sentence: " + ' '.join(nline))
    sure = input("are you sure?\n")
    if(sure.lower()=='y' or sure.lower()=='yes'):
        return ' '.join(nline)
    else:
        return checkformistakes(line, nline)

def grabclasses(line):
    nline = []
    for word in line.split():
        print("sentence: " + line)
        wclass = input('Classify: ' + word + '\n')
        nline.append(word + "\\" + wclass)
    print("sentence: " + ' '.join(nline))
    sure = input("are you sure?\n")
    if(sure.lower()=='y' or sure.lower()=='yes'):
        return ' '.join(nline)
    else:
        return checkformistakes(line, nline)



def main():

    parser = argparse.ArgumentParser(description='Andhra Friends scraping')
    parser.add_argument('file', default = None, type=str, help='Input file name')
    parser.add_argument('outfileclass', default = None, type=str, help='Name of output file of cleansed data augmented with classification')

    args = parser.parse_args()

    if(not args.file):
        print("must include filename")

    with open(args.file) as f:
        textlines = f.readlines()
        
        textlines = textlines
        # need to tag each, pipe into separate files

        textlines = list(filter(lambda x: x!='', textlines))

        classification = list(map(lambda x: grabclasses(x), textlines))

        with open(args.outfileclass, 'w') as w:
            w.write('\n'.join(classification))    

main()