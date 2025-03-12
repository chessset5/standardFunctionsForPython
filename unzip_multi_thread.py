import zipfile
import os
from concurrent.futures import ThreadPoolExecutor


def unzip_file_multithreaded(zip_file_path: str) -> None:
    """
    Unzips a ZIP file to the same directory in a multi-threaded fashion.

    Args:
        zip_file_path (str): The path to the ZIP file to be unzipped.

    Raises:
        FileNotFoundError: If the ZIP file does not exist.
        zipfile.BadZipFile: If the ZIP file is corrupted.
    """
    if not os.path.exists(zip_file_path):
        raise FileNotFoundError(f"The file {zip_file_path} does not exist.")
    
    
    output_dir: str = os.path.abspath(zip_file_path).removesuffix(".zip")
    os.makedirs(output_dir,exist_ok=True)

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_objects: list[zipfile.ZipInfo] = zip_ref.infolist()
        tree: list[str] = zip_ref.namelist()
        tree.sort()
        tree = list(map(lambda x: x +"\n", tree))
        
        with open(file= os.path.join(output_dir,"tree.txt"),mode="w",encoding="utf-8") as tree_file:
            tree_file.writelines(tree)

        def extract_member(zip_info: zipfile.ZipInfo) -> None:
            """
            Extracts a single member from the ZIP file.

            Args:
                zip_info (zipfile.ZipInfo): The ZIP file member to extract.
            """
            zip_ref.extract(member=zip_info, path=output_dir)

        with ThreadPoolExecutor(max_workers=1 if __debug__ else None) as executor:
            executor.map(extract_member, zip_objects)


# Example usage
unzip_file_multithreaded(r"C:\Users\Aaron.Shackelford\OneDrive - Lyles Group\Downloads\56.1113.v4_Prj_EngFramework_20250312.zip")
unzip_file_multithreaded(r"C:\Users\Aaron.Shackelford\OneDrive - Lyles Group\Downloads\56.1113.v1_Prj_EngFramework_20250312.zip")
