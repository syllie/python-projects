from translate import Translator
translator = Translator(to_lang="ja")

try:
    with open('./test.txt') as my_file:
        text = my_file.readline()

    translation = translator.translate(text)

    with open('./test-ja.txt', 'w', encoding="utf-8") as my_file:
        my_file.write(translation)

    print(translation)
except FileNotFoundError:
    print('File does not exist.')
except UnicodeEncodeError:
    print('Something went wrong')
