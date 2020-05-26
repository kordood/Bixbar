module.exports.function = function submitSurvey (gender, age) {
  // Simply construct an object from the inputs and return it.
  // This is where your API call to submit a survey will be (if desired).
  return {
    gender: gender,
    age: age,
  };
}
