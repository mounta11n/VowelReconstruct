# VowelReconstruct

## Description
VowelReconstruct is a method for testing the intelligence of language models by evaluating their ability to reconstruct text from which almost all vowels have been removed. This repository provides a set of tasks with varying difficulty levels, along with a Python script to measure the performance of language models.

## Motivation
With the rapid development of AI technology, keeping up with the latest innovations and changes in language models can be challenging. Additionally, there is a lack of reliable and valid methods to test local language models for intelligence in a way that is comprehensible for the average user and comparable. The VowelReconstruct method aims to address this by providing a practical and meaningful test to evaluate the intelligence of language models.

## Usage
1. Clone the repository to your local machine.
2. Install the required dependencies mentioned in the repository (Levenshtein).
3. Choose a text file from the provided tasks with varying difficulty levels (easy, medium, or challenging).
4. Run the Python script `vowel_reconstruct.py` with one argument, so that it will remove vowels from the chosen text, excluding words consisting only of vowels.
5. Run the Python script `vowel_reconstruct.py` with two arguments: the original text file and the reconstructed text from the language model. For example: `python vowel_reconstruct.py easy_original.txt reconstructed.txt`.
6. The script will calculate the Levenshtein distance, similarity score, and YASimScore (a combination of distance and similarity. Here lower values indicate better performance).
7. Evaluate the results to assess the intelligence of the language model.

## Results
The repository includes interim results from several measurements conducted using different language models and model sizes. These results provide insights into the performance and intelligence of the tested models. Lower YASimScore, Levenshtein distance, and higher similarity scores indicate better performance.

|     Name     |  Size   | Specifications | Similarity | Levenshtein | YASimScore |
|:------------:|:-------:|:--------------:|:----------:|:-----------:|:----------:|
|   Guanaco    |   7B    |      */*       |   39.81%   |     151     |   379.29   |
|   WizardLM   |   7B    |      q40       |   42.36%   |     194     |   457.90   |
| **--------** | **---** |   **------**   | **------** |   **---**   |  **---**   |
|    Vicuna    |   13B   |     q41_v3     |   44.90%   |     109     |   242.76   |
|    Vicuna    |   13B   |     q41_v3     |   57.64%   |     29      |   50.31    |
|    Vicuna    |   13B   |      q6k       |   51.27%   |     190     |   370.82   |
|   WizardLM   |   13B   |     q40_v3     |   51.27%   |     41      |   79.95    |
|   WizardLM   |   13B   |     q40_v3     |   51.59%   |     31      |   60.09    |
|   WizardLM   |   13B   |     q40_v3     |   51.27%   |     42      |   81.92    |
|   WizardLM   |   13B   |     q40_v3     |   50.00%   |     29      |   58.00    |
|   WizardLM   |   13B   |      q4km      |   57.96%   |     34      |   58.64    |
|   WizardLM   |   13B   |      q6k       |   55.73%   |     41      |   73.52    |
| **--------** | **---** |   **------**   | **------** |   **---**   |  **---**   |
|    based     |   30B   |     q40_v3     |   53.50%   |     108     |   201.87   |
|    LLaMA     |   30B   |    s-hotcot    |   67.20%   |     83      |   123.45   |
| **--------** | **---** |   **------**   | **------** |   **---**   |  **---**   |
| **Guanaco**  | **65B** |   **q40_v3**   |  **99%**   |    **2**    |  **2.01**  |
| **--------** | **---** |   **------**   | **------** |   **---**   |  **---**   |
|   Claude+    |   */*   |      100k      |    93%     |     12      |   12.90    |
|   GPT-3.5    |   */*   |      */*       |   96.18%   |     12      |   12.48    |
|    GPT-4     |   */*   |      */*       |   97.77%   |      2      |    2.04    |

## Contribution
If you have any suggestions, improvements, or additional tests for evaluating language models, feel free to contribute to this repository by submitting a pull request.

## Disclaimer
The VowelReconstruct method is an independent effort and is not associated with any specific language model or organization. It aims to provide a practical way to assess the intelligence of language models based on a specific test scenario.
