# language: pt

Funcionalidade: Cadrastrar revista no estoque

Contexto: Usuário irá cadrastrar a revista no estoque

    Cenário: O internauta quer cadrastrar uma revista em estoque 
        Dado que estou no caminho file:///home/josias/Documentos/revistas/web-app/cadastrarRevista.html
        Quando digito os campos referentes a revista
        Então clico no botao cadrastrar 

    # Cenário: O internauta quer verificar a revista cadrastrada
    # Dado que estou no caminho file:///home/josias/Documentos/revistas/web-app/index.html
    #     Então devo visualizar o texto "30000"
    #         E devo visualizar o texto "Ligua da justica"
    #         E devo visualizar o texto "50"
    #         E devo visualizar o texto "2018-07-02"
    #         E devo visualizar o texto "15"