import os
import shutil
import datetime


def replicate_files(source_dir, destination_dirs):
    """
    Replicates files from the source directory to multiple destination directories.

    Args:
        source_dir (str): Path to the source directory containing the files to be duplicated.
        destination_dirs (list): List of destination directories where the files should be duplicated.
    """

    if not os.path.isdir(source_dir):
        raise ValueError(f"Source directory '{source_dir}' does not exist.")

    for destination_dir in destination_dirs:
        if not os.path.isdir(destination_dir):
            os.makedirs(destination_dir)

        for filename in os.listdir(source_dir):
            source_file_path = os.path.join(source_dir, filename)
            destination_file_path = os.path.join(destination_dir, filename)

            if os.path.isfile(source_file_path):
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                timestamped_filename = f"{filename}-{timestamp}"
                timestamped_destination_file_path = os.path.join(destination_dir, timestamped_filename)

                try:
                    shutil.copy2(source_file_path, timestamped_destination_file_path)
                except Exception as e:
                    print(f"Error copying file '{filename}' to '{timestamped_destination_file_path}': {e}")


if __name__ == "__main__":
    source_dir = input("Enter the source directory path: ")
    destination_dirs = input("Enter a comma-separated list of destination directories: ").split(",")

    replicate_files(source_dir, destination_dirs)