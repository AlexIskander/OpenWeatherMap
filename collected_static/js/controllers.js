(function () {
    var app = angular.module('myApp', []);
    app.controller('HelloController',
        function ($scope) {
            $scope.greeting = {text: 'Hello Iskander'};
        });

    app.controller('TextController',
        function ($scope) {
            var someText = {};
            someText.message = 'You have started your journey.';
            $scope.someText = someText;
        });


    app.controller('graphController', function ($scope) {

        $scope.width = 600;
        $scope.height = 400;
        $scope.yAxis = "Sales";
        $scope.xAxis = "2014";

$scope.data = [
  {
    label: 'January',
    value: 36
  },
    {
    label: 'February',
    value: 54
  },

    {
    label: 'November',
    value: 252
  },
  {
    label: 'December',
    value: 342
  }

]

        $scope.max = 0;

var arrLength = $scope.data.length;
for (var i = 0; i < arrLength; i++) {
  // Найти максимальное значение на оси X
  if ($scope.data[i].value > $scope.max)
  $scope.max = $scope.data[i].value;
}


    });


})();

