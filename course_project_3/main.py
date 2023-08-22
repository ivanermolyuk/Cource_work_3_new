from course_project_3 import data
from course_project_3 import executed_operations
from course_project_3 import message

data_list = data.get_input_data('../operations.json')

operations = executed_operations.get_executed_operations(data_list)

for operation in operations:
    print(message.get_message(operation))
