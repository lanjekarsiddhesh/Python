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

    # non empty task validation
    if task == "":
        print("Please enter some task.")
        return None

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
        with open("tasks.csv", "+a") as file:
            file.write(f"{index},{task},{date},{time}\n")


def read_tasks(date=""):
    no_task = True
    if os.path.exists("tasks.csv"):
        with open("tasks.csv", 'r') as file:
            # tasks = file.readlines()
            for task in file.readlines():
                if date in task:
                    print(task)
                    no_task = False
               
    if no_task == True:
        print(f"No tasks for {date} date")


def main():
    which_tasks = {1:"Add Task", 2:"Read Task"}

    user = int(input("Which task you perform from above please choose: "))

    if which_tasks[user] == "Add Task":
        # task = input("Enter the task you want to add: ")
        # date = input("Enter the date for this task (YYYY-MM-DD): ")
        # time = input("Enter the time in 12 hrs for this task (HH:MM) with AM/PM: ")
        Add_task()
    elif which_tasks[user] == "Read Task":
        which_task_view = input("if you want all specific date task so please enter date [YYYY-MM-HH] or if not enter blank: ")
        if which_task_view != "":
            read_tasks(which_task_view)
        else:
            read_tasks()
    else:
        print("Enter valid option 1 or 2")

if __name__ == "__main__":
    main()


