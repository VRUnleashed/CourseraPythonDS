fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print("Invalid file.")

email = dict()

for line in fh:

    if not line.startswith('From:') and line.startswith('From'):
        words = line.split()
        key = words[1]

        email[key] = email.get(key, 0) + 1

temp = list()
for key, value in email.items():
    temp.append((key, value))

max_key, max = temp[0]

for k, v in temp:
    if v > max:
        max = v
        max_key = k

print(max_key, max)
