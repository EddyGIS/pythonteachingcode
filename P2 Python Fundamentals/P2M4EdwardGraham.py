
# [ ] create The Weather

import os

# Download the weather data
cmd = 'curl -L https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt'
os.system(cmd)

# Add Rio de Janeiro to the file
mean_temps = open('mean_temp.txt', 'a+')
mean_temps.write("Rio de Janeiro,Brazil,30.0,18.0\n")

# Move to the beginning and read the headings
mean_temps.seek(0)
headings = mean_temps.readline().strip().split(',')

# Print student name
print("Edward Graham")

# Read the weather data
city_temp = mean_temps.readline()

while city_temp:
    city_temp = city_temp.strip().split(',')

    print(headings[0], "of", city_temp[0],
          headings[2], "is", city_temp[2], "Celsius")

    city_temp = mean_temps.readline()

mean_temps.close()
