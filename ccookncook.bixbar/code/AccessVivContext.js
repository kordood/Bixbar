module.exports.function = function accessVivContext ($vivContext) {
  //JSON.stringify($vivContext, undefined, 1);
  //String bixbyUserId = $vivContext.bixbyUserId
  return JSON.stringify($vivContext.bixbyUserId, undefined, 1);
}
