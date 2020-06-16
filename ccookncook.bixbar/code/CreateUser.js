var http = require('http')
var console = require('console')
var config = require('config')

module.exports.function = function createUser (survey, $vivContext) {

  var user;
  if(survey.isGender["isMale"] == true){
    user = {
    "gender": "Male",
    "age": survey.age,
    "userID" : $vivContext.bixbyUserId,
    };
  }  
  else{
    user = {
    "gender": "Female",
    "age": survey.age,
    "userID" : $vivContext.bixbyUserId,
    };
  }
  
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