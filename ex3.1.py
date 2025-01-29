import matplotlib.pyplot as plt
import json

input_file = "internetdata.json"
output_low_income = "hist1.png"
output_high_income = "hist2.png"

f = open(input_file, "r")
data = json.load(f)

low_usage = []
high_usage = []

for record in data:
    income = record.get("incomeperperson")
    internet_usage = record.get("internetuserate")
    if income is not None and internet_usage is not None:
        if(income < 10000):
            low_usage.append(internet_usage)
        else:
            high_usage.append(internet_usage)

def create_histogram(data, title, output_file, color):
    plt.figure(figsize=(10, 5))
    plt.hist(data, bins=20, edgecolor="black", alpha=0.75, color=color)
    plt.xlabel("Internet Usage (%)")
    plt.ylabel("Number of Countries")
    plt.title(title)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.savefig(output_file)
    plt.close()

create_histogram(low_usage, "Internet Usage in Low-Income Countries (<10,000)", output_low_income, color="blue")
create_histogram(high_usage, "Internet Usage in High-Income Countries (≥10,000)", output_high_income, color="green")

print(f"Histograms were saved as {output_low_income} and {output_high_income}")