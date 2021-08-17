function(isoString){
    var humanDate = new Date(isoString);
    return humanDate.toLocaleString('en-GB');
}