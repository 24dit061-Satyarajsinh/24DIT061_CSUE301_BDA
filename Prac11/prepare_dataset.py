import csv

input_file = "SMSSpamCollection"
output_file = "sms_spam.csv"

with open(input_file, "r", encoding="utf-8") as infile, \
     open(output_file, "w", newline="", encoding="utf-8") as outfile:

    writer = csv.writer(outfile)

    writer.writerow(["label", "message"])

    for line in infile:
        parts = line.rstrip("\n").split("\t", 1)

        if len(parts) == 2:
            label, message = parts
            writer.writerow([label, message])

print("Dataset converted successfully.")
print("Output file:", output_file)