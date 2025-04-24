from logger import task_logger
task=[]
def add_task(task_name:str):
    task_logger.debug("DEBUG : Entering function add_task()")
    if not task_name:
        task_logger.warning("WARNING : Attempted to add empty task")
        return "Task name cannot be empty"
    task.append(task_name)
    task_logger.info(f"INFO: task added:'{task_name}'")
def display_tasks():
    task_logger.debug("DEBUG: Entering function display_tasks()")
    if not task:
        task_logger.warning("WARNING: No task found here")
        print(task)
        return 
    task_logger.info("INFO : Displaying tasks")
    for i in task:
        print(i)
        
def remove_tasks(index:int):
    task_logger.debug(f"DEBUG: Attempting to remove task at {index}")
    try:
        removed=task.pop(index)
        task_logger.info(f"INFO: Task at {index} has been removed")
        return removed
    except IndexError as e:
        task_logger.error(f"ERROR : Failed to remove task at index :{index}- {e}")
        return "Index not found"
