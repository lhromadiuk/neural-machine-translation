from pathlib import Path

import sentencepiece as spm

PROC_DIR = Path("data/processed")
VOCAB_DIR = Path("data/vocab")
VOCAB_DIR.mkdir(parents=True, exist_ok=True)


def train_sentencepiece():
    input_file = PROC_DIR / "train.en"
    model_prefix = VOCAB_DIR / "wmt14_en_de_bpe"
    vocab_size = 8000

    print(f"Training SentencePiece BPE model on {input_file}")
    spm.SentencePieceTrainer.train(
        input=str(input_file),
        model_prefix=str(model_prefix),
        vocab_size=vocab_size,
        character_coverage=1.0,
        model_type='bpe'
    )


if __name__ == "__main__":
    train_sentencepiece()
