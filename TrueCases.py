from constants import *
import csv


def calculate_true_cases(total_deaths):
    """
    Uses total deaths to calculate the true number of cases of COVID-19 in an area
    :param total_deaths: int
    :return: int
    """

    # Number of cases that caused the deaths
    cases_that_caused_deaths = total_deaths / FATALITY_RATE

    # Number of times cases have doubled
    times_doubled = DAYS_TO_DEATH / DOUBLING_TIME

    # True cases today
    return cases_that_caused_deaths * (2**times_doubled)


def csv_to_dict(file_name):
    """
    Converts a csv file to lists
    :param file_name: string
    :return: lists
    """

    # variable
    cities_dict = {}

    with open(file_name) as csv_file:

        # convert each row to a list of strings
        csv_reader = csv.reader(csv_file, delimiter=',')

        line_count = 0

        for row in csv_reader:

            # skip column headers
            if line_count == 0:
                line_count += 1
                continue

            # skip non-US territories
            if row[0] == '':
                continue

            city_data = [row[1], row[2], int(row[8])]    # [county, state, deaths]

            cities_dict[row[0]] = city_data

    return cities_dict


cities_data = csv_to_dict('03-28-2020.csv')


for fips in cities_data:
    county = cities_data[fips][0]
    state = cities_data[fips][1]
    deaths = cities_data[fips][2]
    print("County: " + county + "  State: " + state + "  Deaths: ", deaths)
    true_cases = calculate_true_cases(deaths)
    print("True Cases: ", true_cases)