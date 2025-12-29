def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    if parts[0] != "cp":
        return
    file_in = parts[1]
    file_out = parts[2]
    if file_in == file_out:
        return
    try:
        with open(file_in, "r") as f_in, open(file_out, "w") as f_out:
            f_out.write(f_in.read())
    except FileNotFoundError:
        return
