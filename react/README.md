# Anotacoes de aprendizado.

O React é uma biblioteca JavaScript declarativa, eficiente e flexível para criar interfaces com o usuário. Ele permite compor interfaces de usuário complexas a partir de pequenos e isolados códigos chamados “componentes”.

Usa JSX - Permite usar marcacao XML(html) dentro do javascript.
Babel - converte uma fonte javascript para outra fonte. (no projeto o que foi convertido roda no nodejs).
webpack - converte tudo que nao seja suportado no navegador para um codigo javascript suportado. arquvio gerado = bundle.js

class = classe.
className = estilo css.
render = retorna um elemento React.
props = acessa valores das subtags

variavel state = react disponibiliza, ela fica sendo observada, ataulizada etc..

React recomenda inicializar dados, buscar, em metodos do ciclo de vida do react Ex: componentWillMount -> chamado antes de montar o componente.
para que a mudanca de estado seja notada, deve mudar o estado da variavel com this.setState, isso resultara na chamada de render() novamente.

Agora, render nao renderiza tudo novamente, o HTML sempre sera convertido em React Elements, e aconselha que os elementos do HTML tenha id unicos, assim
o react pode saber o que de fato mudou para mudar apenas aquele elemento do DOM.

componentWillMount vs componentDidMount = Will sempre sera chamado quando state mudar, Did so sera chamado uma vez.

export default App {
export = acessar externalmente
default = o nome padrao, se nao tiver, temque usar {(nome)} pra chamar algo especifico.
App = nome do modulo classe.
}
alem de classes, da pra exportar funcoes, para chamar, usar new nome().funcao()
ex:
class Square extends React.Component {
constructor(){
super(); // deve ser chamado sempre por primeiro
}
render() {
return (
<button className="square">
{this.props.value}
</button>
);
}
}
--- return <Square value={i} />;

construtores de classe devem ter super
constructor(props) {
super(props);
}

NUNCA no render returnar mais de um elemento exemplo
return (

  <div></div>
  <div></div>
);
JSX espera um PAI ou seja.
return (
  <div>
    <div></div>
    <div></div>
  </div>
);
-----------------------

Biblioteca que funciona tanto para JavaScript Client-side quanto para Server-side: o PubSubJS.
chamamos de publisher, quem publica o aviso, e de subscriber quem se inscreve para recebe-lo.
npm install pubsub-js
EX:
PubSub.publish('atualiza-lista-autores',novaListagem);
PubSub.subscribe('atualiza-lista-autores', function(topico,novaLista){
});

---

High Order Components, quando ter varios componentes e eles acessam o mesmo estado, cria-se um component pai que guarda o estado,
e seus filhos separados que sao importados para ele, podem ver o mesmo estado.

---

Roteamento, react nao tem suporte para rotas. Deve-se instalar o React Router.
Ex:
import {Router,Route,browserHistory, IndexRoute } from 'react-router';

(<Router history={browserHistory}>
<Route path="/" component={App}>
<IndexRoute component={Home}/>
<Route path="/autor"/>
<Route path="/livro"/>
</Route>
</Router>),

se nao indicarmos o nome da url, o router ira gerar.
para ele deixar com o nome que esta em path, deve importar e usar browserHistory.
Para que outras paginas sejam inseridas em outra, deve-se colocar dentro da rota Route.
do outro lado da rota "pai", os filhos acessados sao passados como paramentros e podem ser
recuperados com {this.props.children}.

IndexRoute - caso nenhum filho seja chamado, ele sera passado como padrao para Route pai.

para navegacao, se usar <a>, ele ira fazer uma requisicao, para apenas renderizar, devemos usar
Link do Router.
Ex:
import {Link} from 'react-router';

<li className="pure-menu-item"><Link to="#" className="pure-menu-link">Home</Link></li>

---

select, ele já será suportado pelo React para o Check box ou radio button, ao ter a propriedade value - no HTML normal, não tem o value para o select, ele seria apenas para as options.

O value no selection e ele automaticamente, escolhe a option correta. Esta é uma facilidade que o React nos oferece.
Ex:
<select value={this.state.autorId} name="autorId" id="autorID" onChange={this.setAutorId}

---

caso o nome das propriedades de state seja o mesmo das propriedade do elemento HTML.
podemos usar spread operator
Ex:
<input id={this.props.id} type={this.props.type} name={this.props.name} value/>
para
<input {...this.props}/>
