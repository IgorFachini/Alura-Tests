docker - vem com a ideia de "containers" que tem como funcao encapsular suas "aplicacoes", podendo ter N container na mesma SO, descartando a nescidade de configuracao de "ambiente" para a aplicacao.

Requisitos: Linux, ou Windows Pro, Enterprise, Education -> Docker CE for windows,
windows de outras versoes: -> docker ToolKit.

Depois de instalado: Windows: docker recomenda usar powershell por ser mais "poderoso".
No powershell testar: docker run hello-world

As imagens do docker, sao baixadas em camadas que representam o 'recurssos' da imagem.
cada imagem tem seu peso, isso facilita por exemplo na economia de peso futuro.
Por exemplo: baixo uma imagem do Ubunto e do CentOS, alguma camada que tem no ubunto o centOS tambem usa, entao ela nao vai baixar a mesma camada dinovo, mas s usar da outra imagem. As camada sao somente LEITURA, as escrita de arquivos dentro das imagems sao feitas em uma camada LEITURA/ESCRITA que foi crida em cima das de LEITURA. 

VOLUMES: Lugar aonde salva os dados.Linkar uma pasta da vm, com o desktop.

Rede default: 172.17.0.*

Load Balancer: Distribui as requisicoes de forma que nao sobrecarregue.

Docker Composer: Ajuda subir multiplos containers, seguindo o arquivo de config na extensao .yml.

--------------------------------------------------------------------------------------

Comandos:(docker) no comeco.

run (imagem) (parametros): (se nao tiver)baixa, cria e roda container.
-it= abre cli do container
-d= impede que imagen que ficam rodando travem o cli, deixa a imagem em bkg.
-P= atribua portas aleatorias do meu PC para poder acessar a imagem.
-p= voce define a porta.
--name= da um nome pro container
-e variavel="ola": cria ou escreve na variavl de ambiente.
-v "/var/www": cria um volume, sao representados por Mounts, "DIR PC:DIR VM"
-w "": define o diretorio pra execurta comandos
--network minha-rede = usa rede customizada



pull: baixa a imagem.

start (id): inicia o container ja criado.
-a = start com cli.

ps: lista os containers ativos.
-a = lista todos
-q = retorna apenas os ids.

rm (id): remove container
rmi (id,r): remove imagem

prune no final: limpa algo, por exemplo (container prune) remove  todos os containers.

images: lista imagems baixadas

port (id): ver porta da imagem que esta sendo usado.

docker-machine ip : para Versao ToolKit, moostra o ip da maquina virtual.

$(): tras o retorno dos comados executados. Ex de uso. docker stop $(docker ps -q)

inspect: mostra detalhes do container.

build (DIR): buildar dockerfile
-f = especifica nome
-t = nome da imagem

network: relacao a rede
create minha-rede= criar rede
--driver = tipo de drive por exemplo (bridge)
ls = lista as redes



ctrl D: exit

---------------
dockerfile

Ex:
FROM node:latest                = Tecnologia
MAINTAINER Igor Fachini         = Quem atualiza essa imagem.
ENV NODE_ENV=production         = variaveis de ambiente.
ENV PORT=3000
COPY . /var/www                 = Arquivos que ja estarao na imagem.
WORKDIR /var/www                = diretorio base que comeca o cli.
RUN npm install                 = quando a imagem estiver sendo construida executa esse comando.
ENTRYPOINT ["npm", "start"]     = comando que executa quando inicia a imagem.
EXPOSE $PORT                    = porta de acesso externa.

---------------------------
Publicando

docker login
docker push (imagem)