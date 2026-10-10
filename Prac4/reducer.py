import sys

current_year = None
max_temp = None

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    year, temp = line.split("\t")
    temp = int(temp)

    if current_year == year:
        if temp > max_temp:
            max_temp = temp
    else:
        if current_year is not None:
            print(f"{current_year}\t{max_temp}")

        current_year = year
        max_temp = temp

if current_year is not None:
    print(f"{current_year}\t{max_temp}")