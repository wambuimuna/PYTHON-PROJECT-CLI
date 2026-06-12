def add_task(tasks, title, description, due_date):
    # very simple helper a student might write
    if not tasks:
        new_id = 1
    else:
        new_id = tasks[-1].get("id", 0) + 1
    task = {
        "id": new_id,
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False,
    }
    tasks.append(task)
    return task


def mark_task_as_complete(tasks, task_id):
    # find task by id and mark done
    for t in tasks:
        if t.get("id") == task_id:
            t["completed"] = True
            return True
    return False


def view_pending_tasks(tasks):
    # return tasks not yet completed
    return [t for t in tasks if not t.get("completed")]


def calculate_progress(tasks):
    # percent complete as float
    if not tasks:
        return 0.0
    total = len(tasks)
    done = sum(1 for t in tasks if t.get("completed"))
    return (done / total) * 100.0
