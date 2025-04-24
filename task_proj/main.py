from task import add_task,remove_task,display_task

def main():
    print("task manager app")
    display_task()
    print(add_task('develop'))
    print(add_task('write unit test'))
    print(add_task('deploy'))
    display_task()
    print(remove_task(0))
    display_task()
    print(remove_task(0))
    display_task()
    print(remove_task(0))
if __name__ =="__main__":
    main()