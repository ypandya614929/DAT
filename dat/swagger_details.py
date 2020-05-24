EmotionActivity = {
    "name": "emotion",
    "http_method": "post",
    "resource_type": "list",
    "fields": {
            "Enter Text": {
                "type": "string",
                "param_type": "body",
                "required": True,
                "description": "Enter Text That You Want To Analyse",
            }
        }
}

UserEmotionActivity = {
    "name": "useremotion",
    "http_method": "post",
    "resource_type": "list",
    "fields": {
            "Enter Userid": {
                "type": "string",
                "param_type": "body",
                "required": True,
                "description": "Enter Twitter Userid",
            }
        }
}

HashEmotionActivity = {
    "name": "hashemotion",
    "http_method": "post",
    "resource_type": "list",
    "fields": {
            "Enter Hashtag ": {
                "type": "string",
                "param_type": "body",
                "required": True,
                "description": "Enter Twitter Hashtag Including '#' ",
            }
        }
}

TimechartActivity = {
    "name": "timechart",
    "http_method": "post",
    "resource_type": "list",
    "fields": {
            "Enter Userid ": {
                "type": "string",
                "param_type": "body",
                "required": True,
                "description": "Enter Twitter Userid",
            }
        }
}

UrlActivity = {
    "name": "url",
    "http_method": "post",
    "resource_type": "list",
    "fields": {
            "Enter Userid ": {
                "type": "string",
                "param_type": "body",
                "required": True,
                "description": "Enter Twitter Userid",
            }
        }
}

SourceActivity = {
    "name": "source",
    "http_method": "post",
    "resource_type": "list",
    "fields": {
            "Enter Hashtag ": {
                "type": "string",
                "param_type": "body",
                "required": True,
                "description": "Enter Twitter Hashtag Including '#' ",
            }
        }
}
