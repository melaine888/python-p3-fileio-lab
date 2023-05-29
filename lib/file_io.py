from pathlib import Path

def write_file(file_name, file_content):
    file_path = Path(file_name).with_suffix('.txt')
    with file_path.open(mode='w') as file:
        file.write(file_content)
def append_file(file_name, append_content):
    file_path = Path(file_name).with_suffix('.txt')
    with file_path.open(mode='a') as file:
        file.write(append_content)
def read_file(file_name):
    file_path = Path(file_name).with_suffix('.txt')
    with file_path.open(mode='r') as file:
        content = file.read()
    return content


    
