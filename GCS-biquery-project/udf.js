function transform(line){
    var values = line.split(',');
    var obj = new Object();
    obj.id = values[0];
    obj.FirstName = values[1];
    obj.LastName = values[2];
    obj.Email = values[3];
    obj.Department = values[4];
    var jsonString = JSON.stringify(obj)
    return jsonString
   
}