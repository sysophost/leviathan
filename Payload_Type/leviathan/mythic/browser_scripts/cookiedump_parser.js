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

            rows.push({"domain": data["domain"],
                        "name": data["name"],
                        "expires": support_scripts["leviathan_epoch_to_human_readable"](data["expirationDate"]),
                        "hostOnly": data["hostOnly"],
                        "httpOnly": data["httpOnly"],
                        "secure": data["secure"],
                        "session": data["session"],
                        "value": data["value"],
                        "row-style": row_style,
                        "cell-style": cell_style
            });
        }   
	}
    	return support_scripts["leviathan_create_table"](
            [
                {"name":"domain"},
                {"name":"name"},
                {"name":"expires"},
                {"name":"hostOnly"},
                {"name":"httpOnly"},
                {"name":"secure"},
                {"name":"session"},
                {"name":"value"}
            ], rows);
    }catch(error){
        console.log(error)
        return  "<pre> Error: View console for messages</pre>";
    }
}