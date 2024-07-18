from pydub import AudioSegment
import os

def main():
    # Set the root folder where the audio files are stored
    root_folder = '.'

    # List all audio files in the root folder
    audio_files = [f for f in os.listdir(root_folder) if f.endswith('.wav')]

    # Sort the files in sequential order (assuming they are named in order)
    audio_files.sort()

    # Initialize an empty AudioSegment
    merged_audio = AudioSegment.empty()

    # Loop through each audio file and append it to the merged_audio
    for audio_file in audio_files:
        audio_path = os.path.join(root_folder, audio_file)
        audio_segment = AudioSegment.from_file(audio_path)
        merged_audio += audio_segment

    # Export the merged audio to a new file
    output_path = os.path.join(root_folder, 'merged_audio.mp3')
    merged_audio.export(output_path, format='wav')

    print(f'Merged audio saved as {output_path}')
