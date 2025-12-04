import csv
import glob

def merge_csv_files(output_file):
    csv_files = glob.glob("*.csv")

    with open(output_file, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)

        for file in csv_files:
            with open(file, "r", encoding="utf-8") as infile:
                reader = csv.reader(infile)
                for row in reader:
                    writer.writerow(row)

    print(" All CSV files merged")

if __name__ == "__main__":
    merge_csv_files("merged.csv")
