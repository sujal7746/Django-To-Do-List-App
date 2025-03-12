A simple web-based To-Do List application built with Django, a powerful Python web framework. This app allows users to add, delete, update, and toggle the completion status of tasks, with an interactive interface and an admin panel for managing tasks. Tasks are stored in a SQLite database by default.<br />

**Features**<br />
Add Tasks: Enter a task and add it to your list.<br />
Delete Tasks: Remove tasks you no longer need.<br />
Update Tasks: Edit task titles and mark them as completed.<br />
Toggle Completion: Quickly mark tasks as done or undone.<br />
Admin Interface: Manage tasks via Django’s built-in admin panel.<br />
Persistent Storage: Tasks are saved in a SQLite database (db.sqlite3).<br />
Styled Interface: Basic CSS for a clean, user-friendly look.<br />

**Requirements**<br />
Python 3.x<br />
Django (pip install django)<br />

**Usage**<br />
Add a Task:<br />
On the main page (/), type a task in the input box and click "Add".<br />
Toggle Completion:<br />
Click "Done" to mark a task as complete (or "Undo" to revert).<br />
Edit a Task:<br />
Click "Edit" to update the task title or completion status.<br />
Delete a Task:<br />
Click "Delete" to remove a task.<br />
Admin Panel:<br />
Visit /admin, log in with your superuser credentials, and manage tasks.<br />
Tasks are stored in db.sqlite3 and persist between sessions.<br />

**Code Overview**<br />
todos/models.py:<br />
Defines the Task model with fields for title, completion status, and creation date.<br />
todos/views.py:<br />
Handles logic for adding, deleting, updating, and toggling tasks.<br />
todos/urls.py:<br />
Maps URLs to views (e.g., /delete/<task_id>).<br />
todo_project/urls.py:<br />
Includes app URLs and admin panel routing.<br />
todos/templates/todos/index.html:<br />
Displays the task list and form to add tasks.<br />
todos/templates/todos/update_task.html:<br />
Form for editing tasks with basic CSS.<br />
todos/admin.py:<br />
Registers the Task model with the admin interface.<br />
Main Page: Task list with add/delete options.<br />
Update Page: Editing a task.<br />
Admin Panel: Managing tasks.<br />

**Troubleshooting**
Error: "No module named django"<br />
Run pip install django again.<br />
Page Not Found:<br />
Ensure URLs are correctly set up in urls.py.<br />
Database Issues:<br />
Delete db.sqlite3 and rerun python manage.py migrate to reset.<br />
