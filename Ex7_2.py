# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

addition = 0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    pos = line.find('0')
    num = line[pos:]

    number = float(num)
    addition = addition + number
    count = count + 1

average = addition / count

print('Average spam confidence:', average)
