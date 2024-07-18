
import chat_api
import image_api
import bark_transformer

song_name = input("What do you want your song to be called?: ")
song_desc = input("Briefly describe your song: ")


chat_api.main(song_desc, song_name)
print("------------")
print("Now we shall generate your image!")
image_api.main(song_desc, song_name)
print("------------")
print("------------")
print("------------")
print("Thank you for using our service!")


