var http = require('http')
var console = require('console')
var config = require('config')

module.exports.function = function personalize ($vivContext) {
  
  user = {
    "userID" : $vivContext.bixbyUserId,
    };

  var options = {
    passAsJson: true,
    returnHeaders: true,
    format: 'json'
  };

  let url = "http://www.bixbar.com/recommend/";

  var response = http.postUrl(url, user, options);
  console.log("response");
  console.log(response);
  return response.parsed;
}
