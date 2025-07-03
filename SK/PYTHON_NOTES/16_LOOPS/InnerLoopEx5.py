#Display 12 Months Calendar for 2023,2024 and 2025
#InnerLoopEx5.py
import calendar as c
for year in range(2023,2026): # Outer For Loop Supply Year
    print("="*50)
    print("12 Months Calendar for {}".format(year))
    print("=" * 50)
    for i in range(1,13): # Inner For Loop Suply Months
        print(c.month(year,i))
    else:
        print("=" * 50)

