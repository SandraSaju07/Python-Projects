# Import the required libraries
from newspaper import Article
import nltk
from gtts import gTTS
import os
import sys

# Function to download and parse the article content from the provided URL
def fetch_article_content(url):
    try:
        # Initialize article object
        article = Article(url)

        # Download and parse the article
        article.download()
        article.parse()

        # Download necessary puntk tokenizer for NLP
        nltk.download('punkt', quiet = True)
        article.nlp()

        # Return article text content
        return article.text
    
    except Exception as e:
        print(f"Error fetching the article: {e}")
        sys.exit(1)
    
# Function to convert and save text to speech
def convert_text_to_speech(content, output_file, language = 'en'):
    try:
        # Convert text content to speech
        tts = gTTS(text = content, lang = language, slow = False)

        # Save the speech to an MP3 file
        tts.save(output_file)
        print(f"The text has been converted to speech and saved as {output_file}", flush = True)

    except Exception as e:
        print('error')
        print(f"Error converting text to speech: {e}")
        sys.exit(1)

# Function to play the saved MP3 file
def play_audio(file_path):
    try:
        if os.name == 'nt':  # For Windows systems
            os.system(f"start {file_path}")
        else:  # For macOS/Linux systems
            os.system(f'open {file_path}' if os.name == 'posix' else f'afplay {file_path}')
    
    except Exception as e:
        print(f"Error playing the audio file: {e}")
        sys.exit(1)
    
# Main function to execute the complete process
def main():
    # User input: URL of the article to be converted to speech
    article_url = input("Enter the article URL: ")

    # Fetch the article content
    article_content = fetch_article_content(article_url)

    # Provide file name for the output speech file
    output_file = 'read_article.mp3'

    # Convert the article content to speech
    convert_text_to_speech(article_content,output_file=output_file)

    # Play the generated MP3 file
    play_audio(output_file)

if __name__ == '__main__':
    main()