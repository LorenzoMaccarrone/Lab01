import random

class NicknamePunteggio:
    def __init__(self,nickname,punteggio):
        self.nickname = nickname
        self.punteggio = int(punteggio)
    def __str__(self):
        return f'{self.nickname} {self.punteggio}'
    def __repr__(self):
        return f'{self.nickname} {self.punteggio}'
class Risposta:
    def __init__(self,risposta,corretta):
        self.risposta=risposta
        self.corretta=corretta
    def __str__(self):
        return self.risposta
    def __repr__(self):
        return self.risposta


class Domanda:
   def __init__(self, domanda, livello):
       self.domanda = domanda
       self.livello = int(livello)
       self.risposte = []
   def setRisposte(self, risposta1, risposta2, risposta3, risposta4):
       self.risposte.append(risposta1)
       self.risposte.append(risposta2)
       self.risposte.append(risposta3)
       self.risposte.append(risposta4)
   def getRisposta(self):
       return self.risposte


   def __str__(self):
       s = f" {self.domanda} \n {self.livello} \n"
       for c in self.risposte:
           s+=f" {c} \n"
       return s





def main ():
   f = open("Domande.txt", "r")
   righe = f.readlines()
   domande=[]
   #tolgo i \n
   for riga in righe:
       domande.append(riga.rstrip('\n'))
   count=0
   count1=0
   question=[]

   while count<len(domande):
       q=Domanda(domande[count], domande[count + 1])
       q.setRisposte(Risposta(domande[count + 2],1),Risposta(domande[count + 3],0),Risposta(domande[count + 4],0),Risposta(domande[count + 5],0))
       question.append(q)
       count+=7
   #controlliamo quanti livelli ci sono in modo da sapere quando stoppare il ciclo delle domande
   livello_massimo=0
   for q in question:
       if(q.livello>livello_massimo):
           livello_massimo=q.livello
   #salviamo i nomi già presenti all'interno del file
   f = open("punti.txt", "r")
   scores = []
   righe1 = f.readlines()
   for riga in righe1:
       scores.append(riga.rstrip('\n'))
   punteggi = []
   rough = []
   for s in scores:
       rough = s.split()
       punteggi.append(NicknamePunteggio(rough[0], rough[1]))
   f.close()
   vincita=0
   perdita=0
   domanda_trovata=0
   domande_shuffled=list(question)
   random.shuffle(domande_shuffled)
   livello_attuale=0
   #ciclo per far funzionare il gioco
   while vincita==0 & perdita==0:
       print("RISPONDI ALLE SEGUENTI DOMANDE")
       for q in domande_shuffled:
           if livello_attuale==livello_massimo+1:
               print("Bravo hai vinto!")

               #agiorniamo e stampiamo la leaderboard nel file
               nome_giocatore=input("Dimmi il tuo nickname per la Leaderboard")
               nome_punteggio=NicknamePunteggio(nome_giocatore,livello_attuale-1)
               giocatore_trovato = 0
               for p in punteggi:
                   if p.nickname==nome_giocatore:
                       p.punteggio=livello_attuale-1
                       giocatore_trovato=1
                       punteggi = sorted(punteggi, key=lambda NicknamePunteggio: NicknamePunteggio.punteggio,
                                         reverse=True)
               if giocatore_trovato == 0:
                   punteggi.append(NicknamePunteggio(nome_giocatore, livello_attuale-1))
                   punteggi = sorted(punteggi, key=lambda punteggio: punteggio,reverse=True)
                   for p in punteggi:
                       if p.punteggio == -1:
                           p.punteggio = 0
               f = open("punti.txt", "w")
               for x in punteggi:
                   f.write(f"{x.nickname} {x.punteggio}\n")
               f.close()
               return 0


           if q.livello == livello_attuale:
               risposte_shuffled=list(q.risposte)
               random.shuffle(risposte_shuffled)
               print(f"{q.domanda} (LIVELLO DOMANDA = {q.livello})\n")
               for i in risposte_shuffled:
                   print(f"{i}\n")
               val=int(input("Quale di queste è giusta (scrivi il numero corrispondente)?"))
               for r in risposte_shuffled:
                   if r.corretta==1:
                       x=risposte_shuffled.index(r)+1
                       if val==x:
                           "Passi al prossimo round"
                           livello_attuale+=1
                       else:
                           perdita=1
                           print("No, è sbagliata, HAI PERSO")
                           # agiorniamo e stampiamo la leaderboard nel file
                           nome_giocatore = input("Dimmi il tuo nickname per la Leaderboard")
                           nome_punteggio = NicknamePunteggio(nome_giocatore, livello_attuale-1)
                           giocatore_trovato = 0
                           for p in punteggi:
                               if p.nickname == nome_giocatore:
                                   p.punteggio = livello_attuale-1
                                   giocatore_trovato = 1
                                   punteggi = sorted(punteggi,
                                                     key=lambda NicknamePunteggio: NicknamePunteggio.punteggio,
                                                     reverse=True)
                           if giocatore_trovato == 0:
                               punteggi.append(NicknamePunteggio(nome_giocatore, livello_attuale-1))
                               punteggi = sorted(punteggi, key=lambda NicknamePunteggio: NicknamePunteggio.punteggio, reverse=True)
                           for p in punteggi:
                               if p.punteggio==-1:
                                   p.punteggio=0
                           f = open("punti.txt", "w")
                           for x in punteggi:
                               f.write(f"{x.nickname} {x.punteggio}\n")
                           f.close()

                           return 0
















   # adesso ho nel vettore question tutti gli oggetti di tipo domanda con i loro attributi corretti
'''DA CANCELLARE (consigli su come proseguire)
PER ADESSO: abbiamo la lista question con tutte le domande da proporre
Dobbiamo ancora fare alcune cose
0)implementare il meccanismo di vincita o perdita del gioco (insieme alla 3)
1)implementare la possibilità di randomizzare le 3 risposte ad ogni domanda tenendo traccia di quale sia quella giusta
2)implementare la possibilità di randomizzare le domande per ogni livello di difficotà in modo che non escano in
ordine sempre le stesse domande
3)implementare i punteggi con il nickname relativo, e quindi chiedere il nick che ci servirà per salvare i punteggi
nel file punti.txt (ps visto che si esce quando si sbaglia e si guadagna un punto per ogni domanda giusta
basta guardare a che livello di difficoltà è arrivato il tipo quando finisce il programma, o perchè ha sbagliato o
perchè ha vinto)
4)stampare i punteggi nel file punti.txt'''

main()