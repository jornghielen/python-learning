import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'Python_learning_chapter_2/downloading_data/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates and high temperatures from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

print(highs)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8-bright')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot.
ax.set_title("Daily high temperatures - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()