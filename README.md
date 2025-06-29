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
taskmate add <TaskName> 
```
(optional)

```
taskmate add <TaskName> -d <description> -s <status> -p <priority>
```
<h4>Note : status only accepts ['in-progress','done','todo'] defult = todo
</br>
Priority only accepts ["low","medium","high"] default="low"</h4>
<h3>Update a Task</h3>

- Update Name

```
taskmate update <TaskId> -n <NewTaskName>
```

- Update Description

```
taskmate update <TaskId> -d <NewTaskDescription>
```

- Update Priority

```
taskmate update <TaskId> -p <NewTaskPriority>
```
<h3>Note: All the above 3 flags can also be used at the same time </h3>
</br>
<h3> List Tasks </h3>

- List All Task

```
taskmate list
```

- List Task Based on their Status

```
taskmate List done 
```

```
taskmate List in-progress 
```

```
taskmate List todo 
```
</br>
<h3>Delete Task's</h3>

- Delete Task By Providing Their Id

```
taskmate delete <TaskId>
```
- Delete all Task

```
taskmate delete
```
<h3>Change the Status of a Task</h3>

```
taskmate mark <TaskId> <NewStatus>
```
The New Status only accepts done , todo , in-progress
</br>
<h3>Veiw Sort the Tasks </h3>

- Sort Tasks based on their Status
    - todo - in-progress -done

    ```
    taskmate sort -s
    ```
    - done - in-progress - done

    ```
    taskmate sort -S
    ```
- Sort Tasks based on their Priority
    - high - medium - low

    ```
    taskmate sort -p
    ```
    - low - medium - high

    ```
    taskmate sort -P
    ```
<h3>Note : Sorting Doesn't affect the Main Task Table</h3>
</br>
<h4>Special Thanks to Roadmap.sh and Realpython.com </h4>