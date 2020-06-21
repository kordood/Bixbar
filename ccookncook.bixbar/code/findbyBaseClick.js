module.exports.function = function findbyBaseClick (title) {
    const console = require('console');
  const fail = require("fail");
  var http = require("http");
  var config = require('config');
  console.log("name of cocktail : " + title);
  
  console.log(typeof title);
  title = String(title);
  console.log(typeof title);

  if(title.indexOf("(") != -1){
    console.log(typeof title);
    
    var cocktailNameArray = title.split("(");
    
    title = cocktailNameArray[0];

  }
  
  console.log("name of cocktail : " + title);

  var response = null;
   
  const baseURL = "http://www.bixbar.com/cocktail/?q=";
 
  if(title.length == 0){
    throw fail.checkedError("No Result", "NoResult");
  }  
  else{
    
    let url = baseURL + title; //http://bixbar.run.goorm.io/cocktail/?q=DirtyMartini
   
    let options = {
      format : 'json',
      
    };

    //return type : json
    response = http.getUrl(url, options);
    
    console.log(response);

    
    if(response.status == 404 ){
 
      throw fail.checkedError("No Result", "404 error");  

    }
    
  }

  return response;
}
