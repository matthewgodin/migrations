import sys
import os
from datetime import datetime

LAST_PERFORMED_FILE = 'last_performed.txt'
if len(sys.argv) == 3 and sys.argv[1] == 'make':
    date_time = datetime.now()
    file_name = str(date_time.year) + '_' + str(date_time.month) + '_' \
        + str(date_time.day) + '_' + str(date_time.hour) + '_' \
        + str(date_time.minute) + '_' + str(date_time.second) + '_' \
        + str(date_time.microsecond) + '_' + sys.argv[2] + '.sql'
    f = open(file_name, 'w')
    f.close()
elif len(sys.argv) == 2 and sys.argv[1] == 'migrate':
    files = os.listdir()
    files.sort()
    if len(files) > 0:
        i = 0
        while files[i][0] == '.':
            i += 1
        if LAST_PERFORMED_FILE in files:
            f = open(LAST_PERFORMED_FILE, 'r')
            last_performed = f.read()
            f.close()
            while files[i] != last_performed:
                i += 1
            i += 1
        while files[i].endswith('.sql'):
            print("Executing migration " + files[i])
            i += 1
        if i > 0:
            f = open(LAST_PERFORMED_FILE, 'w')
            f.write(files[i - 1])
            f.close()
else:
    print("\nUsage:\n\nmigrations.py make <migration-name>\n\nmigrations.py "
        + "migrate\n")