def get_file_extension(file_path: str) -> str:
    if not file_path:
        return ""

    file_name = file_path.split("/")[-1]

    if "." not in file_name:
        return ""

    if file_name.startswith(".") and file_name.count(".") == 1:
        return ""

    return file_name.split(".")[-1]
