def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    command_name, source_file_path, destination_file_path = parts
    if command_name != "cp" or source_file_path == destination_file_path:
        return
    try:
        with (open(source_file_path, "r") as source_file,
              open(destination_file_path, "w") as copied_file):
            copied_file.write(source_file.read())
    except FileNotFoundError:
        return
