#finding the upcoming date
day = int(input("day : "))
month = int(input("month : "))
year = int(input("year : "))
if month == 1 and 1<=day<=30 and 1800<=year<=2025:
    print(f"{day+1}/{month}/{year}") 
elif month == 1 and day==31 and 1800<=year<=2025:
    print(f"1/{month+1}/{year}") 
elif month == 2 and 1<=day<=27 and 1800<=year<=2025:
    print(f"{day+1}/{month}/{year}") 
elif month == 2 and 1<=day<=27 and year%4 == 0 and 1800<=year<=2025 :
    print(f"{day +1}/{month}/{year}")
elif month == 2 and day==28 and year%400 == 0 and 1800<=year<=2025 :
    print(f"{day +1}/{month}/{year}")
elif month == 2 and day==28 and year%100 == 0 and 1800<=year<=2025 :
    print(f"1/{month +1}/{year}")
elif month == 2 and day==28 and year%4 != 0 and 1800<=year<=2025 :
    print(f"1/{month +1}/{year}") 
elif month == 3 and 1<=day<=30 and 1800<=year<=2025:
    print(f"{day+1}/{month}/{year}")
elif month == 3 and day==31 and 1800<=year<=2025:
    print(f"1/{month +1}/{year}") 
elif month == 4 and 1<=day<=29 and 1800<=year<=2025:
    print(f"{day+1}/{month}/{year}")
elif month == 4 and day==30 and 1800<=year<=2025:
    print(f"1/{month}/{year}")
elif month == 5 and 1<=day<=30 and 1800<=year<=2025:
    print(f"{day+1}/{month}/{year}")
elif month == 5 and day==31 and 1800<=year<=2025:
    print(f"1/{month}/{year}")
elif month == 6 and 1<=day<=29 and 1800<=year<=2025:
    print(f"{day+1}/{month}/{year}")
elif month == 6 and day==30 and 1800<=year<=2025:
    print(f"1/{month}/{year}")
elif month == 7 and 1<=day<=30 and 1800<=year<=2025 :
    print(f"{day+1}/{month}/{year}")
elif month == 7 and day==31 and 1800<=year<=2025:
    print(f"1/{month}/{year}")
elif month == 8 and 1<=day<=30 and 1800<=year<=2025:
    print(f"{day+1}/{month}/{year}")
elif month == 8 and day==31 and 1800<=year<=2025:
    print(f"1/{month}/{year}")
elif month == 9 and 1<=day<=29 and 1800<=year<=2025:
    print(f"{day+1}/{month}/{year}")
elif month == 9 and day==30 and 1800<=year<=2025:
    print(f"1/{month}/{year}")
elif month == 10 and 1<=day<=30 and 1800<=year<=2025:
    print(f"{day+1}/{month}/{year}")
elif month == 10 and day==31 and 1800<=year<=2025:
    print(f"1/{month}/{year}")
elif month == 11 and 1<=day<=29 and 1800<=year<=2025:
    print(f"{day+1}/{month}/{year}")
elif month == 11 and day==30 and 1800<=year<=2025:
    print(f"1/{month}/{year}")
elif month == 12 and 1<=day<=30 and 1800<=year<=2025:
    print(f"{day+1}/{month}/{year}")
elif month == 12 and day==30 and 1800<=year<=2025:
    print(f"1/{month}/{year +1}")



