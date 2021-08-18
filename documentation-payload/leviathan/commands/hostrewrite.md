+++
title = "hostrewrite"
chapter = false
weight = 100
hidden = false
+++

## Summary

Rewrite host header for outgoing requests
- Needs Admin: False  
- Version: 1  
- Author: @sysop_host  

### Arguments

#### tabid

- Description:   
- Required Value: True  
- Default Value: None  

#### host

- Description: Host header to inject
- Required Value: True  
- Default Value: None  

## Usage

```
hostrewrite {"host":"host header value"}
```


## Detailed Summary

This command uses the chrome.webRequest API to inject an arbitrary host header in the outgoing request.
https://developer.chrome.com/docs/extensions/reference/webRequest/#event-onSendHeaders