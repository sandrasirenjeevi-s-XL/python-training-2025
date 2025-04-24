from logger import task_logger

task=[]

def add_task(task_name:str):
    task_logger.debug("DEBUG : entering function add_task(%)")

    if not task_name:
        task_logger.warning("WARNING : attempt to done a empty task")
        return"task name cannot be empty"
    task.append(task_name)
    
    task_logger.info(f"INFO : task added '{task_name}'")

def display_task():
    task_logger.debug("DEBUG : entering function display_task()")
    if not task:
        task_logger.warning("WARN : no task found here")
        print(task)
        return
    task_logger.info("INFO : Displaying task...")
    for i in task:
        print(i)
def remove_task(index:int):
    task_logger.debug(f"DEBUG : attemptting to remove task at {index}")
    try:
        removed=task.pop(index)
        task_logger.info(f"INFO : task at index {index} had been removed")
        return removed
    except IndexError as e:
        task_logger.error(f"ERROR : failed to remove a task at {index}-{e}")
        return "index not found"
    