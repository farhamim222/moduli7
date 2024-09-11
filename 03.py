def airport_program():
    airports = {}

    while True:
        print("\nChoose an option:")
        print("1: Enter a new airport")
        print("2: Retrieve airport by ICAO code")
        print("3: Exit")
        choice = input("Your choice: ")

        if choice == "1":

            icao_code = input("Enter the airport ICAO code: ").strip().upper()
            name = input("Enter the airport name: ").strip()


            airports[icao_code] = name
            print(f"Airport {name} (ICAO: {icao_code}) saved.")

        elif choice == "2":

            icao_code = input("Enter the ICAO code to search: ").strip().upper()


            if icao_code in airports:
                print(f"Airport {icao_code}: {airports[icao_code]}")
            else:
                print(f"No airport found with ICAO code {icao_code}.")

        elif choice == "3":

            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")

airport_program()
