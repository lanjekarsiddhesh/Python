import os

def Add_task():
    total_tasks = 0
    if os.path.exists("tasks.csv"):
        with open("tasks.csv", "r") as file:
            total_tasks = len(file.readlines())

    task = input("Enter the task you want to add: ")
    date = input("Enter the date for this task (YYYY-MM-DD): ")
    time = input("Enter the time in 12 hrs for this task (HH:MM) with AM/PM: ")
    index = total_tasks + 1

    # split time
    if "am" in time.lower():
        clean_am_time = time.lower().replace("am", "")
        hour, minutes = clean_am_time.split(":")
    elif "pm" in time.lower():
        clean_pm_time = time.lower().replace("pm", "")
        hour, minutes = clean_pm_time.split(":")
    else:
        print("Please enter AM/PM also")
        return None

    # time vaildation
    if int(hour) > 12:
        print("Enter time in 12 hours format")
        return None
    
    if int(minutes) > 59:
        print("Enter valid minutes")
        return None
        
    # write tasks
    if not os.path.exists("tasks.csv"):
        with open("tasks.csv", "w") as file:
            file.write(f"{index},{task},{date},{time}\n")
    else:
        with open("tasks.csv", "a") as file:
            file.write(f"{index},{task},{date},{time}\n")

Add_task()