from gtts import gTTS

text = ''

with open("teste.txt", "r") as arquivo:
    for line in arquivo:
        text += line
    print(arquivo)
    print(text)
audio = gTTS(text, lang="pt-br")

audio.save(f'capitulo_2pt2.mp3')

