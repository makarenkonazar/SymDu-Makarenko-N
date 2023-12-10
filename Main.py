import csv

try:
    file_r = open("Lab11.csv", "r")
    reader = csv.DictReader(file_r, delimiter = ",")

    for row in reader:
        print(row["Country Name"], '; ', row["2015 [YR2015]"], '; ', row["2019 [YR2019]"])

except FileNotFoundError:
    print("Файл Lab11.csv не вдалося відкрити")

except:
    print("Виникла якась помилка")
file_r.close()


try:
    user_in = input("Введіть назву країни: ")

    with open("Lab11.csv", "r") as file_r, open("New_Lab11.csv", "w", newline='') as new_file:
        reader = csv.DictReader(file_r, delimiter=",")
        fieldnames = ["Series Name", "Series Code", "Country Name", "Country Code", "2015 [YR2015]", "2019 [YR2019]"]
        writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            if row["Country Name"] == user_in:
                writer.writerow({
                    "Series Name": row["Series Name"], "Series Code": row["Series Code"], "Country Name": row["Country Name"], "Country Code": row["Country Code"], "2015 [YR2015]": row["2015 [YR2015]"], "2019 [YR2019]": row["2019 [YR2019]"]
                })
except FileNotFoundError:
    print("Файл Lab11.csv не вдалося відкрити")

except:
    print("Виникла якась помилка")
file_r.close()
new_file.close()



