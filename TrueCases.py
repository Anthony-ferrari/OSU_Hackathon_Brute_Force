from constants import *
import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


fips = set()
counties_dict = {}
true_cases_dict = {}
labels = []
stated_cases_list = []
true_cases_list = []



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
    return round(cases_that_caused_deaths * (2**times_doubled))


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
#
#
# cities_data = csv_to_dict('03-28-2020.csv')
#
#
# for fips in cities_data:
#     county = cities_data[fips][0]
#     state = cities_data[fips][1]
#     deaths = cities_data[fips][2]
#     print("County: " + county + "  State: " + state + "  Deaths: ", deaths)
#     true_cases = calculate_true_cases(deaths)
#     print("True Cases: ", true_cases)



def read_us_counties_csv(file_name):
    """

    """

    # read the data
    with open(file_name) as csv_file:

        # convert each row to a list of strings
        csv_reader = csv.reader(csv_file, delimiter=',')

        line_count = 0
        counties_with_deaths = []

        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue

            if int(row[5]) > 0:
                counties_with_deaths.append(row)

        return counties_with_deaths


counties_with_deaths = read_us_counties_csv('us-counties.csv')


def get_counties_with_deaths_today(counties_list, date):
    """

    :param counties_list:
    :return:
    """

    # counties with deaths today
    today_list = []

    for county in counties_list:
        if county[0] == date:
            today_list.append(county)

    return today_list


# get the number of deaths per county today
counties_with_deaths_today = get_counties_with_deaths_today(counties_with_deaths, '2020-03-27')


# track counties with over 10 deaths
for county in counties_with_deaths_today:

    # variable(s)
    county_fips = county[3]
    county_stated_cases = int(county[4])
    county_deaths = int(county[5])
    county_name = county[1]
    state_name = county[2]
    date = county[0]
    county_state_name = county_name + ", " + state_name

    if county_deaths > 27:
        true_cases_dict[county_state_name] = [county_stated_cases, calculate_true_cases(county_deaths)]


# print the county with true cases
for county in true_cases_dict:
    print("County: " + county + "   Stated Cases: ", true_cases_dict[county][0], "  True Cases: ", true_cases_dict[county][1])


# populate lists for graph
for county in true_cases_dict:
    labels.append(county)
    stated_cases_list.append(true_cases_dict[county][0])
    true_cases_list.append(true_cases_dict[county][1])

print(labels)
print(len(labels))
print(stated_cases_list)
print(len(stated_cases_list))
print(true_cases_list)
print(len(true_cases_list))


x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, stated_cases_list, width, label='stated cases')
rects2 = ax.bar(x + width/2, true_cases_list, width, label='true cases')

ax.set_ylabel('Number of Cases')
ax.set_title('Coronavirus Cases: Stated v. True')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()





# # organize counties by fips---------------------------------------------------------
# for county in counties_with_deaths:
#
#     # variable(s)
#     county_fips = county[3]
#     county_stated_cases = int(county[4])
#     county_deaths = int(county[5])
#     county_name = county[1].replace(" ", "")
#     state_name = county[2].replace(" ", "")
#     date = county[0]
#     county_state_name = county_name + state_name
#
#     # ignore non-fips locations for now
#     if county_fips == "":
#         continue
#
#     # update numbers for existing fips
#     if county_fips in fips:
#
#         # update number of stated cases
#         counties_dict[county_state_name][2] += county_stated_cases
#
#         # update number of deaths
#         counties_dict[county_state_name][3] += county_deaths
#
#     else:
#
#         # update set of recorded fips
#         fips.add(county_fips)
#
#         # update first date of death, cases, and deaths
#         # [ county name, date of first death, cases, deaths]
#         counties_dict[county_state_name] = [county_state_name, date, county_stated_cases, county_deaths]
