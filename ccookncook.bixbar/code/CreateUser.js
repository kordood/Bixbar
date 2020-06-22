var http = require('http')
var console = require('console')
var config = require('config')

module.exports.function = function createUser (survey, $vivContext) {

  var user;
  if(survey.gender == "Male"){
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
    format: 'json'
  };

  let url = "http://www.bixbar.com/user";

  var response = http.postUrl(url, user, options);

  console.log(response);
  return user;
}
