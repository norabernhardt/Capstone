import csv

counter=0
with open("Reihe-22B13.csv") as csv_file:
    csv_reader=csv.reader(csv_file)
    for row in csv_reader:    
        next(csv_reader)
        content=row[0].split("\t")[0]
        print(content,"\n")
        counter+=1



# file=open("Reihe-22B13.csv")
# csvreader=csv.reader(file)
# header = []
# header = next(csvreader)
# print(header)