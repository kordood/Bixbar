module.exports.function = function recommand (cocktailName) {
  
  const console = require('console');
  const fail = require("fail");
  var http = require("http");
  var config = require('config');
  console.log("name of cocktail : " + cocktailName);
 

  
  //cocktail name -> CocktailName으로 바꿔주기 
 // cocktailName = cocktailName.replace(" ", "") ;
  
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
      
      //*** cachetime?
      //**** returnheaders?
      //headers: {
      // 'Authorization': 'Bearer V0NfNbS9Z-xrycNiVVq54x4EWNKjGuA-ihy1AQorDNMAAAFtgVl4Xw'
      //},
    };

    console.log("OK");
    //return type : json
    //response = http.getUrl(baseURL, options);
    response = http.getUrl(url, options);
    
    console.log("OK");
    console.log(response);

    
    if(response.status == 404 ){
 
      throw fail.checkedError("No Result", "404 error");  

    }
    
  }

 
  // var results;
  // results = {
  //   "title" : response.title,
  //   "img" : response.img,
  //   "recipe" : response.recipe,
  // };

  //아직 의문
  return response;
}



// /************************************************************************/
// /*                               Requires                               */
// /************************************************************************/
// var http    = require("http");

// module.exports.function = function profile (kakaoProfile) {
// let options = {
//     format : 'json',
//     headers: {
//       'Authorization': 'Bearer V0NfNbS9Z-xrycNiVVq54x4EWNKjGuA-ihy1AQorDNMAAAFtgVl4Xw'
//     },
//   };
// let url     = "https://bixbar.com/" + cocktailName
// let results = http.getUrl(url, options);

// //프로필없는 경우
// if (results.profileImageURL == ""){
//   results.profileImageURL = "/images/default.png"
//   results.thumbnailURL    = "/images/default.png"
// }
// return results
// }




// module.exports.function = function plusOperation (leftOperand, rightOperand) {
 
//  const console = require('conslole');

//  let name = "더하기";
//  let result = leftOperand + rightOperand;

//  console.log("name : " + name);
//  console.log("result : "+ result);

//   return {
//     result : result,
//     operatorName : name
    

//   };
// }
