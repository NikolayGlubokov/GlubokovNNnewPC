import json, requests, csv

with open('data2.csv') as data_file:
    file_reader=csv.reader(data_file, delimiter = ';')
    for row in file_reader:
        print(row)

with open('data2.csv') as data2:
    fieldnames=['hostname','vendor','model','location']
    data_file2 = csv.DictReader(data2, delimiter=';')
    count = 0
    dt=[]
    for row in data_file2:
        print(row)
        dt.append(row)

    with open('database2.csv', 'w') as file_experiment:

        writer=csv.DictWriter(file_experiment, delimiter=';', lineterminator='\r', fieldnames=fieldnames)
        writer.writeheader()
        for row in dt:
            writer.writerow(row)



