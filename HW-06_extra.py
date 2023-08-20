







def handle_file(path, root_folder, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder/normalize(path.name))


def handle_archive(path, root_folder, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder/normalize(path.name))

    new_name = normalize(path.name.replace('.zip', ''))

    target_folder = root_folder / new_name
    target_folder.mkdir(exist_ok=True)
    try:
        shutil.unpack_archive(str(path.resolve()), str(path.resolve()))
    except 


def remove_empty_folders(path):
    if not any(path.iterdir()):
        path.rmdir()
        remove_empty_folders(path.parent)

def get_folder_object(root_path):
    for folder in root_path.iterdir()


def main(folder_path):
    scan.scan(folder_path)

    for file in scan.jpeg_files:
        handle_file(file, folder_path, 'JPEG')  # шукаємо зображення

    for file in scan.jpg_files:
        handle_file(file, folder_path, 'JPG')   # шукаємо зображення 

    for file in scan.png_files:
        handle_file(file, folder_path, 'PNG')   # шукаємо зображення

    for file in scan.svg_files:
        handle_file(file, folder_path, 'SVG')   # шукаємо зображення

    for file in scan.mp4_files:
        handle_file(file, folder_path, 'MP4')   # шукаємо відео
    
    for file in scan.avi_files:
        handle_file(file, folder_path, 'AVI')   # шукаємо відео
    
    for file in scan.mov_files:
        handle_file(file, folder_path, 'MOV')   # шукаємо відео

    for file in scan.mkv_files:
        handle_file(file, folder_path, 'MKV')   # шукаємо відео

    for file in scan.mp3_files:
        handle_file(file, folder_path, 'MP3')   # шукаємо звук
    
    for file in scan.ogg_files:
        handle_file(file, folder_path, 'OGG')   # шукаємо звук

    for file in scan.wav_files:
        handle_file(file, folder_path, 'WAV')   # шукаємо звук

    for file in scan.amr_files:
        handle_file(file, folder_path, 'AMR')   # шукаємо звук
    
    for file in scan.txt_files:
        handle_file(file, folder_path, 'TXT')   # шукаємо документи 

    for file in scan.docx_files:
        handle_file(file, folder_path, 'DOCX')  # шукаємо документи  
    
    for file in scan.doc_files:
        handle_file(file, folder_path, 'DOC')   # шукаємо документи 
    
    for file in scan.xlsx_files:
        handle_file(file, folder_path, 'XLSX')  # шукаємо документи 
    
    for file in scan.xls_files:
        handle_file(file, folder_path, 'XLS')   # шукаємо документи 

    for file in scan.pptx_files:
        handle_file(file, folder_path, 'PPTX')  # шукаємо документи 

    for file in scan.ppt_files:
        handle_file(file, folder_path, 'PPT')  # шукаємо документи 

    for file in scan.zip_files:
        handle_file(file, folder_path, 'ZIP')  # шукаємо архіви 

    for file in scan.gz_files:
        handle_file(file, folder_path, 'GZ')  # шукаємо архіви 

    for file in scan.tar_files:
        handle_file(file, folder_path, 'TAR')  # шукаємо архіви  

    for file in scan.others_files:
        handle_file(file, folder_path, 'OTHERS')   # шукаємо архіви  

    
    get_folder_object(path)

if __name__ == '__main__':
    parh = sys.argv[1]

    arg = Path(path)

jpeg_files = list()
jpg_files = list()
png_files = list()
svg_files = list()
mp4_files = list()
avi_files = list()
mov_files = list()
mkv_files = list()
mp3_files = list()
ogg_files = list()
wav_files = list()
amr_files = list()
txt_files = list()
docx_files = list()
doc_files = list()
xlsx_files = list()
xls_files = list()
pptx_files = list()
ppt_files = list()
zip_files = list()
gz_files = list()
tar_files = list()
others_files = list()
unknown = list()
extensions = list() 

registered_extentions = {
    'JPEG' : jpeg_files,
    'JPG' : jpg_files,
    'PNG' : png_files,
    

} 