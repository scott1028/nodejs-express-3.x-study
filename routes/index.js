/* GET home page. */
exports.index = function(req, res){
  res.render('index', { title: 'Express' });
};

exports.post_api = function (req, res){
    var fs=require('fs');

    // multipart input field is "input_file" keywork
    fs.readFile(req.files.input_file.path, function (err, data){
        if (!err) {
            var content=data.toString('utf-8');
            res.render('index', { title: content+' from POST' });
        }
        else {
            content='err';
            res.render('index', { title: content+' from POST' });

        }
    });
}