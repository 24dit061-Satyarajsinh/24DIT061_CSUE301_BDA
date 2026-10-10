import sys

for line in sys.stdin:
    line = line.strip()

    if len(line) < 93:
        continue

    try:
        # Year is stored at positions 15-18
        year = line[15:19]

        # Temperature is stored at positions 87-91
        temperature = int(line[87:92])

        # Quality code
        quality = line[92]

        # Ignore missing temperature values
        # and accept valid quality codes
        if temperature != 9999 and quality in "01459":
            print(f"{year}\t{temperature}")

    except:
        continue