var http = require('http')
var console = require('console')
var config = require('config')

module.exports.function = function createUser (survey, $vivContext) {
  /*
  //JSON.stringify($vivContext, undefined, 1);
  //String bixbyUserId = $vivContext.bixbyUserId
  userID = JSON.stringify($vivContext.bixbyUserId, undefined, 1);

  return {
    userID : userID,
    gender: survey.gender,
    age: survey.age,
  };
  */
  var user = {
    "gender": survey.gender,
    "age": survey.age,
    "userID" : $vivContext.bixbyUserId,
  };
  var options = {
    passAsJson: true,
    returnHeaders: true,
    format: 'json',
  };
  //var response = http.postUrl(config.get('remote.url') + '/user', user, options);
  
  var response = http.postUrl('http://www.bixbar.com/user', user, options);
  console.log("response : " + response);
  console.log("response.parsed : " + response.parsed)
  return user//response.parsed;
}