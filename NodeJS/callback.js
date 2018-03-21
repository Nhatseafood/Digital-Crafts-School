

// function add(x, y) {
//     var result = x + y;
//     return result;
//   }

function add (x,y, callback) {
    var result = x + y;
    callback(result);
}
add(1,2, function (result) {console.log(result)});

// function subtract(x, y) {
//     return x - y;
//   }

function subtract (x, y, callback) {
    var result = x - y;
    callback(result);
}
subtract(2,3, function (result) {console.log(result)});

// function greeting(person) {
//     return 'Hola, ' + person + '!';
//   }


function greeting(person, callback) {
    var name = person;
    callback(name);
}
greeting('Nhat', function (name) {console.log(`Hello ${name}!`)});
greeting('Nhat', function (name) {console.log('Hola, ' + name + '!')});

// function product(numbers) {
//     return numbers.reduce(function(a, b) {
//       return a * b;
//     }, 1);
//   }

function product(numbers, callback) {
    var result = numbers.reduce(function(a,b) {
        return a*b
    },1);
    callback(result);

    
}
product([2,4], function (result) {console.log(result)})