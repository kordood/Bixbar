module.exports.function = function accessVivContext (survey, $vivContext) {
  //JSON.stringify($vivContext, undefined, 1);
  //String bixbyUserId = $vivContext.bixbyUserId
  userID = JSON.stringify($vivContext.bixbyUserId, undefined, 1);

  return {
    userID : userID,
    gender: survey.gender,
    age: survey.age,
  };
}
