import os

# Full path to the file
file_path = 'C:\\Users\\a.islam\\OneDrive - Reply\\Documents\\Testing Docs\\Automation\\SUPERVISOR_NO_FLAG.json'

# Check if the file exists
if os.path.exists(file_path):
    # Open the file for reading
    with open(file_path, 'r') as file:
        # Your code to process the file
        file_content = file.read()
        print(file_content)
else:
    print(f"The file '{file_path}' does not exist.")
