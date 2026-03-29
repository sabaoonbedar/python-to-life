day = input("enter the day name: ").strip().lower()

list_days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
days_position = ["first","second","third","fourth","fifth","sixth","seventh"]

map_days_position= dict(zip(list_days,days_position))



if day:
  get_value=map_days_position.get(day)
  print(f"{day} is the {get_value} day of the week")
  
else:
    print("wrong input")
