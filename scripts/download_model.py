import os

from datasets import load_dataset

os.makedirs("data/raw", exist_ok=True)


def download_wmt14():
    print("Downloading WMT14 English-German")
    dataset = load_dataset("wmt14", "de-en")

    for split in ['train', 'validation', 'test']:
        with open(f"data/raw/{split}.en", "w", encoding="utf-8") as f_en, \
                open(f"data/raw/{split}.de", "w", encoding="utf-8") as f_de:
            for example in dataset[split]:
                f_en.write(example["translation"]["en"].strip() + "\n")
                f_de.write(example["translation"]["de"].strip() + "\n")
