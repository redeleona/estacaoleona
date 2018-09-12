'use strict';

angular.module('myApp.view1', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/view1', {
    templateUrl: 'view1/view1.html',
    controller: 'View1Ctrl',
    controllerAs: 'vm'
  });
}])
.controller('View1Ctrl', ['$scope','$document',function($scope,$document) {

  var vm = this;

  //vm.ip_address = '150.163.55.230';
  vm.ip_address = '10.163.16.50';
  vm.ativo = false;

  vm.controlbox_socket = new WebSocket('ws://'+ vm.ip_address+ '/beta1/controlbox');
  //vm.controlbox_socket = new WebSocket('ws://10.163.16.7/beta1/controlbox');

  vm.controlbox_socket.onmessage = function(evt) {
      var ctr = angular.fromJson(evt.data);
      $scope.az = parseInt(ctr.azimute);
      $scope.el = parseInt(ctr.elevacao);
      $scope.control_record = ctr.gravar;
      $scope.control_camera = ctr.camera;
      console.info(evt.data);

      $scope.$apply();
  };

  vm.controlbox_socket.onerror = function(evt) {
        console.info('an error occurred: ' + evt);
    };

    vm.controlbox_socket.onopen = function(evt) {
        console.info('Connection established');
    };

    vm.controlbox_socket.onclose = function() {
        console.info('Connection closed');
        window.setTimeout(attemptConnection, 1000);
    };
    vm.left = function(i) {
        if($scope.az > 0) $scope.az-=i;
        vm.azimute($scope.az);
    };
    vm.right = function(i) {
        //$scope.az+=i ANA ADD
        if($scope.az < 350) $scope.az +=i;
        vm.azimute($scope.az);
    };
    vm.down = function(i) {
        //$scope.el-=i ANA ADD
        if($scope.el > -35) $scope.el -=i;
        vm.elevacao($scope.el);
    };
    vm.up = function(i) {
       // $scope.el+=i ANA ADD
        if($scope.el < 35) $scope.el +=i;
        vm.elevacao($scope.el);
    };

    vm.elevacao = function (i) {
        //$scope.el = i;
        vm.controlbox_socket.send('{"elevacao":"'+$scope.el+'"}');
    }

    vm.azimute = function (i) {
        //$scope.az = i;
        vm.controlbox_socket.send('{"azimute":"'+$scope.az+'"}');
    }

    //ANA add
    vm.rec = function(i) {
        $scope.record = i

        if(i==='True' &&  $scope.control_record === 'gravando' || i==='True' && $scope.control_record === 'Gravação já Iniciada') $scope.control_record = 'Gravação já Iniciada'

        else
            vm.controlbox_socket.send('{"gravar":"'+$scope.record+'"}')
    };

    //ANA add
    vm.ctz_camera = function(i) {
        $scope.cam = i
        vm.controlbox_socket.send('{"camera":"'+$scope.cam+'"}')
    }

  //vm.socket = new WebSocket('ws://10.163.16.51/sjc1/ws');
  vm.socket = new WebSocket('ws://'+ vm.ip_address+'/sjc1/ws');
  
  vm.socket.onmessage = function(evt) {
    document.getElementById('main').innerHTML = evt.data;
  };

  vm.socket.onerror = function(evt) {
    console.info('an error occurred: ' + evt);
  };

  vm.socket.onopen = function(evt) {
    console.info('Connection established');

  };

  vm.socket.onclose = function() {
      console.info('Connection closed');
      //document.getElementById('main').innerHTML = '<img src="/static/stand-by.jpg" alt="">';
      document.getElementById('main').innerHTML = 'Serviço Indisponível';
      window.setTimeout(attemptConnection, 1000);
  };

  //vm.socket1 = new WebSocket('ws://'+vm.ip_address+'/cam_beta_1');
    vm.socket1 = new WebSocket('ws://'+ vm.ip_address+'/sjc2/ws');
	
    vm.socket1.onmessage = function(evt) {
        document.getElementById('main1').innerHTML = evt.data;
    };

    vm.socket1.onerror = function(evt) {
        console.info('an error occurred: ' + evt);
    };

    vm.socket1.onopen = function(evt) {
        console.info('Connection established');
    };

    vm.socket1.onclose = function() {
        console.info('Connection closed');
        document.getElementById('main1').innerHTML = '<img src="/static/stand-by.jpg" alt="">';
        window.setTimeout(attemptConnection, 1000);
    };

    $document.bind('keydown', function (evt) {
        if(vm.ativo) {
            console.info(evt);
            if(evt.keyCode === 39) {
                vm.right(1);
            }

            if(evt.keyCode === 37) {
                vm.left(1);
            }

            if(evt.keyCode === 40) {
                vm.down(1);
            }

            if(evt.keyCode === 38) {
                vm.up(1);
            }
            evt.stopPropagation();
        }
    })

}]);