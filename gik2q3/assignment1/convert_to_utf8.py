import os

def convert_to_utf8(filename, encodings=('utf-8', 'iso-8859-1', 'windows-1252')):
    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as file:
                content = file.read()
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(content)
            break
        except UnicodeDecodeError:
            continue
    else:
        print(f"Failed to convert {filename}. Unknown encoding.")

if __name__ == '__main__':
    directory = "./dataset"
    
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            convert_to_utf8(filepath)
