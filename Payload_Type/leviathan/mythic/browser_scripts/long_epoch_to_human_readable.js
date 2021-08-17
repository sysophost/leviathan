function(epochTimestamp){
    var humanDate = new Date(epochTimestamp);
    return humanDate.toLocaleString('en-GB');
}