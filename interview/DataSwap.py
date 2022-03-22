#Program to find number of days, weeks and months in life left

maxlife = 90
current_humanlife = int(input("Please enter your age as per officical records : "))

#Time left on earth
days_left = round((maxlife - current_humanlife)*365)
weeks_left = round((maxlife-current_humanlife)*52.1429)
months_left = round((maxlife-current_humanlife)*12)
print(f"So you have {months_left} months ,{weeks_left} weeks & {days_left} days in your lifetime now. So enjoy your remaining time")


