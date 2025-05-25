import json
from pathlib import Path

import sentencepiece as spm

sp = spm.SentencePieceProcessor()
sp.load("data/vocab/wmt14_en_de_bpe.model")

special_tokens = {
    "<pad>": 0,
    "<sos>": sp.get_piece_size(),
    "<eos>": sp.get_piece_size() + 1
}


def encode_line(line, sp, max_len=100):
    ids = sp.encode(line.strip(), out_type=int)[:max_len]
    return [special_tokens["<sos>"]] + ids + [special_tokens["<eos>"]]


def encode_file(split, lang):
    in_path = Path(f"data/processed/{split}.bpe.{lang}")
    out_path = Path(f"data/encoded/{split}.{lang}.ids.json")

    print(f"Encoding {in_path} → {out_path}")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    encoded = []
    with in_path.open("r", encoding="utf-8") as f:
        for line in f:
            encoded.append(encode_line(line, sp))

    with out_path.open("w", encoding="utf-8") as f:
        json.dump(encoded, f)


if __name__ == "__main__":
    for split in ['train', 'validation', 'test']:
        for lang in ['en', 'de']:
            encode_file(split, lang)
