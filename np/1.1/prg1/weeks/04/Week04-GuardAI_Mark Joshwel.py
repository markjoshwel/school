# GuardAI
#   Mark Joshwel, SXXXXXXXX
# =========================
# Simulation of a Guard in a Computer Gane

if input(f"Does the guard see the player (y/n) ").lower() == "n":
    print("The guard waits.")

else:
    dist_from_player = int(input("How far away is the player? "))

    if dist_from_player <= 1:
        print("The guard attacks!")

    elif dist_from_player <= 4:
        print("The guard advances.")

    else:
        print("The guard waits.")
