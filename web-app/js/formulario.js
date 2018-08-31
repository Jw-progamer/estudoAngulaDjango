var app = angular.module("FormularioRevistas",[]);
app.controller("ControladorFormulario", function($scope, $http, $window) {
    $scope.revista = {codigo: '',titulo: '', pagina: '', publicacao: '', qtde: ''};
    $scope.cadrastrar = function(){
        ano  = $scope.revista.publicacao.getFullYear();
        mes  = $scope.revista.publicacao.getMonth()+1;
        console.log(mes);
        dia  = $scope.revista.publicacao.getDate();
        $scope.revista.publicacao = ano + "-" + mes + "-" + dia;
        $http.post('http://localhost:8000/api/revista/',$scope.revista).then(
        function(response){
            console.log(response);
            $window.location.href = 'file:///home/josias/Documentos/revistas/web-app/index.html';
           }
        )
    }
})