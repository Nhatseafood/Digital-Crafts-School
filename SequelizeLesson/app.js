const sequelize = require('sequelize');
const sequelize = new sequelize('postgres://localhost.5432/seqClassdb');

var Article = connection.define('article',
{
    title: Sequelize.STRING,
    body: Sequelize.TEXT
});

connection.sync().then(function(){
    
}