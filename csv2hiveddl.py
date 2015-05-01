#!/usr/bin/python
import sys,csv,argparse

def main():
   parser = argparse.ArgumentParser()
   parser.add_argument('csvfile',help="csv file to parse")
   parser.add_argument('hdfsdir',help="location of files on hdfs")
   parser.add_argument('tablename',help="name of Hive table")
   args = parser.parse_args()
   parseCsv(args.csvfile, args.hdfsdir, args.tablename)

def parseCsv(inputFile,hdfsLocation,tableName):
   illegalChars = ['.','-']
   f = open(inputFile, 'rb')
   reader = csv.reader(f)
   headers = reader.next()
   row = reader.next()
   print "CREATE TABLE " + tableName + "("
   for (i,h) in enumerate(headers):
      h = h.translate(None, ''.join(illegalChars))
      try:
         v = int(row[i])
         sys.stdout.write(h + " INT")
      except:
         sys.stdout.write(h + " STRING")
      if i < len(headers) - 1 :
         print(",")
      else:
         print(")")
         print("row format delimited fields terminated by \',\' lines terminated by \'\\n\' location \'" + hdfsLocation + "\' tblproperties (\"skip.header.line.count\"=\"1\");")


if __name__ == '__main__':
   main()
