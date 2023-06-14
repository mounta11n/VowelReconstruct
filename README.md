# VowelReconstruct

## Description
VowelReconstruct is a method for testing the intelligence of language models by evaluating their ability to reconstruct text from which almost all vowels have been removed. This repository provides a set of tasks with varying difficulty levels, along with a Python script to measure the performance of language models.

## Motivation
With the rapid development of AI technology, keeping up with the latest innovations and changes in language models can be challenging. Additionally, there is a lack of reliable and valid methods to test local language models for intelligence in a way that is comprehensible and comparable. The VowelReconstruct method aims to address this by providing a practical and meaningful test to evaluate the intelligence of language models.

## Usage
1. Clone the repository to your local machine.
2. Install the required dependencies mentioned in the repository.
3. Choose a text file from the provided tasks with varying difficulty levels (easy, medium, or challenging).
4. Remove almost all vowels from the chosen text, excluding words consisting only of vowels.
5. Run the Python script `vowel_reconstruct.py` with the original text file and the reconstructed text from the language model as arguments. For example: `python vowel_reconstruct.py original.txt reconstructed.txt`.
6. The script will calculate the Levenshtein distance, similarity score, and YASimScore (a combination of distance and similarity). Lower values indicate better performance.
7. Evaluate the results to assess the intelligence of the language model.

## Results
The repository includes interim results from several measurements conducted using different language models and model sizes. These results provide insights into the performance and intelligence of the tested models. Lower YASimScore, Levenshtein distance, and higher similarity scores indicate better performance.

## Contribution
If you have any suggestions, improvements, or additional tests for evaluating language models, feel free to contribute to this repository by submitting a pull request.

## Disclaimer
The VowelReconstruct method is an independent effort and is not associated with any specific language model or organization. It aims to provide a practical way to assess the intelligence of language models based on a specific test scenario.
