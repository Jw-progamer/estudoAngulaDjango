var app = angular.module("Revistas",[]);
app.controller("ControladorRevistas", function($scope, $http) {
    $http.get("http://localhost:8000/api/revista/").then(function(response){
        $scope.revistas = response.data;
    })
})
