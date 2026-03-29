day = input("enter day name:  ").lower()

if day.isdigit():
   print("this is a number we can't let you do something to the system")
   raise ValueError('digits not allowed')

elif isinstance(day,str):
    print("validity check done -> this is string great go ahead --------->")
    match day:
        case "monday":
            print("First day of a week")
        case "tuesday":
            print("Second day of a  week")
        case "wednesday":
            print("third day of a week")
        case "thursday":
            print("fourth day of a week")
        case "friday":
            print("fifth day of a week")
        case "saturday":
            print("sixth day of a week")
        case "sunday":
            print("seventh day of a week")
        
        case _:
            print('the day is not found in our system')
else:
    print("something is wrong")
