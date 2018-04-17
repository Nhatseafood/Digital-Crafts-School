module.export = (sequelize, DataType) => {
    var post = sequelize.define('posts', {
        title: DataType.STRING,
        body: DataType.STRING
    },{});
    Comment.associate
    }