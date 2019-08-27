import json
import sys
import os
import subprocess as s

class Chatbot():
    def __init__(self, nome):
        try:
            memoria = open(nome+'.json','r')
        except FileNotFoundError:
            memoria = open(nome+'.json','w')
            memoria.write('[["Will","Alfredo"],{"Hi" : "Hi, what is your name","tchau" : "tchau"}]')
            memoria.close()
            memoria = open(nome+'.json','r')
        self.nome = nome
        self.conhecidos, self.frases = json.load(memoria)
        memoria.close()
        self.historico = [None]

    def escuta(self,frase=None):
        if frase==None:
            frase = input('>: ')
        frase=str(frase)
        frase = frase.lower()
        frase = frase.replace('é','eh')
        return frase

    def pensa(self,frase):
        if frase in self.frases:
            return self.frases[frase]
        if frase == 'aprende':
            chave = input('Digite a frase: ')
            resp = input('Digite a resposta: ')
            self.frases[chave] = resp
            self.gravaMemoria()
            return 'Aprendido'
        if self.historico[-1] == 'Olá, qual o seu nome?':
            nome = self.pegaNome(frase)
            frase = self.respondeNome(nome)
            return frase
        try:
            resp = str(eval(frase))
            return resp
        except:
            pass
        return 'Não entendi'
            
    def pegaNome(self,nome):
        if 'o meu nome eh ' in nome:
            nome = nome[14:]

        nome = nome.title()
        return nome

    def respondeNome(self,nome):
        if nome in self.conhecidos:
            frase = 'Eaew '
        else:
            frase = 'Muito prazer '
            self.conhecidos.append(nome)
            self.gravaMemoria()
            
        return frase+nome
    def gravaMemoria(self):
        memoria = open(self.nome + '.json', 'w')
        json.dump([self.conhecidos,self.frases], memoria)
        memoria.close()

    def fala(self,frase):
        if 'executa ' in frase:
            plataforma = sys.platform
            comando = frase.replace('executa ','')
            if 'win' in plataforma:
                os.startfile(comando)
            if 'linux' in plataforma:
                try:
                    s.Popen(comando)
                except FileNotFoundError:
                    s.Popen(['xdg-open',comando])
        else:
            print(frase)
        self.historico.append(frase)

