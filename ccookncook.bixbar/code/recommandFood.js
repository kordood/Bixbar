module.exports.function = function recommandFood (queryInput) {
  const console = require('console');
  const fail = require("fail");
  var http = require("http");
  var config = require('config');
  
  console.log("input string: " + queryInput);
  
  //띄어쓰기 삭제 
  queryInput = queryInput.replace(" ", "");
  
  console.log("input string: " + queryInput);

  var response = null;
   
  const baseURL = "http://bixbar.run.goorm.io/getfood/?q=";
 
  if(queryInput.length == 0){
    throw fail.checkedError("No Result", "NoResult");
  }  
  else{
    
    let url = baseURL + queryInput; //http://bixbar.run.goorm.io/getfood/?q=abcde
   
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
