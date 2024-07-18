import bark_transformer


def main(text, song_name):
    paragraph = text

    lines = paragraph.splitlines()

    i = 0
    for line in lines:
        bark_transformer.main(line, song_name, i)
        i = i + 1