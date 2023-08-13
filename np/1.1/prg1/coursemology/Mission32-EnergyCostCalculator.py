TARIFF = 0.2743


def calculateEnergyCost(appliance_list: list, hrs_input: str):
    hr_list = [int(h) for h in hrs_input.split(";")]
    total_energy: float = 0

    print(f"{'Name':<18} {'Energy(Watts/Hr)':<16} {'Daily Hrs used':<14}")

    for appliance, hours in zip(appliance_list, hr_list):
        print(f"{appliance[0]:<18} {appliance[1]:<16} {hours:<14}")
        total_energy += (appliance[1] * hours) / 1000

    total_energy_cost: float = total_energy * TARIFF

    print(f"\nTotal daily energy consumed (kW): {total_energy}")
    print(f"Total daily energy cost ($): {total_energy_cost:.2f}")

    return total_energy_cost


appliance_list = [
    ["Electric Fan", 70],
    ["Air Con", 1200],
    ["Refrigerator", 200],
]  # type: list[list[str | int]]

print(
    f"List of Electrical Appliacnes with Energy in Watts/Hr:\n"
    f"{'Name':<18} {'Energy(Watts/Hr)':<16}"
)

for name, energy in appliance_list:
    print(f"{name:<18} {energy:<16}")

# input
# hrs_input = input("\nEnter daily hours used for the above appliances seperated by ';' : ")

# process
# total_energy_cost = calculateEnergyCost(appliance_list,hrs_input)

# output (Modify the statement to display the decimal value)
# doesn't calculateEnergyCost output it already?
# print(total_energy_cost)
