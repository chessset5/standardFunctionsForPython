import zlib

def calculate_crc32(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
        crc32 = zlib.crc32(file_data)
        return crc32 & 0xFFFFFFFF

file_path = r"C:\Users\Aaron.Shackelford\OneDrive - Lyles Group\Dev\Archive\Streamline-Backend-Old-SI-FS01\app\briareus\data\Direct Folder Shortcuts\0201.EDC - Shortcut.lnk"
crc32_value = calculate_crc32(file_path)
print(f"CRC32: {crc32_value}")