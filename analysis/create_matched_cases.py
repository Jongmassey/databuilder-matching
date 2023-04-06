import csv

with open("output/matched_cases_stp.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(("patient_id", "n", "text"))
    writer.writerows([(i, i + 10, chr(96 + i)) for i in range(1, 11)])
