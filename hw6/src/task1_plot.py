import matplotlib.pyplot as plt
import os

def freq_counter(month):
    abr_name = month[:3].lower()
    counter = []

    # the {abr_name}_noise_cause.txt file was created from `grep {abr_name} 2024_noise_data.csv | sort | uniq -c`
    with open(os.path.abspath(f"../data/{abr_name}_noise_cause.txt"), "r") as f:
        line = f.readline()

        while line:
            
            # get the frequency
            freq = line.split()[0]
            counter.append(int(freq))
            
            line = f.readline()

    return counter

def get_monthly_data(month_list):
    data = []

    for m in month_list:
        data.append(freq_counter(m))

    return data


# axis data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

causes = ["Commercial", "Helicopter", "House", "Park", "Residential", "Street/Sidewalk", "Unspecified", "Vehicle"]

monthly_freq_data = get_monthly_data(months)

# create a 3 x 4 grid of pie charts
fig, axes = plt.subplots(3, 4, figsize=(16, 10))

for i, ax in enumerate(axes.flat):
    ax.pie(monthly_freq_data[i], startangle=90)
    ax.set_title(months[i])

fig.legend(causes, loc="lower center", ncol=4)

fig.suptitle("2024 Monthly Noise Complaint Cause Frequency", fontsize=16)
plt.tight_layout(rect=[0, 0.07, 1, 0.94])

fig.savefig("task1_plot.png", dpi=300, bbox_inches="tight")
plt.close(fig)
