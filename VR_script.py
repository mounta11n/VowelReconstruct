import sys
import os
from typing import Tuple
import re
from Levenshtein import distance as levenshtein_distance


def remove_vowels(text: str) -> str:
    lines = text.split("\n")
    new_lines = []
    for line in lines:
        words = line.split()
        new_words = []
        for word in words:
            if not re.search("[^aeiouAEIOUäüöÄÜÖ]", word):
                new_words.append(word)
            else:
                new_words.append(re.sub("[aeiouAEIOUäüöÄÜÖ]", "", word))
        new_lines.append(" ".join(new_words))
    return "\n".join(new_lines)


def calculate_similarity(original_text: str, reconstructed_text: str) -> float:
    original_words = original_text.split()
    reconstructed_words = reconstructed_text.split()
    total_chars = sum(len(word) for word in original_words)
    matches = 0

    index_reconstructed = 0
    for original_word in original_words:
        while index_reconstructed < len(reconstructed_words):
            reconstructed_word = reconstructed_words[index_reconstructed]

            if original_word == reconstructed_word:  # exact match
                matches += len(original_word)
                index_reconstructed += 1
                break
            else:
                # Check if a word is missing in the reconstructed text
                missing_word = True
                for c in reconstructed_word:
                    if c in original_word:
                        matches += 1
                        original_word = original_word.replace(c, "", 1)
                        missing_word = False
                if missing_word:
                    index_reconstructed += 1
                else:
                    break

    similarity_percentage = (matches / total_chars) * 100
    return similarity_percentage


def calculate_levenshtein(original_text: str, reconstructed_text: str) -> int:
    return levenshtein_distance(original_text, reconstructed_text)


def process_scenario(arguments: Tuple[str, ...]):
    if len(arguments) == 0:
        original_text = "The letter I have written today is longer than usual because I lacked the time to make it shorter."
        reconstructed_text = "The letter I have write today is longer then usually because I lacked the time to make it shorter."
        similarity = calculate_similarity(original_text, reconstructed_text)
        levenshtein = calculate_levenshtein(original_text, reconstructed_text)
        yasim_score = levenshtein / (similarity / 100)
        print(f"Similarity Value: {similarity}%")
        print(f"Levenshtein-Distance: {levenshtein}")
        print(f"YASimScore: {yasim_score}")

    elif len(arguments) == 1:
        input_path = arguments[0]
        output_path = "TASK_" + os.path.basename(input_path)

        with open(input_path, "r") as input_file:
            original_text = input_file.read()

        task_text = remove_vowels(original_text)

        with open(output_path, "w") as output_file:
            output_file.write(task_text)

        print(f"Saved TASK text in {output_path}")

    elif len(arguments) == 2:
        input_path1, input_path2 = arguments

        with open(input_path1, "r") as input_file1:
            original_text = input_file1.read()

        with open(input_path2, "r") as input_file2:
            reconstructed_text = input_file2.read()

        similarity = calculate_similarity(original_text, reconstructed_text)
        levenshtein = calculate_levenshtein(original_text, reconstructed_text)
        yasim_score = levenshtein / (similarity / 100)
        print(f"Similarity Value: {similarity}%")
        print(f"Levenshtein-Distance: {levenshtein}")
        print(f"YASimScore: {yasim_score}")

    elif len(arguments) == 3:
        input_path1, input_path2, input_path3 = arguments

        with open(input_path1, "r") as input_file1:
            original_text = input_file1.read()

        with open(input_path2, "r") as input_file2:
            task_text = input_file2.read()

        with open(input_path3, "r") as input_file3:
            reconstructed_text = input_file3.read()

        similarity = calculate_similarity(original_text, reconstructed_text)
        levenshtein = calculate_levenshtein(original_text, reconstructed_text)
        difficulty = (len(original_text) - len(task_text)) / len(original_text) * 100
        yasim_score = levenshtein / (similarity / 100)
        print(f"Similarity Value: {similarity}%")
        print(f"Levenshtein-Distance: {levenshtein}")
        print(f"Difficulty: {difficulty}%")
        print(f"YASimScore: {yasim_score}")

    else:
        print("Too many arguments, please provide 0 to 3 arguments.")


if __name__ == "__main__":
    process_scenario(tuple(sys.argv[1:]))
