def api_gw_request():
    return {
        "resource": "/{proxy+}",
        "path": "/",
        "httpMethod": "POST",
        "headers": {},
        "multiValueHeaders": {},
        "queryStringParameters": None,
        "multiValueQueryStringParameters": None,
        "pathParameters": {"proxy": "send-contact-form"},
        "stageVariables": None,
        "requestContext": {},
        "body": '{\r\n  "name": "string",\r\n  "email": "user@example.com",\r\n  "message": "string"\r\n}',
        "isBase64Encoded": False,
    }
