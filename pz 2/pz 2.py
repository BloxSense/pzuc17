def calculate_full_kilobytes(file_size_bytes):
    kilobytes = file_size_bytes // 1024
    return kilobytes

file_size_bytes = int(input("Введите размер файла в байтах: "))

full_kilobytes = calculate_full_kilobytes(file_size_bytes)

print(f"Количество полных килобайтов: {full_kilobytes}")
