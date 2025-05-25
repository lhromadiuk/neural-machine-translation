import os
import re
import string

os.makedirs("data/processed", exist_ok=True)


def preprocess_text(text):
    text = text.lower()
    text = ''.join(ch for ch in text if ch in string.printable)
    text = re.sub(r'[@"]', '', text)
    text = re.sub(r"\s+'", "'", text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def preprocess_file(file):
    for lang in ['en', 'de']:
        input_path = f"data/raw/{file}.{lang}"
        output_path = f"data/processed/{file}.{lang}"
        print(f"Preprocessing {input_path}\n")
        with open(input_path, "r", encoding="utf-8") as fin, \
                open(output_path, "w", encoding="utf-8") as fout:
            for line in fin:
                fout.write(preprocess_text(line) + "\n")


if __name__ == "__main__":
    for split in ['train', 'validation', 'test']:
        preprocess_file(split)
