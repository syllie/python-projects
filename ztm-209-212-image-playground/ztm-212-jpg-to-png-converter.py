from PIL import Image
import glob
import sys
import os

# write a python script that takes 2 arguments: <sourcefolder>, <outputfolder>
#  sourcefolder should exist
#  outputfolder should be created
#  convert all images from .jpg to .png


def main() -> None:
    if len(sys.argv) > 1:
        source_folder = sys.argv[1]
        output_folder = sys.argv[2]
    else:
        print("provide input and output directory")
        sys.exit(1)

    # ensure arguments have a trailing slash
    source_folder = os.path.join(source_folder, '')
    output_folder = os.path.join(output_folder, '')

    try:
        if not glob.glob(source_folder):
            raise FileNotFoundError('Cannot find source folder')

        if not glob.glob(output_folder):
            os.mkdir(output_folder)

        for source_file in glob.glob(f'{source_folder}*.jpg'):
            # print(os.path.basename(f))  # returns last section of a path
            file, ext = os.path.splitext(os.path.basename(source_file))
            with Image.open(source_file) as img:
                img.save(f'{output_folder}{file}.png', 'png')

    except FileNotFoundError as err:
        print(err)
        exit()
    except OSError as err:
        print(err)


if __name__ == "__main__":
    main()
