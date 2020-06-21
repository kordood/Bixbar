module.exports.function = function personalClick ($vivContext, perResults) {

  const console = require('console');
  const fail = require("fail");
  var http = require("http");
  var config = require('config');  
  
  console.log(perResults);
  console.log(typeof(perResults));

  title = String(perResults.title);
  
  if(title.indexOf("(") != -1){
    
    var cocktailNameArray = title.split("(");
    
    title = cocktailNameArray[0];

  }
  
  console.log("name of cocktail : " + title);
  user = {
    "userID" : $vivContext.bixbyUserId,
    "itemName" : title
  };

  var options = {
    passAsJson: true,
    returnHeaders: true,
    format: 'json'
  };

  let url = "http://www.bixbar.com/choose/";

  var response = http.postUrl(url, user, options);

  console.log(response);
  return perResults;
}
