from openai import OpenAI
import requests
from datetime import datetime

def main(song_desc, song_name):
    with open("./api_key.txt", "r") as file:
      api_key = file.read().strip()

    client = OpenAI(api_key=api_key)

    print("------------------")
    print("Generating image!")
    print("------------------")

    response = client.images.generate(
      model="dall-e-3",
      prompt= "make an album cover without any text for a song called " + song_name + "such that the song is about " + song_desc
    ,
      n=1,
      size="1024x1024"
    )

    image_url = response.data[0].url

    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        with open(f"./{"Album cover for " + song_name}.png", "wb") as image_file:
            image_file.write(image_response.content)
        print("Image saved successfully.")
    else:
        print("Failed to retrieve the image.")


