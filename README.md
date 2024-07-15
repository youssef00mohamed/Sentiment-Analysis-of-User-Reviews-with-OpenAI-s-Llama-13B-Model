# Sentiment Analysis with OpenAI's Llama-13B Model

## Overview
This project demonstrates how to perform sentiment analysis on user-provided text using OpenAI's Llama-13B model through the LlamaAPI. It allows users to input a review, which is then analyzed to determine if the sentiment is positive or negative.

## Example
Here is an example of how the output will look:

Write your review: This product exceeded my expectations!
Review: This product exceeded my expectations!
Sentiment: Positive

## Prerequisites
Before running the script, ensure you have the following:
- Python 3 installed on your system
- An API key for accessing OpenAI's services (replace `"Your-Api-Key"` in the script with your actual API key)
- Required Python libraries installed:
  
```bash
pip install llamaapi openai
```

## Usage  

1. **Clone the repository to your local machine:**
   
  ```bash
  git clone https://github.com/youssef00mohamed/Sentiment-Analysis-of-User-Reviews-with-OpenAI-s-Llama-13B-Model
  cd Sentiment-Analysis-of-User-Reviews-with-OpenAI-s-Llama-13B-Model
  ```

2. **Replace `Your-Api-Key` in `llama.py` with your actual OpenAI API key.**
   
3. **Run the script:**
   
  ```bash
  python llama.py
  ```
4. **View Results**
   - The script will output the review you provided and its sentiment classification (either "Positive" or "Negative").


## Contribution

Contributions to this repository are welcome! If you have suggestions for improvements, additional analyses, or new datasets to explore, please feel free to open an issue or pull request. Ensure that your contributions align with the project's objectives and maintain code quality and documentation standards.

## License

This project is licensed under the [MIT License](LICENSE).
