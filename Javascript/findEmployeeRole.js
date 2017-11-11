

function findEmployeesRole(name) {
  nameSplit = name.split(" ");
  firstName = nameSplit[0];
  lastName = nameSplit[1];
  for(var i = employees.length-1; i>=0; i--){
    if(firstName == employees[i].firstName && lastName == employees[i].lastName){
      return employees[i].role;
    }
  }
  return "Does not work here!";
}