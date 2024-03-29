#!usr/bin/python3
"""
  The script accepts an integer as a parameter, which is the employee ID
  The script must display on the standard output the employee TODO list progress in this exact format:
  First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    EMPLOYEE_NAME: name of the employee
    NUMBER_OF_DONE_TASKS: number of completed tasks
    TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
    Second and N next lines display the title of completed tasks: TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""
if __name__ == "__main__":
    import urllib.error as error
    import urllib.request as request

    def make_request(id):
        request_data = request.urlopen(f'https://jsonplaceholder.typicode.com/todos/{id}')
        print(request_data)
