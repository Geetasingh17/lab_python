data = ''
count = 0

with open('v3.txt', 'r') as infile:
    data = infile.readlines()
print(data)

for line in data:
    if '--undefined--' in line:
        count += 1

count