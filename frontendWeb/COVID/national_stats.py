import csv


def csv_to_list(file_name):
    """
    Converts a csv file to lists
    :param file_name: string
    :return: lists
    """

    # variable
    national_dict = {}

    with open(file_name) as csv_file:

        # convert each row to a list of strings
        csv_reader = csv.reader(csv_file, delimiter=',')

        line_count = 0
        confirmed = 0
        deaths = 0
        recoveries = 0

        national_data = []

        for row in csv_reader:

            # skip column headers
            if line_count == 0:
                line_count += 1
                continue

            # skip non-US territories
            if row[0] == '':
                continue

            national_data += [[int(row[7]), int(row[8]), int(row[9])]]    # [confirmed, deaths, recoveries]

        print(national_data)
        for i in range(len(national_data)):
            confirmed += national_data[i][0]
            deaths += national_data[i][1]
            recoveries += national_data[i][2]

        print("Confirmed: " + str(confirmed) + "  Deaths: " + str(deaths) + "  Recoveries: ", str(recoveries))
        return confirmed, deaths, recoveries


nation_data = csv_to_list('03-28-2020.csv')
print(nation_data)

