Relacionado ao Android Studio


pasta sampleData = simular dados, com json, no layout buscar com tools - @samples/.

-- Codigo

AppCompat = Suport a APIs antigas.


-- Layout

ConstaintLayout: Uma API que permite criar layouts do Android de maneira similar ao RelativeLayout,
RelativeLayout Precisa de hierarquia, ConstaintLayout nao. A posicao de seus filhos na arvore de views, define quem vai ficar em cima de quem.
layout_constraint = definir aonde que eu vou 'grudar', para grudar em outros views, ha necessidades que elas tem ID proprios.
Bias = relacao em % de pocionamento em ralacao a x e y, so funciona se os dois lados de x ou y estiverem conectados.


wrap_content - crescer o sufiente.
match_parent - crescer de acordo com o tamanho do pai(hierarquia).
match_constraint - crescer ate o definido(grudado).
tools:... - simula componentes, so aparece na view do DEV.