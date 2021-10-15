import requests
from tok import TOKEN
from pprint import pprint
from ya_disk import YandexDisk


if __name__ == '__main__':
    ya = YandexDisk(token=TOKEN)
    # pprint(ya.get_files_list())
    # ya._get_upload_link('Test/')
    ya.upload_file_to_disk('Test/ljaljalja-1.mp3', 'ljaljalja-1.mp3')

