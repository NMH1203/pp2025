import os
import zipfile as zf

def compress_data():
    file_to_compress = ["student.txt", "mark.txt", "courses.txt"]

    with zf.ZipFile("students.dat", "w", zf.ZIP_DEFLATED) as zipf:
        for file in file_to_compress:
            if os.path.exists(file):
                zipf.write(file)
    
    print("the data complete compress")