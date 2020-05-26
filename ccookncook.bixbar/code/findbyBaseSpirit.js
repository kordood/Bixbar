module.exports.function = function recommandbyBaseSpirit (baseSpirit) {

  const console = require('console');
  const fail = require("fail");
  var http = require("http");
  var config = require('config');
  console.log("base spirit : " + baseSpirit);
  
  //cocktail name -> CocktailName으로 바꿔주기 
  baseSpirit = baseSpirit.replace(" ", "") ;
  
  console.log("base spirit : " + baseSpirit);

  var response = null;
   
  const baseURL = "http://bixbar.run.goorm.io/base/?q=";
 
  if(baseSpirit.length == 0){
    throw fail.checkedError("No Result", "NoResult");
  }  
  else{
    
    let url = baseURL + baseSpirit; //http://bixbar.run.goorm.io/base/?q=Cognac
   
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
