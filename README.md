<h1>TaskMate</h1>
<h3>A CLI application built with python and argparse module </h3>
<h4>Using Datetime and Tabulate Module</h4>
The app works on the CRUD principle 
allowing users to create , read , update and delete their tasks
</br>
All the Tasks created by the user are saved in a JSON File
</br></br>
This project has been created to test my knowledge on working with functions </br>
and recently learnt  argparse module
</br>
<h2>Features</h2>
<h3>

- Add Task (with Description , Status , Priority)
- Update Task (Name , Description , Priority)
- Mark Task Status
- List Task Based on their Specified Status
- Sort Task based on their Status and Priority
- Delete Task 
</h3>
</br>
<h2>How to use</h2>
<h3>

- Add a Task</h3>

```
TaskMate add <TaskName> 
```
(optional)

```
TaskMate add <TaskName> -d <description> -s <status> -p <priority>
```
<h4>Note : status only accepts ['In-progress','Done','Todo'] defult = Todo (case-senstitve) 
</br>
Priority only accepts ["Low","Medium","High"] default="Low"
(case-senstitve) </h4>
<h3>Update a Task</h3>

- Update Name

```
TaskMate update <TaskId> -n <NewTaskName>
```

- Update Description

```
TaskMate update <TaskId> -d <NewTaskDescription>
```

- Update Priority

```
TaskMate update <TaskId> -p <NewTaskPriority>
```
<h3>Note: All the above 3 flags can also be used at the same time </h3>
</br>
<h3> List Tasks </h3>

- List All Task

```
TaskMate list
```

- List Task Based on their Status

```
TaskMate List Done 
```

```
TaskMate List In-progress 
```

```
TaskMate List Todo 
```
</br>
<h3>Delete Task's</h3>

- Delete Task By Providing Their Id

```
TaskMate delete <TaskId>
```
- Delete all Task

```
TaskMate delete
```
<h3>Change the Status of a Task</h3>

```
TaskMate mark <TaskId> <NewStatus>
```
The New Status only accepts Done , Todo , In-progress
</br>
<h3>Veiw Sort the Tasks </h3>

- Sort Tasks based on their Status
    - Todo - In-progress -Done

    ```
    TaskMate sort -s
    ```
    - Done - In-progress - Done

    ```
    TaskMate sort -S
    ```
- Sort Tasks based on their Priority
    - High - Medium - Low

    ```
    TaskMate sort -p
    ```
    - Low - Medium - High

    ```
    TaskMate sort -P
    ```
<h3>Note : Sorting Doesn't affect the Main Task Table</h3>
</br>
<h4>Special Thanks to Roadmap.sh and Realpython.com </h4>