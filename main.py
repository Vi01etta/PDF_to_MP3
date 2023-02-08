from gtts  import gTTS
import pdfplumber
from art import tprint
from pathlib import Path


def pdf_to_mp3(file_path="test.pdf", language='ru'):

    #Проверяем, что файл существует и имеет нужный формат

    if Path(file_path).is_file() and  Path(file_path).suffix == '.pdf':
        print(f'[+] Original file: {Path(file_path).name}')
        print(f'[+] Processing....')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages)
        text = text.replace(' ', '').replace('\n', '')
        my_audio = gTTS(text=text, lang=language)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')
        return f'[+]{file_name}.mp3 saved successfully!\n----Have a good day!----'

    else:
        return 'File not exist, check the file'

def main():
    tprint("PDF TO MP3", font='starwars')
    file_path = input("\nEnter a file path: ")
    language =input("choose language, example 'en' or 'ru' ")
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()