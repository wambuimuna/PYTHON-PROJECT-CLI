from jobnest_cli import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress


def test_add_and_complete():
    tasks = []
    t = add_task(tasks, "Test Task", "Desc", "2024-06-30")
    assert t in tasks
    assert not t["completed"]

    ok = mark_task_as_complete(tasks, t["id"])
    assert ok
    assert tasks[0]["completed"]


def test_view_pending_and_progress():
    tasks = []
    t1 = add_task(tasks, "T1", "d1", "2024-06-30")
    t2 = add_task(tasks, "T2", "d2", "2024-07-01")
    assert len(view_pending_tasks(tasks)) == 2
    mark_task_as_complete(tasks, t1["id"])
    pending = view_pending_tasks(tasks)
    assert len(pending) == 1
    prog = calculate_progress(tasks)
    assert prog == 50.0
