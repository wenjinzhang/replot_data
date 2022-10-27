import os, csv
path = "./figure 8"

file_list = os.listdir(path)

for file_name in file_list:
    file_path = os.path.join(path, file_name)
    
    csv_file = open(file_path)
    csv_reader = csv.reader(csv_file, delimiter=',')
    x = []
    y = []
    for row in csv_reader:
        x.append(float(row[0]))
        y.append(float(row[1]))
    # print(file_name)
    print("{}_x=".format(file_name[:-4]), x)
    print("{}_y=".format(file_name[:-4]), y)
