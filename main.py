import os

from Scenario1.scenario_one_floyd import floyd_main
from Scenario2.scenario_two_belmann import main_belmann_ford
from Scenario3.scenario_three_dijkstra import main_dijkstra

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":

    while True:
        print("\nMinimum Path Algorithms\n")
        print("========================")
        print("1. First Scenario")
        print("2. Second Scenario")
        print("3. Third Scenario")
        print("========================\n")
        choice = input("Select the scenario to run (1, 2, or 3): ")

        if choice == "1":
            floyd_main()
            input("Press Enter to continue...")
            clear_screen()
        elif choice == "2":
            main_belmann_ford()
            input("Press Enter to continue...")
            clear_screen()
        elif choice == "3":
            main_dijkstra()
            input("Press Enter to continue...")
            clear_screen()
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
            input("Press Enter to continue...")
            clear_screen()