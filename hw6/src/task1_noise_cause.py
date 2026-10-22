import os
from datetime import datetime

# filters the dataset to contain noise complaints
# output csv file indicates the month the complaint was created and the subcategory of the noise complaint

output = open(os.path.abspath("../data/2024_noise_data.csv"), "w", encoding="utf-8")
output.write("month,noise_complaint_category\n")

with open(os.path.abspath("../data/2024_311_data.csv"), "r", encoding="utf-8") as f:
    # skip processing the header line
    f.readline()

    line = f.readline()

    while line:
        feats = line.split(',')

        complaint = feats[5].split()
        
        if complaint[0] == "Noise":
            date = datetime.strptime(feats[1].split()[0], "%m/%d/%Y")
            month = date.strftime("%B")
            try:
                subtype = complaint[2]
            except:
                subtype = "Unspecified"

            output.write(f"{month},{subtype}\n")
    
        line = f.readline()

output.close()

print("///Finsihed Processing///")
