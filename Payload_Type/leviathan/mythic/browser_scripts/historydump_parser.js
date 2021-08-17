function(task, responses){
	if(task.status === "error"){
		return "<pre> Error: untoggle for error message(s) </pre>";
	}
  let rows = [];
  try{
  	for(let i = 0; i < responses.length; i++){
        let respdata = JSON.parse(responses[i]["response"]);
        for(let i = 0; i < respdata.length; i++){
            let data = respdata[i]
            let row_style = "";
            let cell_style = {"hidden": "text-align:center", "type":"text-align:center"};

            rows.push({"title": data["title"],
                        "url": data["url"],
                        "last visit time": support_scripts["leviathan_long_epoch_to_human_readable"](data["lastVisitTime"]),
                        "typed count": data["typedCount"],
                        "visit count": data["visitCount"],
                        "row-style": row_style,
                        "cell-style": cell_style
            });
        }   
	}
    	return support_scripts["leviathan_create_table"](
            [
                {"name":"title"},
                {"name":"url"},
                {"name":"last visit time"},
                {"name":"typed count"},
                {"name":"visit count"}
            ], rows);
    }catch(error){
        console.log(error)
        return  "<pre> Error: View console for messages</pre>";
    }
}