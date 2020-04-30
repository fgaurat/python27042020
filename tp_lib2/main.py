from zipfile import ZipFile
import glob
import csv
from datetime import date

if __name__ == "__main__":
    
    # archive = "data.zip"
    # with ZipFile(archive) as myzip:
    #     myzip.extractall()

    list_csv = glob.glob("*.csv")
    
    for f in list_csv:

        with open(f, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_ts = int(row['due_date'])
                ts = date.fromtimestamp(data_ts)
                print(row['id'],row['title'],ts.strftime('%d/%m/%Y'))