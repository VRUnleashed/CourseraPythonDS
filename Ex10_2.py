fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print("Invalid file.")

hours = dict()

for line in fh:

    if not line.startswith('From:') and line.startswith('From'):
        words = line.split()
        time = words[5]
        hour = time[0:2]

        hours[hour] = hours.get(hour, 0) + 1

tmp = list()

for k, v in sorted(hours.items()):
    print(k, v)
