var express = require('express');

var router = express.Router();

router.get('/', function(req,res) {
    res.render('index', {
        pageTitle: 'Home',
        pageID: 'home'

    });

        
    

});
module.exports = router;




// router.get('/', function(req,res) {
//     res.send(

//         `
//         <link rel=stylesheet" type="text/css" href="css/style.css"
        
//         <h2> Welcome Digital Crafts </h2>
//         <p> Digital Crafts 16 weeks</p>
//         <img src=""/images/misc/background.jpg" style="height:300px;">
//         <script src="/reload/reload.js"></script>



        
//         `
//     ) 