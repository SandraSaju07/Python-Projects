# Import required libraries
import os
import sys
from pytubefix import YouTube
from pydub import AudioSegment
import speech_recognition as sr

# Function to download audio of a YouTube video as MP4
def download_audio(youtube_url, output_path):
    try:
        # Create a youtube object
        yt = YouTube(youtube_url)

        # Get the audio stream and download it
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_file = audio_stream.download(output_path)

        print(f"Downloaded audio: {audio_file}")
        return audio_file
    
    except Exception as e:
        print(f"An error occurred during download: {e}")
        sys.exit(1)

# Function to convert the audio file to WAV file from WAP4 format
def convert_audio_to_wav(audio_file):
    try:
        # Convert audio to WAV format using pydub
        audio_segment = AudioSegment.from_file(audio_file)
        wav_file = audio_file.replace(".mp4",".wav")  
        audio_segment.export(wav_file,format='wav')

        print(f"Converted to WAV: {wav_file}")
        return wav_file
    
    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        sys.exit(1)

# Function to transcribe the audio using Speech Recognition
def transcribe_audio(wav_file):
    # Initialize Speech Recognition object
    recognizer = sr.Recognizer()
    transcription = ""

    # Read and recognize the audio using Speech Recognition
    try:
        with sr.AudioFile(wav_file) as source:
            # Read the entire audio
            audio_data = recognizer.record(source)
            # Use Google Web Speech API
            transcription = recognizer.recognize_google(audio_data)
        
        print("Transcription completed.")
        return transcription
    
    except sr.UnknownValueError:
        print(f"Google Speech Recognition could not understand audio")
        return None
    
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service: {e}")
        return None
    
# Function to save the transcription to a text file
def save_transcription(transcription, output_path):
    try:
        with open(output_path,'w') as file:
            file.write(transcription)

        print(f"Transcription saved to: {output_path}")

    except Exception as e:
        print(f"An error occurred while saving transcription: {e}")

# Main file to run the complete process      
def main():
    # Input YouTube video URL
    youtube_url = input("Enter YouTube video URL: ")

    # Output path for audio file saving
    output_path = "./output"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # Download audio from youtube
    audio_file = download_audio(youtube_url, output_path)

    # Convert audio to WAV file format
    wav_file = convert_audio_to_wav(audio_file)

    # Transcribe the audio
    transcription = transcribe_audio(wav_file)

    if transcription:
        # Save transcription to text file
        output_path = os.path.join(output_path, 'transcription.txt')
        save_transcription(transcription, output_path)

    # Clean up: Remove the downloaded audio files if needed
    os.remove(audio_file)
    os.remove(wav_file)

if __name__ == "__main__":
    main()