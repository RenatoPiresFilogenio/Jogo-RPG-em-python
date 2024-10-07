from random import randint
import random
lista_Monstro = []
playerStatus = []
def npc_monstro():
    nivel = randint(3,8)
    Monstro = {
        "monstro": nivel,
        "hp": 15 * nivel,
        "dano": 10 * nivel,}
    lista_Monstro.append(Monstro.copy())

def Monstro_Gerador(n_npc):
    for i in range(n_npc):
        npc_monstro()


def UP(a,b):
    if player["abates"] > player["abates-atual"]:
        player["nivel"] += 1
        print("o heroi subiu de nivel!!!")
        player["abates-atual"] += 1
        player["hp"] += 100
        player["dano"] += 10
        player["defesa"] += 5
        print("agora os status do herói são")
        print(f"o heroi bob tem {player["hp"]} de vida e {player["dano"]} de dano com sua defesa de {player["defesa"]}")
        return
def CBT(HPM=0,HPJ=0):

    print(f"BOB ira enfrentar o monstro{HPM["monstro"]}")
    print("1 - para atacar")
    print("2 - para se defender")

    Option = int(input("escolha sua próxima ação"))
    while True:
        if Option == 1:
            print("você selecionou atacar")
            HPM["hp"] -= HPJ["dano"]
            print(f"você deu {HPJ["dano"]} de dano, o monstro está com {HPM["hp"]} de vida")

            if HPM["hp"] <= 0:
                print("O monstro morreu")
                HPJ["abates"] += 1

                UP(a = HPJ["abates"], b = HPJ["abates-atual"])
                break



            HPJ["hp"] -= HPM["dano"]
            HPJ["hp"] += HPJ["defesa"]

            if HPJ["hp"] <= 0:
                print("O Heroi morreu")
                break
            print(f"Após seu ataque o Monstro lhe ataca e você fica com {HPJ["hp"]}")
            Option = int(input("escolha sua próxima ação"))

        elif Option == 2:
            print("voce decidiu se defender")
            Numero_Para_Defesa = randint(0,100)
            if Numero_Para_Defesa >= 50:

                print("BOB conseguiu se preparar para o próxima ataque e ganha 5 de dano")
                HPJ["dano"] += 5


                HPJ["hp"] -= HPM["dano"]
                HPJ["hp"] += HPJ["defesa"]

                if HPJ["hp"] <= 0:
                    print("O Heroi morreu")
                    break

                print(f"BOB recebe {HPM["dano"]} de dano, mas sua armadura impede {HPJ["defesa"]} ficando com {HPJ["hp"]}")

                Option = int(input("escolha sua próxima ação"))
            else:
                print("BOB se atrapalha e tropeça, perdendo 5 de defesa")
                HPJ["defesa"] -= 5

                HPJ["hp"] -= HPM["dano"]
                HPJ["hp"] += HPJ["defesa"]
                print(f"BOB recebe {HPM["dano"]} de dano, mas sua armadura impede {HPJ["defesa"]} ficando com {HPJ["hp"]}")
                if HPJ["hp"] <= 0:

                    print("O Heroi morreu")
                    break

                print(f"BOB recebe {HPM["dano"]} de dano, mas sua armadura impede {HPJ["defesa"]} ficando com {HPJ["hp"]}")
                Option = int(input("escolha sua próxima ação"))
        else:
            print("opção invalida")
            Option = int(input("escolha sua próxima ação"))



genMonstro = randint(0,10)
Monstro_Gerador(genMonstro)
npc_monstro()

#PLAYER STATUS#################
player ={
        "nome":"bob",
        "nivel":1,
        "hp":100,
        "dano":15,
        "defesa":10,
        "abates-atual":0,
        "abates":0,}


playerStatus.append(player.copy())

for n in playerStatus:
    print(f"o heroi bob tem {n["hp"]} de vida e {n["dano"]} de dano com sua defesa de {n["defesa"]}")
playerStatus = player
CBT(HPM = random.choice(lista_Monstro),HPJ = player)



#####################

