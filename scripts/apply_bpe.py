from pathlib import Path

import sentencepiece as spm

PROC_DIR = Path("data/processed")
VOCAB_DIR = Path("data/vocab")
BPE_MODEL = VOCAB_DIR / "wmt14_en_de_bpe.model"


def apply_bpe(split):
    sp = spm.SentencePieceProcessor(model_file=str(BPE_MODEL))

    for lang in ['en', 'de']:
        input_file = PROC_DIR / f"{split}.{lang}"
        output_file = PROC_DIR / f"{split}.bpe.{lang}"

        if not input_file.exists():
            continue

        print(f"Applying BPE")

        with input_file.open("r", encoding="utf-8") as fin, \
                output_file.open("w", encoding="utf-8") as fout:
            for line in fin:
                pieces = sp.encode(line.strip(), out_type=str)
                fout.write(" ".join(pieces) + "\n")

        print(f"BPE applied to {split}.{lang}")


if __name__ == "__main__":
    for split in ['train', 'validation', 'test']:
        apply_bpe(split)
