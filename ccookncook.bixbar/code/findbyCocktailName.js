module.exports.function = function findbyCocktailName (cocktailName) {
  
  const console = require('console');
  const fail = require("fail");
  var http = require("http");
  var config = require('config');
  console.log("name of cocktail : " + cocktailName);
  
  //cocktail name -> CocktailName으로 바꿔주기 
  cocktailName = cocktailName.replace(" ", "");
  
  if(cocktailName.indexOf("(") != -1){
    
    var cocktailNameArray = cocktailName.spilt("(");
    cocktailName = cocktailNameArray[0];

  }
  
  console.log("name of cocktail : " + cocktailName);

  var response = null;
   
  const baseURL = "http://bixbar.run.goorm.io/cocktail/?q=";
 
  if(cocktailName.length == 0){
    throw fail.checkedError("No Result", "NoResult");
  }  
  else{
    
    let url = baseURL + cocktailName; //http://bixbar.run.goorm.io/cocktail/?q=DirtyMartini
   
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



