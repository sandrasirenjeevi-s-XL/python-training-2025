from task import display_tasks,add_task,remove_tasks
def main():
    print("Task manager App")
    display_tasks()
    print(add_task("Develop"))
    print(add_task("Write Unit Test"))
    print(add_task("Deploy"))
    display_tasks()
    print(remove_tasks(0))
    display_tasks()
    print(remove_tasks(0))
    display_tasks()
    print(remove_tasks(0))
    display_tasks()
    print(remove_tasks(0))
if __name__=="__main__":
    main()
