from translate import Translator


def write_output(output_file, translation):
    if not output_file:
        print(translation)
    else:
        with open(output_file, 'a', encoding="utf-8") as f:
            f.write(translation)
            f.write('\n')


def validate_language(language):
    return language in ['de', 'nl', 'fr', 'en']


try:
    source = input(
        "Source file for translation (ENTER for manual input): ").strip()

    output_file = input(
        "Output file for translation (ENTER for output to screen): ").strip()

    while True:
        input_language = input(
            "Source language (ENTER for English. Valid options: de,nl,fr): ").strip()
        if not input_language:
            input_language = 'en'
            break
        if validate_language(input_language):
            break

    while True:
        output_language = input(
            "Language for translation (ENTER for Dutch. Valid options: en,de,fr: ").strip()
        if not output_language:
            output_language = 'nl'
            break
        if validate_language(output_language):
            break

    translator = Translator(from_lang=input_language, to_lang=output_language)

    # manual mode when no input file is given
    if not source:
        while True:
            text = input("Text to translate (END to stop): ").strip()
            if text == 'END':
                break
            if text:
                translation = translator.translate(text)
                write_output(output_file, translation)

    else:
        # read from file
        with open(source) as f:
            text = f.read()

        translation = translator.translate(text)

        write_output(output_file, translation)

except FileNotFoundError:
    print('File does not exist.')
except UnicodeEncodeError:
    print('Unicode error')
except BaseException:
    print('Something went wrong')
