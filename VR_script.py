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
        print("Do you want to edit a text and remove its vowels or do you want to calculate a Sym-Score?")
        print("1: Edit text")
        print("2: Calculate Sym-Score")
        choice = input("Enter 1 or 2: ")

        if choice == "1":
            txt_files = [f for f in os.listdir() if f.endswith(('.txt', '.md'))]
            print("Select a file to be edited:")
            for i, f in enumerate(txt_files):
                print(f"{i + 1}: {f}")
            file_choice = int(input("Enter the number of the file: ")) - 1
            file_path = txt_files[file_choice]

            with open(file_path, "r") as file:
                content = file.read()

            new_content = remove_vowels(content)
            new_file_path = "task-" + file_path

            with open(new_file_path, "w") as new_file:
                new_file.write(new_content)

            print(f"File was edited and saved as {new_file_path}.")

        elif choice == "2":
            print("Which Sym-Score do you want to calculate?")
            print("Sym-1-Score")
            print("Sym-2-Score")
            print("Sym-3-Score")
            sym_choice = input("Enter 1, 2 or 3: ")

            txt_files = [f for f in os.listdir() if f.endswith(('.txt', '.md'))]
            print("Select a file to calculate the Sym-Score:")
            for i, f in enumerate(txt_files):
                print(f"{i + 1}: {f}")
            file_choice = int(input("Enter the number of the file: ")) - 1
            file_path = txt_files[file_choice]

            with open(file_path, "r") as file:
                content = file.read()

            process_scenario((sym_choice, content, file_path))

        else:
            print("Invalid entry. Please enter 1 or 2.")
            return
    elif len(arguments) == 3:
        try:
            original_text_length, original_text_path = PATH_TEXT_MAPPING[arguments[0]]

            reconstructed_text = arguments[1]
            file_path = arguments[2]
            
            with open(original_text_path, "r") as original_file:
                original_text = original_file.read()

            similarity = calculate_similarity(original_text, reconstructed_text)
            similarity2 = float(similarity) / 100
            levenshtein = calculate_levenshtein(original_text, reconstructed_text)
            levenshtein_ratio = float(levenshtein) / float(original_text_length)
            sim_score2 = float(similarity2) / float(levenshtein_ratio)
            
            # (Score^2 + 30), then take the log10, and finally square the result
            log10_value = math.pow(math.log10(pow(sim_score2, 2) + 30), 2)

            similarity_round = round(similarity, 1)
            levenshtein_ratio_round = round(levenshtein_ratio, 2)
            log10_value_round = round(log10_value, 2)

            print(f"=============================")        
            print(f"Similarity Value        {similarity_round}%")
            print(f"Levenshtein-Distance    {levenshtein}")
            print(f"Lev-Distance(rel)       {levenshtein_ratio_round}")
            print(f"=============================")
            print(f"Sym-{arguments[0]}-Score             {log10_value_round}")
            print(f"=============================")                             
            
            # Save the results to a new file
            new_file_name = f"sym_{arguments[0]}_score-{os.path.basename(file_path)}"
            with open(new_file_name, "w") as new_file:
                new_file.write(f"=============================\n")        
                new_file.write(f"Similarity Value        {similarity_round}%\n")
                new_file.write(f"Levenshtein-Distance    {levenshtein}\n")
                new_file.write(f"Lev-Distance(rel)       {levenshtein_ratio_round}\n")
                new_file.write(f"=============================\n")
                new_file.write(f"Sym-{arguments[0]}-Score             {log10_value_round}\n")
                new_file.write(f"=============================\n\n")
                new_file.write(reconstructed_text)
                new_file.write("\n\n")
                with open(original_text_path, "r") as original_file:
                    new_file.write(original_file.read())

            print(f"Results saved to {new_file_name}")

        except KeyError as e:
            print("Error: Invalid option specified. Please provide 1, 2, or 3 as the first argument.")

    else:
        print("Error: Invalid number of arguments. Please provide either 0 or 3 arguments.")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        _, sym_choice, file_path = sys.argv
        with open(file_path, "r") as file:
            content = file.read()
        process_scenario((sym_choice, content, file_path))
    else:
        process_scenario(tuple(sys.argv[1:]))