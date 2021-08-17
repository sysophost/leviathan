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

            rows.push({"title": data["window"],
                        "url": data["url"],
                        "incognito": data["incognito"],
                        "active": data["active"],
                        "highlighted": data["highlighted"],
                        "window id": data["windowid"],
                        "tab id": data["id"],
                        "row-style": row_style,
                        "cell-style": cell_style
            });
        }   
	}
    	return support_scripts["leviathan_create_table"](
            [
                {"name":"title"},
                {"name":"url"},
                {"name":"incognito"},
                {"name":"active"},
                {"name":"highlighted"},
                {"name":"window id"},
                {"name":"tab id"},
            ], rows);
    }catch(error){
        console.log(error)
        return  "<pre> Error: View console for messages</pre>";
    }
}