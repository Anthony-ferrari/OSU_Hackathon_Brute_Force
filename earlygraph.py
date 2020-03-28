import matplotlib.pyplot as plt

x = ["1/22/2020", "3/18/2020", "3/21/2020", "3/22/2020", "3/23/2020", "3/24/2020", "3/25/2020", "3/26/2020",
     "3/26/2020", "3/27/2020", "3/27/2020"]
y = [1, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

plt.bar(x, y, color='blue', label='Reported Cases of COVID-19')
plt.title('Growth of COVID-19 Cases: 1st Case to Current Cases')
plt.xlabel('Report Date')
plt.ylabel('Reported Number of Cases')
plt.legend(facecolor='gray', shadow=True, loc=2)
plt.show()
