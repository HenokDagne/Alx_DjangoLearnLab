import codecs

input_file = r"C:\Users\hp\Documents\alx\Alx_DjangoLearnLab\django_blog\db.json"

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw = f.read(4)
        if raw.startswith(codecs.BOM_UTF16_LE) or raw.startswith(codecs.BOM_UTF16_BE):
            return 'utf-16'
        else:
            return 'utf-8'

encoding = detect_encoding(input_file)

if encoding == 'utf-16':
    # Read as UTF-16 and overwrite as UTF-8
    with codecs.open(input_file, 'r', encoding='utf-16') as f:
        content = f.read()
    with codecs.open(input_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Converted {input_file} from UTF-16 to UTF-8 in-place.")
else:
    print(f"{input_file} is already UTF-8 encoded.")
    # Optionally, display the content
    with codecs.open(input_file, 'r', encoding='utf-8') as f:
        print(f.read())