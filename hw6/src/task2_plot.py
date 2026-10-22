import matplotlib.pyplot as plt
import os

def parse_rodent_file():
	# stores zipcodes as keys and their corresponding freq as values
	data = {}

	# the following file was created by using grep to select all rodent complaints
    # then csvtool to select the zipcodes and sort + uniq -c to count the freq
    with open(os.path.abspath("../data/rodent_location_occurance.txt"), "r") as f:
		line = f.readline()

		while line:
			parsed = line.split()
			freq = int(parsed[0])
			data[parsed[1]] = freq			

			line = f.readline()
	return data

# data
location_freq_data = parse_rodent_file()

# plotting
height = len(location_freq_data) * 0.25
plt.figure(figsize=(10, height))

plt.barh(location_freq_data.keys(), location_freq_data.values())

plt.xlabel("Frequency")
plt.ylabel("Zipcode")
plt.title("Frequency of Rodent Complaints by Zipode")

plt.ylim(-0.5, len(location_freq_data) - 0.5)
plt.tight_layout()


plt.savefig("task2_plot.png", dpi=300, bbox_inches="tight")
plt.close()
