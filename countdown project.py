from datetime import datetime

user_input = input("please enter your goal and deadline[dd.mm.yyyy] separated by colon:\n ")
user_list = user_input.split(":")

goal = user_list[0]
deadline = user_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()
remaining_time = deadline_date-today_date
remaining_time_in_hours = int(remaining_time.total_seconds()/60/60)

print(f"time remaining for your goal of {goal} is {remaining_time_in_hours} hours")