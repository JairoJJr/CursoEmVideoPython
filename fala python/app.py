import gtts

nome = str(input('Digite seu nome: '))


from playsound import playsound

with open('frase.txt','r') as arquivo:
    for linha in arquivo:
        frase = gtts.gTTS(linha,lang='pt-br')
        frase.save('frase.mp3')
        playsound('frase.mp3')



