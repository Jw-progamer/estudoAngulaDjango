var app = angular.module("FormularioRevistas",[]);
app.controller("ControladorFormulario", function($scope, $http) {
    $scope.revista = {codigo: '',titulo: '', pagina: '', publicacao: '', qtde: ''};
    $scope.cadrastrar = function(){
        ano  = $scope.revista.publicacao.getFullYear();
        mes  = $scope.revista.publicacao.getMonth();
        dia  = $scope.revista.publicacao.getDate();
        $scope.revista.publicacao = ano + "-" + mes + "-" + dia;
        $http.post('http://localhost:8000/api/revista/',$scope.revista).then(
        function(response){
            console.log('Foi sucesso')   ;
            console.log(response);
           }
        )
    }
})