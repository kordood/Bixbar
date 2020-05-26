var http = require('http')
var console = require('console')
var config = require('config')

module.exports.function = function createUser () {
  var user = {
    "gender": "femail",
    "age": "23",
    "userId" : "testID",//$vivContext.bixbyUserId,
  };
  var options = {
    passAsJson: true,
    returnHeaders: true,
    format: 'json'
  };
  var response = http.postUrl(config.get('remote.url') + '/user', user, options);

  console.log(response);
  return response.parsed;
}
