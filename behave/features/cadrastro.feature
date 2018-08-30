# language: pt

Funcionalidade: Cadrastrar revista no estoque

Contexto: Usuário irá cadrastrar a revista no estoque

    Cenário: O internauta quer cadrastrar a revista em estoque 
        Dado que estou no caminho file:///home/josias/Documentos/revistas/web-app/cadastrarRevista.html
        Quando coloco "859585855" no campo "codigo"
             E coloco "Dragon Ball super" no campo "titulo"
             E coloco "859585855" no campo "codigo"
             E coloco "30" no campo "paginas" 
             E coloco "2018-08-2" no campo "data"
             E coloco "10" no campo "quantidade"
        Então clico no botao cadrastrar 

    Cenário: O internauta quer verificar a revista cadrastrada
    Dado que estou no caminho file:///home/josias/Documentos/revistas/web-app/index.html
        Então devo visualizar o texto "859585855"
            E devo visualizar o texto "Dragon Ball super"
            E devo visualizar o texto "30"
            E devo visualizar o texto "2018-08-2"
            E devo visualizar o texto "10"