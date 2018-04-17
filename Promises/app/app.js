var express = require('express');
var app = express();
require('any-promise/register/bluebird');
var promise = require('bluebird');
var rp = require('request-promise');
const bodyParser = require('body-parser');
var cheerio  = require('cheerio');
var fs = require('mz/fs');


app.set('view engine', 'ejs');
app.set('views', 'app/views');

app.use(bodyParser.urlencoded({extended :false}))

// defined the options for the pg-promise library
var options = {
    promiseLib : promise
  }
  
  // configuring the pg-promise database connection
var pgp = require('pg-promise')(options);
var connectionString = 'postgres://localhost:5432/nadiasgarden';
var db = pgp(connectionString);

app.use(express.static('app/public'));




var websites1 = rp('https://en.wikipedia.org/wiki/Futures_and_promises')
var websites2 = rp('https://en.wikipedia.org/wiki/Continuation-passing_style')
var websites3 = rp('https://en.wikipedia.org/wiki/JavaScript')
var websites4 = rp('https://en.wikipedia.org/wiki/Node.js')
var websites5 = rp('https://en.wikipedia.org/wiki/Google_Chrome')


 
// Promise.all([websites1, websites2, websites3, websites4, websites5])
// .then(function (htmlString) {
//           //process html..
//           console.log(htmlString, "this is my first req ------------------------>");
//       })
//       .catch(function (error){
//           //crawling failed..
//       });

// function saveWebSite (url,filename) {
//    rp(url)
//    .then(function (htmlString) {
//        console.log("it works") 
//        fs.writeFile(filename, htmlString, (err) => {
//         if (err) throw err;
//         console.log('The file has been saved!');
//        })
//    })
//    .catch(function (err) {
//        console.log(err)

//    })
   
// };
// saveWebSite('https://en.wikipedia.org/wiki/Google_Chrome', "Google");

// function cat2Files (filename1,filename2, output) {
    

//     fs.readFile("views/" + filename1,  (err, data) => {
//         if (err) throw err;
//         console.log('The file has been read!');
//         fs.appendFile(output, data, (err) => {
//             if (err) throw err;
//             console.log('The file has been saved!' + data);
//         })
//     });

//     fs.readFile("views/" + filename2, (err, data) => {
//         if (err) throw err;
//         console.log('The 2nd file has been read!');
//         fs.appendFile(output, data, (err) => {
//             if (err) throw err;
//             console.log('The 2nd file has been saved!' + data);
//         })
//     });
 
// };   
// cat2Files('testSite1', 'testSite2', 'yahooandgoogle');


function addNumbers(x,y) {
    var answer = x + y;
    // var p =
    return new Promise(function (resolve, reject){
        if(Number.isInteger(answer)){
        resolve(answer);
        }else{
            reject('error');
        }
    });
    //     p.then(function (answer) { 
    //     console.log('Done:' ,answer);
    // });
    //     p.catch(function (error) {
    //     reject(':('); 
    //     console.log(error);
    // });
}

    
  addNumbers(2,5)
    .then(ans => console.log(ans))
    .catch(err => console.log(err))
  addNumbers('the','dog').then(ans => console.log(ans)).catch(err => console.log(err))
   
    






var server = app.listen(2001, function(){
    console.log('Example app listening on port 2001 ');
});


