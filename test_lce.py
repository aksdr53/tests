def get_increase_count(arr):
    count = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            count += 1
    return count


def floor(instructions):
    floor = 0
    for symbol in instructions:
        if symbol == '(':
            floor += 1
        else:
            floor -=1
    return floor


arr = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
print(get_increase_count(arr))
instructions = ')))(((('
print(floor(instructions))


SELECT FIRST_NAME, LAST_NAME FROM Employees WHERE MANAGER_ID = NULL

SELECT Employees.FIRST_NAME, Employees.LAST_NAME 
FROM Employees, Departments
WHERE Employees.EMPLOYEE_ID = Departments.MANAGER_ID