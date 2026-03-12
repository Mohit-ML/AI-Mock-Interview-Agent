# AI Mock Interview Agent

This is a simple AI based mock interview project built using Python.

The goal of this project is to simulate a basic interview environment where a user can answer interview questions and the system evaluates the answer using semantic similarity.

The program asks some basic AI and Machine Learning related interview questions. The user writes their answer in the terminal, and the system compares the user's answer with an expected answer.

To compare the answers, the project uses a sentence transformer model to convert text into embeddings and then calculates cosine similarity between the user's answer and the expected answer.

Based on the similarity score, the system gives feedback such as:
- Correct
- Partially Correct
- Incorrect

## Technologies Used

- Python  
- Sentence Transformers  
- Scikit-learn  

## How the project works

1. The program stores interview questions and expected answers.
2. The system asks a question to the user.
3. The user types their answer.
4. The program converts both answers into embeddings.
5. Cosine similarity is calculated between them.
6. Based on the similarity score, the answer is evaluated.

## How to run the project

1. Install the required libraries
Run this program

## Example

Question: What is machine learning?

User answer: computers learn patterns from data

Output:
Similarity score: 0.72  
Result: Correct Answer

## Future Improvements

- Add more interview questions  
- Build a web interface  
- Add scoring system for the full interview  

- Store interview results for users

## Features

- Simple AI mock interview simulation
- Multiple interview questions
- Answer evaluation using semantic similarity
- Cosine similarity scoring
- Python based implementation

- ## Future Improvements

- Add web interface
- Add scoring system for full interview
- Add more interview questions
