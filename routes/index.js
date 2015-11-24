/* GET home page. */
exports.index = function(req, res){
  res.render('index', { title: 'Express' });
};

exports.post_api = function (req, res){
    var fs = require('fs');

    debugger;

    // multipart input field is "input_file" keywork
    fs.readFile(req.files.input_file.path, function (err, data){
        if (!err) {
            var content = data.toString('utf-8');
            console.log('Recv from Client: ', content);
            res.render('index', { title: content+' from POST' });
        }
        else {
            content = 'err';
            console.error('Some error from Request!');
            res.render('index', { title: content+' from POST' });
        }
    });
}