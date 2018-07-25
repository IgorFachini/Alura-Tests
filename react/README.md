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

React recomenda inicializar dados, buscar, em metodos do ciclo de vida do react Ex: componentWillMount -> chamado antes de montar  o componente.
para que a mudanca de estado seja notada, deve mudar o estado da variavel com this.setState, isso resultara na chamada de render() novamente.

Agora, render nao renderiza tudo novamente, o HTML sempre sera convertido em React Elements, e aconselha que os elementos do HTML tenha id unicos, assim
o react pode saber o que de fato mudou para mudar apenas aquele elemento do DOM.

componentWillMount vs componentDidMount = Will sempre sera chamado quando state mudar, Did so sera chamado uma vez.



export default App {
export = acessar externalmente
default = o nome padrao, se nao tiver, temque usar {(nome)} pra chamar algo especifico.
App = nome do modulo classe.
}
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
---  return <Square value={i} />;

construtores de classe devem ter super
  constructor(props) {
    super(props);
  }
