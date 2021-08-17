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

            rows.push({"url": data["url"],
                        "state": data["state"],
                        "danger": data["danger"],
                        "filename": data["filename"],
                        "mime": data["mime"],
                        "incognito": data["incognito"],
                        "exists": data["exists"],
                        "fileSize": data["fileSize"],
                        "start time": support_scripts["leviathan_iso_date_to_human_readable"](data["startTime"]),
                        "end time": support_scripts["leviathan_iso_date_to_human_readable"](data["endTime"]),
                        "row-style": row_style,
                        "cell-style": cell_style
            });
        }   
	}
    	return support_scripts["leviathan_create_table"](
            [
                {"name":"url"},
                {"name":"state"},
                {"name":"danger"},
                {"name":"filename"},
                {"name":"mime"},
                {"name":"incognito"},
                {"name":"exists"},
                {"name":"fileSize"},
                {"name":"start time"},
                {"name":"end time"}
            ], rows);
    }catch(error){
        console.log(error)
        return  "<pre> Error: View console for messages</pre>";
    }
}