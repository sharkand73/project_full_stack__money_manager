from datetime import datetime
import repositories.transaction_repository as transaction_repo

def convert_date(date_string):
    year = int(date_string[:4])
    month = int(date_string[5:7])
    day = int(date_string[-2:])
    return datetime(year, month, day)


# ---------------- SANTANDER functions ------------------

def file_list(filename):
    file_list = []
    with open(filename, 'r', encoding = "ISO-8859-1") as file:
        while True:
            string = file.readline()
            if string == "":
                break
            else:
                file_list.append(string)
    return file_list

def validate(file_list):
    empty ="\t\t\t\t\t\t\n"
    if len(file_list) <4:
        return None   
    if file_list[0][:5] != "From:":
        return None
    if file_list[2][:8] != "Account:":
        return None      
    # remove first four lines
    for i in range(0, 4):
        file_list.pop(0)
    for line in file_list:
        if line == empty:
            file_list.remove(line)
    if len(file_list) % 4:
        return None
    else: 
        return file_list
    return file_list

def parse_description(line):    # takes the whole description
    start = line.index("\xa0") + 1
    return line[start:]

def parse_date(line):   # parses the date 
    return line[-11:-1]

def parse_amount(line): # parses the monetary value between the two symbols
    start = line.index("\xa0") + 1
    end = line[start:].index("\xa0") + start
    return line[start: end]

def trim_description(description):  # removes start and end, leaving merchant
    start = description.index("TO ") + 3
    end = description.find(",")
    return description[start: end]

def create_dict(list):
    dict_list = []
    i = 0
    while i < len(list):
        date = parse_date(list[i])
        description = parse_description(list[i+1])
        amount = float(parse_amount(list[i+2]))
        if amount < 0:
            #print(i // 4)
            description = trim_description(description)
            dict_list.append({'date': date, 'description': description, 'amount': amount})
        i += 4
    return dict_list

def convert_date_2(date_string):
    year = int(date_string[-4:])
    month = int(date_string[3:5])
    day = int(date_string[:2])
    return datetime(year, month, day) 