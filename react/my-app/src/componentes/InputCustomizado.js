import React, { Component } from 'react'; // JSX exige que nome do mudulo importa de react seja chamado de REACT.

// deve ser exportado para ser enxergado.
export default class InputCustomizado extends Component{
	//propriedades do component sao acessadas com prop herdado de Component
	render() {
		return (
			<div className="pure-control-group">
			  <label htmlFor={this.props.id}>{this.props.label}</label> 
			  <input id={this.props.id} type={this.props.type} name={this.props.name} value={this.props.value}  onChange={this.props.onChange}/>                  
			</div>			
		);
	}
}
