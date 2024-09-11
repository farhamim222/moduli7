def ask_names():
    names = set()

    while True:
        name = input("Enter a name (empty input to stop): ").strip()

        if name == "":
            break

        if name in names:
            print("Previously entered name")
        else:
            print("New name")
            names.add(name)

    print("\nEntered names:")
    for name in names:
        print(name)

ask_names()
