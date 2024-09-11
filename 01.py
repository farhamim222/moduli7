def get_season_by_month(month):

    seasons = ("winter", "spring", "summer", "autumn", "winter")

    if month in [12, 1, 2]:
        return seasons[0]
    elif month in [3, 4, 5]:
        return seasons[1]
    elif month in [6, 7, 8]:
        return seasons[2]
    elif month in [9, 10, 11]:
        return seasons[3]
    else:
        return "Invalid month"

month = int(input("Enter the month number (1-12): "))
season = get_season_by_month(month)

print(f"The season for month {month} is {season}.")
