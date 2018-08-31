# language: pt

Funcionalidade: Cadrastrar revista no estoque

Contexto: Usuário irá cadrastrar a revista no estoque

    Cenário: O internauta quer cadrastrar a revista em estoque 
        Dado que estou no caminho file:///home/josias/Documentos/revistas/web-app/cadastrarRevista.html
        Quando coloco "400000" no campo "codigo"
             E coloco "Super Mario-kun" no campo "titulo"
             E coloco "20" no campo "paginas" 
             E coloco "2017-07-02" no campo "data"
             E coloco "9" no campo "quantidade"
        Então clico no botao cadrastrar 

    Cenário: O internauta quer verificar a revista cadrastrada
    Dado que estou no caminho file:///home/josias/Documentos/revistas/web-app/index.html
        Então devo visualizar o texto "400000"
            E devo visualizar o texto "Super Mario-kun"
            E devo visualizar o texto "20"
            E devo visualizar o texto "2017-07-02"
            E devo visualizar o texto "9"