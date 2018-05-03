phython -3
https://www.python.org/

editor pra python PyCharm
executar phyton sem programas https://repl.it/
com path refenciado 
executa com comando python, inicia console do python,
comandos chama-se como funcao()


print("ola") - printa
aceita funcoes
ex: 
print("Brasil", "ganhou", 5, "titulos mundiais", sep="-")
Brasil-ganhou-5-titulos mundiais

variavel: //nao precisa declarar tipo, padrao Snake_Case = idade_esposa = 20
pais = "Italia"

type(pais): //retorna o tipo
<clas 'str>

funcoes,ifs, while ... = //é utilizado dois pontos (:), e esse bloco obrigatoriamente deve estar 4 espaços (ou um TAB) mais à direita, voltar espacos para esquerda termina funcao,


chute = input("Digite o seu número: "): //espera digitar algo, devolve uma string do digitado

if (condição):
    //executa código caso a condição seja verdadeira
else:
    //executa código caso a condição seja falsa
elif (chute < numero_secreto):
    //else com condicao de entrada

int("12"): // converte string para int
int(18.895629671768187): = 18 // fazer cast

while (total_de_tentativas > 0): //laço com base na condicao verdadeira
        total_de_tentativas = total_de_tentativas - 1

for rodada in range(1,10): //laco de inicio e fim, imprimi 1 a 9
    print(rodada)

for rodada in range(1,10,2):// com step, pulos
for rodada in [1,2,3,4,5]: // passando manualmente sem range
 
print("Tentativa {} de {}".format(rodada, total_de_tentativas))
//As chaves significam que o Python deve substituí-las pelos valores das variáveis, deixar vazio fara na sequencia,
se colocar numero, fara na sequencia dos numeros, e se colocar regras como {:.2f}, ira aplicalas

if (chute < 1 or chute > 100): // OR, OU condicao

continue // no caso do for, while, sem sair do laço continua para a proxima iterecao

import random
random.random() // gera um número no intervalo entre 0.0 e 1.0, por EX: 0.6022965518496559
random.randrange(1, 101)// gera numero aleatorio no range defindo

abs(-10) = 10// retorna o valor absoluto

import forca // imorta a classe forca.py

funcao //
def jogar():
    blabla      
    blabla  // define funcao com def

chamando funcao
jogar() // direto
forca.jogar // de outra classe

if (__name__ == "__main__"): //  __name__, e ela é preenchida com o valor __main__ caso o arquivo seja executado diretamente.
