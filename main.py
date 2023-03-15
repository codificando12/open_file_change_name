import os
from translate import Translator

os.chdir(r'ESCRIBI LA CARPETA DONDE ESTAN LOS ARCHIVOS')

translator = Translator(to_lang='zh')
for name in os.listdir():
    src = name
    divide_name = src.split('.')
    trans_name = divide_name[0]
    print(trans_name)
    translation = translator.translate(trans_name)
    print(translation)
    
    # translated_name = translator.translate(trans_name, dest="en")
    dst = translation +'.'+divide_name[1]
    # dst = translated_name +'.docx'
    os.rename(src, dst)
    






