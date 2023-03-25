from pprint import pprint

import csv

import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


contacts_list_1 = []
contacts_list_1.append(contacts_list[0])
for contact in contacts_list[1:]:
    fio = []
    for с in contact[0:3]:
        if с != '':
            i = с.split(sep = ' ')
            fio.append(i)
    fio_1 = sum(fio, [])
    if len(fio_1) < 3:
        fio_1.append('')
    contacts_list_1.append(fio_1+contact[3:])

pattern = r"(\+7|8)?\s*\(?(\d{3})\)?\s*\-?(\d{3})\-?(\d{2})\-?(\d{2})\s*\(?(доб.)?\s*(\d+)?\)?"
replace = r"+7(\2)\3-\4-\5 \6\7"
non_duplicate = []
duplicate_list = []
for contacts in contacts_list_1:
    res = re.sub(pattern, replace,contacts[5])
    contacts[5] = res
    if contacts[0:2] in non_duplicate:
        duplicate_list.append(contacts)
    else:
        non_duplicate.append(contacts[0:2])


for contact in contacts_list_1:
    for duplicate in duplicate_list:
        if contact == duplicate:
            contacts_list_1.remove(contact)
        elif contact[0:2] == duplicate[0:2]:
            i = contacts_list_1.index(contact)
            for ii in range(len(contact)):
                if contact[ii] == '':
                    contacts_list_1[i][ii] = duplicate[ii]



with open("phonebook.csv", "w",  encoding="utf-8") as f:
   datawriter = csv.writer(f, delimiter=',')
   datawriter.writerows(contacts_list_1)