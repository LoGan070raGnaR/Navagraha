while(1):

    mass_or_weight = input("Do you want to find Mass(M) or Weight(W) ? ")

    # Finding Mass
    if mass_or_weight.upper() == "M":

        mass = float(input("Enter Mass: "))
        unit = input("Mass is in Pounds(P) or Kilograms(K) ? ")

        if unit.upper() == "P":
            converted_mass_in_kg = mass * 0.45359237
            print(f"Mass = {converted_mass_in_kg} kg")

        elif unit.upper() == "K":
            converted_mass_in_lbs = mass / 0.45359237
            print(f"Mass = {converted_mass_in_lbs} lbs")

        else:
            print("Please enter correct information -> Enter P or K")

    # Finding Weight
    elif mass_or_weight.upper() == "W":
        # Gravitational Force in Solar Systems
        ss_gravity = input("Gravitational Force on Planets: \n"
                        "For Mercury --> Enter - 1 \n"
                        "For Venus --> Enter - 2 \n"
                        "For Earth --> Enter - 3 \n"
                        "For Mars --> Enter - 4 \n"
                        "For Jupiter --> Enter - 5 \n"
                        "For Saturn --> Enter - 6 \n"
                        "For Uranus --> Enter - 7 \n"
                        "For Neptune --> Enter - 8 \n"
                        
                        "Gravitational Force on Dwarf Planets: \n"
                        "For Pluto --> Enter - P \n"
                        "For Ceres --> Enter - C\n"
                        "For Makemake --> Enter - M\n"
                        "For Haumea --> Enter - H\n"
                        "For Eris --> Enter - E\n"
                        
                        "For the Sun --> Enter S\n"
                        "For Earth's Moon --> Enter 0")

        if ss_gravity == "1":
            gravity = 3.7
        elif ss_gravity == "2":
            gravity = 8.87
        elif ss_gravity == "3":
            gravity = 9.80665
        elif ss_gravity == "4":
            gravity = 3.711
        elif ss_gravity == "5":
            gravity = 24.79
        elif ss_gravity == "6":
            gravity = 10.44
        elif ss_gravity == "7":
            gravity = 8.87
        elif ss_gravity == "8":
            gravity = 11.15
        elif ss_gravity.upper() == "P":
            gravity = 0.58
        elif ss_gravity.upper() == "C":
            gravity = 0.27
        elif ss_gravity.upper() == "M":
            gravity = 0.5
        elif ss_gravity.upper() == "H":
            gravity = 0.63
        elif ss_gravity.upper() == "E":
            gravity = 0.82
        elif ss_gravity.upper() == "S":
            gravity = 274.20
        elif ss_gravity == "0":
            gravity = 1.625
        else:
            print("Please enter correct information -> Enter any number from 0 to 8 or Letters like P, C, M, H, E")

        weight_conversion = input("Mass to Weight --> Plain Covnert (P) --or-- Mass to Weight --> Different Unit (U) ?")

        if weight_conversion.upper() == "P":

            mass = float(input("Enter Mass: "))
            unit = input("Mass is in Pounds(P) or Kilograms(K) ? ")

            if unit.upper() == "P":
                weight = mass * gravity
                print(f"Weight = {weight} lbsm/s^2")

            elif unit.upper() == "K":
                weight = mass * gravity
                print(f"Weight = {weight} kgm/s^2")

            else:
                print("Please enter correct information -> Enter P or K")

        elif weight_conversion.upper() == "U":

            mass = float(input("Enter Mass: "))
            unit = input("Mass is in Pounds(P) or Kilograms(K) ? ")

            if unit.upper() == "P":
                converted_mass_in_kg = (mass * 0.45359237) * gravity
                print(f"Weight = {converted_mass_in_kg} kgm/s^2")

            elif unit.upper() == "K":
                converted_mass_in_lbs = (mass / 0.45359237) * gravity
                print(f"Weight = {converted_mass_in_lbs} lbsm/s^2")

            else:
                print("Please enter correct information -> Enter P or K")

        else:
            print("Please enter correct information -> Enter P or U")

    else:
        print("Please enter correct information -> Enter M or W")