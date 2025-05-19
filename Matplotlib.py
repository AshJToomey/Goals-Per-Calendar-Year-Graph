# goals per calendar year graph

import matplotlib.pyplot as plt

# User input
years = list(map(int, input("Enter calendar year (e.g. 2018, 2019, 2020): ").split(',')))
goals = list(map(int, input("Enter goals per season in each year (same order): ").split(',')))

# Input validation
if len(years) != len(goals):
    print("Error: Number of years and number of goal values must match.")
else:
    plt.figure(figsize=(10, 5))
    plt.plot(years, goals, linestyle=':', color='green', marker='o', label = 'Goals')
    
    # Annotate points
    for i in range(len(years)):
        plt.text(years[i], goals[i], f"{goals[i]}", fontsize=9, ha='center', va='bottom')

    plt.title("Goals per Calendar Year")
    plt.xlabel("Year")
    plt.ylabel("Goals Scored")
    plt.grid(True)
    plt.xticks(years)
    plt.legend()
    plt.tight_layout()
    plt.savefig("goals_per_year.png")
    plt.show()

