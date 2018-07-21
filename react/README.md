# Anotacoes de aprendizado.

O React é uma biblioteca JavaScript declarativa, eficiente e flexível para criar interfaces com o usuário. Ele permite compor interfaces de usuário complexas a partir de pequenos e isolados códigos chamados “componentes”.

render = retorna um elemento React.
props = acessa valores das subtags
ex: 
class Square extends React.Component {
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
