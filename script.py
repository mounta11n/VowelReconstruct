import sys
import os
import math
from typing import Tuple
import re
from Levenshtein import distance as levenshtein_distance

PATH_TEXT_MAPPING = {
    "1": (387, "solution-1-easy.md"),
    "2": (980, "solution-2-medium.md"),
    "3": (2084, "solution-3-challenging.md")
}

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
        sym_score = levenshtein / (similarity / 100)
        print(f"Similarity Value: {similarity}%")
        print(f"Levenshtein-Distance: {levenshtein}")
        print(f"SymScore: {sym_score}")
    elif len(arguments) == 2: 
        try:
            original_text_length, original_text_path = PATH_TEXT_MAPPING[arguments[0]]

            reconstructed_text_path = arguments[1]
            
            with open(original_text_path, "r") as original_file:
                original_text = original_file.read()

            with open(reconstructed_text_path, "r") as reconstructed_file:
                reconstructed_text = reconstructed_file.read()

            similarity = calculate_similarity(original_text, reconstructed_text)
            similarity2 = float(similarity) / 100
            levenshtein = calculate_levenshtein(original_text, reconstructed_text)
            levenshtein_ratio = float(levenshtein) / float(original_text_length)  # Calculate LevDistance relative
            
            sim_score2 = float(similarity2) / float(levenshtein_ratio)               # Calculate undefined division by LevDistance rel  
            
            # Modify the math: (Score^2 + 30), then take the log10, and finally square the result
            log10_value = math.pow(math.log10(pow(sim_score2, 2) + 30), 2)

            similarity_round = round(similarity, 1)
            levenshtein_ratio_round = round(levenshtein_ratio, 2)
            log10_value_round = round(log10_value, 2)

            print(f"==========================")        
            print(f"Similarity Value     {similarity_round}%")
            # print(f"Similarity / 100: {similarity2}")
            print(f"Levenshtein-Distance {levenshtein}")
            print(f"Lev-Distance(rel)    {levenshtein_ratio_round}")
            # print(f"sim_score2 : {sim_score2}")
            print(f"==========================")
            print(f"Sym-{arguments[0]}-Score          {log10_value_round}")
            print(f"==========================")                             
            
        except KeyError as e:
            print("Error: Invalid option specified. Please provide 1, 2, or 3 as the first argument.")

    else:
        print("Error: Invalid number of arguments. Please provide either 0 or 2 arguments.")


if __name__ == "__main__":
    process_scenario(tuple(sys.argv[1:]))