bibliotecas
.h = header, cabecalho, definicoes
<> = do compilador
"" = local

stdio.h = entradas e saidas de texto.
stdlib.h = stander lib
time.h = data e hora



============
FILE* = arquivo
printf("imprimi na tela %d", variavel), % = mascara, d= inteiro ,c char
scanf("%d",&variavel) = (o que vou ler, variavel que vai guardar)
& = indica o endereco de memoria, evita copiar

abs(numero negativo) =  converte para positivo
rand() = retorna um interio aleatorio / srand(tempo) = popula rand para gerar aleatorio.
(rand() % 3) = retorna um numero dentro de 3
time(0) = busca a data atual em segundos
tipo[] = array
char palavra[20] = arra para guardar uma palavra, nao existe string.
sprintf(variavel,"texo") = colocar o texto na variavel
%s = imprimi o texto por inteiro do array
\0 = usado em texto pra indicar que chego ao fim do texto
strlen(texto) = retorna o tamanho
fopen("arquivo",mascara(ler,escrever etc...)) = abre um arquivo, devolve um ponteiro, devolve 0 se nao achar {
    mascaras = r: leitura, +:escrita
}
fclose(FILE) = fecha o arquivo
fscanf(arquivo-> FILE,saida, variavel, ...) = le o arquivo sequencialmente, linhas = sequencia
fprintf(arquivo -> FILE,"mascara", variavel) = escreve no arquivo
fseek(FILE, posicao, SEEK_SET) = aponta para algum lugar do arquivo{
    SEEK_SET = relaciona para a primeira posicao do arquivo
}
exit(numero) = 0 indica sucesso, >0 indica alguma falha
malloc = memorry alocation == garente espaco na memoria
free(variavel) = libera a memoria
sizeof(variavel) = retorna a quantidade de bytes que o tipo de var precisa

struct nome {
    var n1;
    var n2;
} = conjunto de variaveis -> nome.n1 ...

typedef var nome novoNome = da um apelido ao tipo, ex: typedef struct mapa MAPA -> em vez struct de chama struct mapa m, faz MAPA m;

strcpy(char[], char[]) - copia ate achar o \o para outra char[] -> lib string.h


-> == atalho para acessar conteudos ponteiros struct, se nao tivesse usaria (*var).var


if(condicao)

for(int i = 1, i <3, i++) = loop condicional

while() = enquanto, verifica primeiro

do - while = enquanto, roda primeiro

void teste(int n) = funcao, recebe um numero, cria um novo endereco com o que recebe
void teste(int* n) = recebe a referencia de um numero(memoria): ex{
    printf("%d %d", (*n),n);
    numero, endereco da memoria
}

-
um array sao ponteiros que apontam pra primeira posicao



break; = quebra bloco de codigo.
continue; = em for, ignora as acoes abaixo e vai pra proxima interacao.
#define = diretiva, constante, valor que nao muda.


BIT = numero de computador 0 ou 1
Bytes = colecao de BIT

1 byte = 8 bits = 256

