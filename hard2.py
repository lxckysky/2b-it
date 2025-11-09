from typing import Dict, Tuple


def main() -> None:
    try:
        line = input()
    except EOFError:
        return

    words = line.split()
    if not words:
        print("")
        return

    freq: Dict[str, int] = {}
    first_seen: Dict[str, int] = {}

    for idx, word in enumerate(words):
        normalized = word.lower()
        if normalized not in freq:
            first_seen[normalized] = idx
            freq[normalized] = 0
        freq[normalized] += 1

    best_word = ""
    best_score: Tuple[int, int] = (-1, len(words)) 
    for word, count in freq.items():
        first_idx = first_seen[word]
        if count > best_score[0] or (count == best_score[0] and first_idx < best_score[1]):
            best_word = word
            best_score = (count, first_idx)

    print(best_word)


if __name__ == "__main__":
    main()