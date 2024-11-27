import sqlite3

conn = sqlite3.connect('utilizadores.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS utilizadores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    altura REAL NOT NULL,
    peso REAL NOT NULL
)
''')
conn.commit()

def registrar_usuario():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura (em metros): "))
    peso = float(input("Digite o peso (em kg): "))
    
    cursor.execute("INSERT INTO utilizadores (nome, idade, altura, peso) VALUES (?, ?, ?, ?)", 
                   (nome, idade, altura, peso))
    conn.commit()
    print(f"Utilizador registrado com sucesso!")

def calcular_imc():
    nome = input("Digite o nome do utilizador de que deseja saber o valor do IMC: ")
    cursor.execute("SELECT altura, peso FROM utilizadores WHERE nome = ?", (nome,))
    resultado = cursor.fetchone()
    
    if resultado:
        altura, peso = resultado
        imc = peso / (altura ** 2)
        print(f"O IMC de {nome} é: {imc:.2f}")

        with open(f"IMC_{nome}.txt", "w") as arquivo:
            arquivo.write(f"O IMC do/da {nome} é: {imc:.2f}")
        print(f"Arquivo 'IMC_{nome}.txt' gerado com sucesso!")
    else:
        print(f"Utilizador {nome} não encontrado.")

def menu():
    while True:
        print("\n1. Registrar utilizador")
        print("2. Consultar e calcular IMC")
        print("3. Sair")
        
        escolha = int(input("Escolha uma opção: "))
        
        match escolha:
            case 1:
                registrar_usuario()
            case 2:
                calcular_imc()
            case 3:
                print("Saindo do programa.")
                break
            case _:
                print("Opção inválida. Tente novamente.")

menu()

conn.close()
