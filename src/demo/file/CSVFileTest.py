import csv
from matplotlib import pyplot as plt
filename = 'd:\\namelist.csv'
print(filename)
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
    print(highs)
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')
plt.title("Daily high temperatures, July 2014", fontsize=24)

plt.show()