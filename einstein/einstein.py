# Program calculating E by E=mc^2

# Main function
def main():

    mass = int(input())

    energy = energy_mass(mass)

    print(energy)


# Calculating energy
def energy_mass(mass):

    energy = mass * ((3 * (10 ** 8)) ** 2)

    return energy


main()
