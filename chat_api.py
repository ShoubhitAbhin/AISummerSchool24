from openai import OpenAI
import bark_transformer
import break_text
import merge_audio


def main(song_desc, song_name):
    with open("./api_key.txt", "r") as file:
      api_key = file.read().strip()

    client = OpenAI(api_key=api_key)

    print("Working on it!")

    response = client.chat.completions.create(
      model="gpt-4o",
      messages=[
        {
          "role": "system",
          "content": """write an amazing rap song which has a length of 12 lines, only the song no outline about the verse, intro, outro etc. write this song about"""
        },
        {
          "role": "user",
          "content": song_desc
        }
      ],
      temperature=0.6,
      max_tokens=1000,
      n=1
    )

    text = response.choices[0].message.content


    print("\n---------------------------------\n")
    print("This is your song: ")
    print(text)
    print("\n---------------------------------\n")
    print("Audio file being generated!")
    break_text.main(text, song_name)
    merge_audio.main()
    print("")
    print("\n---------------------------------\n")
    print("Audio file generated!")
    print("\n---------------------------------\n")

  
