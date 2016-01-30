import csv
word_list = 'Smith%J,Doe%J' #list names here in lastname,%firstinitial format, separated by comma
word_set = set(word_list.split(','))
csv_out = csv.writer(open('authmatch_output.txt', 'w'), delimiter = '\t', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
with open ('research_output_auths.csv', 'rb') as csv_file:
  csv_reader = csv.reader(csv_file)
  for row in csv_reader:
    if (set(row[14].split()) & word_set) | (set(row[15].split()) & word_set) | (set(row[16].split()) & word_set) | (set(row[17].split()) & word_set) | (set(row[18].split()) & word_set) | (set(row[19].split()) & word_set) | (set(row[20].split()) & word_set) | (set(row[21].split()) & word_set) | (set(row[22].split()) & word_set) | (set(row[23].split()) & word_set) | (set(row[24].split()) & word_set) | (set(row[25].split()) & word_set):
      csv_out.writerow([row[0],row[1],row[26],row[27],row[28],row[29],(set(row[14].split()) & word_set),(set(row[15].split()) & word_set),(set(row[16].split()) & word_set),(set(row[17].split()) & word_set),(set(row[18].split()) & word_set),(set(row[19].split()) & word_set),(set(row[20].split()) & word_set),(set(row[21].split()) & word_set),(set(row[22].split()) & word_set),(set(row[23].split()) & word_set),(set(row[24].split()) & word_set),(set(row[25].split()) & word_set)])

    