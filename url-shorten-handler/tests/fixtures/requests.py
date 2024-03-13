def api_gw_request_post_url():
    return {
        "version": "2.0",
        "routeKey": "POST /urls",
        "rawPath": "/urls",
        "rawQueryString": "",
        "headers": {
            "accept": "*/*",
            "authorization": "Bearer eyJraWQiOiJVUjlGTWU0c3pJNWxaK0dNOUZjUnRXeXdEbzNtNnkxMEVOOTByZWdxWDBNPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIzNjcyYzU5ZC01ZmJjLTRlNWItOWU3Yy0xOWI1OTdmZjM2MDMiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmV1LXdlc3QtMi5hbWF6b25hd3MuY29tXC9ldS13ZXN0LTJfV3VyeDZGSVVkIiwiY29nbml0bzp1c2VybmFtZSI6ImJhcnQiLCJvcmlnaW5fanRpIjoiOTdjM2ZkNDktNzc3NS00MWI0LTg0ODktNmEyMTA2NDAzZjBhIiwiYXVkIjoiN3JlNmM5a21yYmRiam1qM3YzM3BubmxzOHMiLCJldmVudF9pZCI6IjEwODI2MjQ1LTdiY2QtNGZlMi05NzA4LTEyODFlOTY4OTcyOSIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNzA5OTI4MTMxLCJuaWNrbmFtZSI6ImJhcnQiLCJleHAiOjE3MDk5MzE3MzEsImlhdCI6MTcwOTkyODEzMSwianRpIjoiOWQyYjFhYmItNGQ0NC00NTliLWFiNDktYjg3NThmNjI5MGNkIiwiZW1haWwiOiJiYXJ0b3N6X3BAaG90bWFpbC5jb20ifQ.lZiKoNXm8LyNftWQm4myOR4QHRwN5X7p9w-iLPchj3vcMeI5jc29OS5bw2OnQKFX7Fk76XNgKRA8byItT3eTnyMD0RhMgohA5PBIguytPwMHeEoWoaQau-UOgrBzMi4XXsWmc5QVtk7B13Cdb_un0GiDe1Xkt7STOsJt8ZazuJ8mHUuv4SRjBrK3x2Z832pOXa1ybiCWCFTMjbIizl-vMQg3SuNTnO8jnjxoyJhEV60jN1NCpPXqh1O2-z2Hjh0_oKhfSGdVKBDL-suvTNkU4OY_XGhIVRT8gNVjVOTMmqExwUx_vGyJ2qhODKyVo1hCqs4TpPVu9XXiQvCpiNMR4w",
            "content-type": "application/json",
            "host": "shorten.rtx.wtf",
            "user-agent": "insomnia/8.6.1",
        },
        "requestContext": {
            "accountId": "907824143427",
            "apiId": "efx7utlm0j",
            "authorizer": {
                "jwt": {
                    "claims": {
                        "aud": "7re6c9kmrbdbjmj3v33pnnls8s",
                        "auth_time": "1709928131",
                        "cognito:username": "bart",
                        "email": "bartosz_p@hotmail.com",
                        "email_verified": "true",
                        "exp": "1709931731",
                        "iat": "1709928131",
                        "nickname": "bart",
                        "token_use": "id",
                    },
                    "scopes": None,
                }
            },
            "domainName": "shorten.rtx.wtf",
            "domainPrefix": "shorten",
            "http": {
                "method": "POST",
                "path": "/urls",
                "protocol": "HTTP/1.1",
                "sourceIp": "82.21.32.80",
                "userAgent": "insomnia/8.6.1",
            },
            "requestId": "UU5AfhhCLPEEMuA=",
            "routeKey": "POST /urls",
            "stage": "$default",
            "time": "08/Mar/2024:20:02:23 +0000",
        },
        "body": '{\n\t"url":"https://media.tenor.com/d7VOr5nJ0W4AAAAC/cat-meme.gif"\n}',
        "isBase64Encoded": False,
    }


def request_context():
    return {
        "accountId": "907824143427",
        "apiId": "efx7utlm0j",
        "authorizer": {
            "jwt": {
                "claims": {
                    "aud": "7re6c9kmrbdbjmj3v33pnnls8s",
                    "auth_time": "1709761939",
                    "cognito:username": "bart",
                }
            }
        },
    }


def api_gw_request_options_url():
    return {
        "version": "2.0",
        "routeKey": "OPTIONS /urls",
        "rawPath": "/urls",
        "rawQueryString": "",
        "headers": {
            "accept": "*/*",
            "content-length": "0",
            "host": "shorten.rtx.wtf",
            "user-agent": "insomnia/8.6.1",
            "via": "2.0 dbeea278d9cc0659ab002a66cfdb03f8.cloudfront.net (CloudFront)",
            "x-amz-cf-id": "SDKtx_-mSxyOAUqOfwT0scdJqb5WONPKx46kZcp_g1P3i05tKWILNA==",
            "x-amzn-trace-id": "Root=1-65eb6f1d-2436e5330d393a9f2b75d5dd",
            "x-forwarded-for": "82.21.32.80, 15.158.44.204",
            "x-forwarded-port": "443",
            "x-forwarded-proto": "https",
        },
        "requestContext": {
            "accountId": "907824143427",
            "apiId": "efx7utlm0j",
            "domainName": "shorten.rtx.wtf",
            "domainPrefix": "shorten",
            "http": {
                "method": "OPTIONS",
                "path": "/urls",
                "protocol": "HTTP/1.1",
                "sourceIp": "82.21.32.80",
                "userAgent": "insomnia/8.6.1",
            },
            "requestId": "UU5MlglMLPEEPSA=",
            "routeKey": "OPTIONS /urls",
            "stage": "$default",
            "time": "08/Mar/2024:20:03:41 +0000",
            "timeEpoch": 1709928221048,
        },
        "isBase64Encoded": False,
    }


def api_gw_request_get_url():
    return {
        "version": "2.0",
        "routeKey": "GET /urls",
        "rawPath": "/urls",
        "rawQueryString": "",
        "headers": {
            "accept": "*/*",
            "authorization": "Bearer eyJraWQiOiJVUjlGTWU0c3pJNWxaK0dNOUZjUnRXeXdEbzNtNnkxMEVOOTByZWdxWDBNPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIzNjcyYzU5ZC01ZmJjLTRlNWItOWU3Yy0xOWI1OTdmZjM2MDMiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmV1LXdlc3QtMi5hbWF6b25hd3MuY29tXC9ldS13ZXN0LTJfV3VyeDZGSVVkIiwiY29nbml0bzp1c2VybmFtZSI6ImJhcnQiLCJvcmlnaW5fanRpIjoiOTdjM2ZkNDktNzc3NS00MWI0LTg0ODktNmEyMTA2NDAzZjBhIiwiYXVkIjoiN3JlNmM5a21yYmRiam1qM3YzM3BubmxzOHMiLCJldmVudF9pZCI6IjEwODI2MjQ1LTdiY2QtNGZlMi05NzA4LTEyODFlOTY4OTcyOSIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNzA5OTI4MTMxLCJuaWNrbmFtZSI6ImJhcnQiLCJleHAiOjE3MDk5MzE3MzEsImlhdCI6MTcwOTkyODEzMSwianRpIjoiOWQyYjFhYmItNGQ0NC00NTliLWFiNDktYjg3NThmNjI5MGNkIiwiZW1haWwiOiJiYXJ0b3N6X3BAaG90bWFpbC5jb20ifQ.lZiKoNXm8LyNftWQm4myOR4QHRwN5X7p9w-iLPchj3vcMeI5jc29OS5bw2OnQKFX7Fk76XNgKRA8byItT3eTnyMD0RhMgohA5PBIguytPwMHeEoWoaQau-UOgrBzMi4XXsWmc5QVtk7B13Cdb_un0GiDe1Xkt7STOsJt8ZazuJ8mHUuv4SRjBrK3x2Z832pOXa1ybiCWCFTMjbIizl-vMQg3SuNTnO8jnjxoyJhEV60jN1NCpPXqh1O2-z2Hjh0_oKhfSGdVKBDL-suvTNkU4OY_XGhIVRT8gNVjVOTMmqExwUx_vGyJ2qhODKyVo1hCqs4TpPVu9XXiQvCpiNMR4w.eyJzdWIiOiIzNjcyYzU5ZC01ZmJjLTRlNWItOWU3Yy0xOWI1OTdmZjM2MDMiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmV1LXdlc3QtMi5hbWF6b25hd3MuY29tXC9ldS13ZXN0LTJfV3VyeDZGSVVkIiwiY29nbml0bzp1c2VybmFtZSI6ImJhcnQiLCJvcmlnaW5fanRpIjoiYzlmYjllMTYtYTVmMC00NTFlLTgxYTAtMzQzNWM5MWJhZTdkIiwiYXVkIjoiN3JlNmM5a21yYmRiam1qM3YzM3BubmxzOHMiLCJldmVudF9pZCI6ImZiNGYzOTE3LTBmYmMtNDE4OC04ZGNlLWUzMTNiZTFjNTg2MCIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNzA5OTEwMjQ5LCJuaWNrbmFtZSI6ImJhcnQiLCJleHAiOjE3MDk5MTM4NDksImlhdCI6MTcwOTkxMDI0OSwianRpIjoiZDgwMjM5NzMtZTZmNy00NjNkLWI5ODYtOTk1YTg1OWQwNjZkIiwiZW1haWwiOiJiYXJ0b3N6X3BAaG90bWFpbC5jb20ifQ.x_XswP3IcMPL4teNiOh_hKLrmLcfunY3M2BPmJhrvDchtTTKp9lXoqOTgqye5PC1V2beFwknmMQqlWPVrh1LkyOwuO-ZtaYdxI9iskQYFeLxzzOmk8ZWnn-of3ahMktN6w33LQpqQgsUOSoapWlKWrdh4FOqhKp9tY1xeDslfZpZIe5o7CHdlxptKxDLUEUmOpHKBSu4P0F-7jm6SxHIm9BS8NPpqMtXiTy3DeLK4OeaRwoQ_d5_akwPIqG5gaElOV1rp1LvoJS5bjGW8v4Cx2zMxzma2HebuozIe-_xj6BzVwRqUc61eVJcU7Tu97RzdEZWeDKMKR7NBby2mu68QQ",
            "content-length": "0",
            "host": "shorten.rtx.wtf",
            "user-agent": "insomnia/8.6.1",
            "via": "2.0 dbeea278d9cc0659ab002a66cfdb03f8.cloudfront.net (CloudFront)",
            "x-amz-cf-id": "qWMKJ968JgK0fYoNcvCfTQ-CQ5YSvgElZBQhuodWeKRePRlweKKOVg==",
            "x-amzn-trace-id": "Root=1-65eb6ef7-1c34729c5815f8da288320f1",
            "x-forwarded-for": "82.21.32.80, 15.158.44.204",
            "x-forwarded-port": "443",
            "x-forwarded-proto": "https",
        },
        "requestContext": {
            "accountId": "907824143427",
            "apiId": "efx7utlm0j",
            "domainName": "shorten.rtx.wtf",
            "domainPrefix": "shorten",
            "http": {
                "method": "GET",
                "path": "/urls",
                "protocol": "HTTP/1.1",
                "sourceIp": "82.21.32.80",
                "userAgent": "insomnia/8.6.1",
            },
            "requestId": "UU5GrgRkrPEEPKQ=",
            "routeKey": "GET /urls",
            "stage": "$default",
            "time": "08/Mar/2024:20:03:03 +0000",
            "timeEpoch": 1709928183234,
        },
        "isBase64Encoded": False,
    }


def api_gw_request_get_url_list_jwt():
    return {
        "version": "2.0",
        "routeKey": "GET /{id+}",
        "rawPath": "/api/urls/G3rZi26WMeGnqVvuNSnENu",
        "rawQueryString": "",
        "headers": {
            "cache-control": "no-cache",
            "content-length": "0",
            "host": "efx7utlm0j.execute-api.eu-west-2.amazonaws.com",
            "user-agent": "Amazon CloudFront",
            "via": "1.1 cb3394cad3f414f33c4f30965c750226.cloudfront.net (CloudFront)",
            "x-amz-cf-id": "Ot_Jg3a7rED4t9MLIXAayWc35quJbYnGq6Uz8Yh538E56u2YR1CxHw==",
            "x-amzn-trace-id": "Root=1-653e2c65-2567a04d526bfa2749ada0a9",
            "x-forwarded-for": "2.99.21.143, 15.158.44.243",
            "x-forwarded-port": "443",
            "x-forwarded-proto": "https",
        },
        "requestContext": request_context(),
        "pathParameters": {"proxy": "api/urls/G3rZi26WMeGnqVvuNSnENu"},
        "isBase64Encoded": False,
    }


def api_gw_request_get_url_shorten_rtx():
    return {
        "version": "2.0",
        "routeKey": "GET /{id+}",
        "rawPath": "/api/urls/G3rZi26WMeGnqVvuNSnENu",
        "rawQueryString": "",
        "headers": {
            "cache-control": "no-cache",
            "content-length": "0",
            "host": "efx7utlm0j.execute-api.eu-west-2.amazonaws.com",
            "user-agent": "Amazon CloudFront",
            "via": "1.1 cb3394cad3f414f33c4f30965c750226.cloudfront.net (CloudFront)",
            "x-amz-cf-id": "Ot_Jg3a7rED4t9MLIXAayWc35quJbYnGq6Uz8Yh538E56u2YR1CxHw==",
            "x-amzn-trace-id": "Root=1-653e2c65-2567a04d526bfa2749ada0a9",
            "x-forwarded-for": "2.99.21.143, 15.158.44.243",
            "x-forwarded-port": "443",
            "x-forwarded-proto": "https",
        },
        "requestContext": {
            "accountId": "907824143427",
            "apiId": "efx7utlm0j",
            "domainName": "efx7utlm0j.execute-api.eu-west-2.amazonaws.com",
            "domainPrefix": "efx7utlm0j",
            "http": {
                "method": "GET",
                "path": "/api/urls/G3rZi26WMeGnqVvuNSnENu",
                "protocol": "HTTP/1.1",
                "sourceIp": "2.99.21.143",
                "userAgent": "Amazon CloudFront",
            },
            "requestId": "Njvf9gy3LPEEJfA=",
            "routeKey": "GET /{id+}",
            "stage": "$default",
            "time": "29/Oct/2023:09:56:53 +0000",
            "timeEpoch": 1698573413854,
        },
        "pathParameters": {"proxy": "api/urls/G3rZi26WMeGnqVvuNSnENu"},
        "isBase64Encoded": False,
    }


# def api_gw_request_get_url_stats():
#     return {
#         "version": "2.0",
#         "routeKey": "GET /urls/stats/{id+}",
#         "rawPath": "/urls/stats/G3rZi26WMeGnqVvuNSnENu",
#         "rawQueryString": "",
#         "headers": {
#             "accept": "*/*",
#             "accept-encoding": "gzip, deflate, br",
#             "cache-control": "no-cache",
#             "content-length": "38",
#             "content-type": "application/json",
#             "host": "shorten.rtx.wtf",
#             "postman-token": "29f99b36-31b1-437f-bf56-804b20a90200",
#             "user-agent": "PostmanRuntime/7.32.3",
#             "x-amzn-trace-id": "Root=1-64e9f530-2debc86545e295bb0a1f8e64",
#             "x-forwarded-for": "78.150.27.179",
#             "x-forwarded-port": "443",
#             "x-forwarded-proto": "https",
#         },
#         "requestContext": {
#             "accountId": "907824143427",
#             "apiId": "efx7utlm0j",
#             "domainName": "shorten.rtx.wtf",
#             "domainPrefix": "shorten",
#             "http": {
#                 "method": "GET",
#                 "path": "/urls/stats/G3rZi26WMeGnqVvuNSnENu",
#                 "protocol": "HTTP/1.1",
#                 "sourceIp": "78.150.27.179",
#                 "userAgent": "PostmanRuntime/7.32.3",
#             },
#             "requestId": "KRM_qhBxLPEEPhQ=",
#             "routeKey": "GET /urls/stats/{id+}",
#             "stage": "$default",
#             "time": "26/Aug/2023:12:50:56 +0000",
#             "timeEpoch": 1693054256780,
#         },
#         "pathParameters": {"proxy": "G3rZi26WMeGnqVvuNSnENu"},
#         "body": '{\r\n    "url": "https://baaart.dev/"\r\n}',
#         "isBase64Encoded": False,
#     }


def api_gw_request_delete_url():
    return {
        "version": "2.0",
        "routeKey": "DELETE /urls",
        "rawPath": "/urls",
        "rawQueryString": "",
        "headers": {
            "accept": "*/*",
            "authorization": "Bearer eyJraWQiOiJVUjlGTWU0c3pJNWxaK0dNOUZjUnRXeXdEbzNtNnkxMEVOOTByZWdxWDBNPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIzNjcyYzU5ZC01ZmJjLTRlNWItOWU3Yy0xOWI1OTdmZjM2MDMiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmV1LXdlc3QtMi5hbWF6b25hd3MuY29tXC9ldS13ZXN0LTJfV3VyeDZGSVVkIiwiY29nbml0bzp1c2VybmFtZSI6ImJhcnQiLCJvcmlnaW5fanRpIjoiOTdjM2ZkNDktNzc3NS00MWI0LTg0ODktNmEyMTA2NDAzZjBhIiwiYXVkIjoiN3JlNmM5a21yYmRiam1qM3YzM3BubmxzOHMiLCJldmVudF9pZCI6IjEwODI2MjQ1LTdiY2QtNGZlMi05NzA4LTEyODFlOTY4OTcyOSIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNzA5OTI4MTMxLCJuaWNrbmFtZSI6ImJhcnQiLCJleHAiOjE3MDk5MzE3MzEsImlhdCI6MTcwOTkyODEzMSwianRpIjoiOWQyYjFhYmItNGQ0NC00NTliLWFiNDktYjg3NThmNjI5MGNkIiwiZW1haWwiOiJiYXJ0b3N6X3BAaG90bWFpbC5jb20ifQ.lZiKoNXm8LyNftWQm4myOR4QHRwN5X7p9w-iLPchj3vcMeI5jc29OS5bw2OnQKFX7Fk76XNgKRA8byItT3eTnyMD0RhMgohA5PBIguytPwMHeEoWoaQau-UOgrBzMi4XXsWmc5QVtk7B13Cdb_un0GiDe1Xkt7STOsJt8ZazuJ8mHUuv4SRjBrK3x2Z832pOXa1ybiCWCFTMjbIizl-vMQg3SuNTnO8jnjxoyJhEV60jN1NCpPXqh1O2-z2Hjh0_oKhfSGdVKBDL-suvTNkU4OY_XGhIVRT8gNVjVOTMmqExwUx_vGyJ2qhODKyVo1hCqs4TpPVu9XXiQvCpiNMR4w",
            "content-length": "20",
            "content-type": "application/json",
            "host": "shorten.rtx.wtf",
            "user-agent": "insomnia/8.6.1",
            "via": "2.0 dbeea278d9cc0659ab002a66cfdb03f8.cloudfront.net (CloudFront)",
            "x-amz-cf-id": "nxS0ftd3PRdQT0Dn3gEq6iwtDDOBF7Gdd8bwTL1-gzF0VUBmpN5RQQ==",
            "x-amzn-trace-id": "Root=1-65eb6f2b-150e8c401265c453635c54ef",
            "x-forwarded-for": "82.21.32.80, 15.158.44.204",
            "x-forwarded-port": "443",
            "x-forwarded-proto": "https",
        },
        "requestContext": {
            "accountId": "907824143427",
            "apiId": "efx7utlm0j",
            "authorizer": {
                "jwt": {
                    "claims": {
                        "aud": "7re6c9kmrbdbjmj3v33pnnls8s",
                        "auth_time": "1709928131",
                        "cognito:username": "bart",
                        "email": "bartosz_p@hotmail.com",
                        "email_verified": "true",
                        "event_id": "10826245-7bcd-4fe2-9708-1281e9689729",
                        "exp": "1709931731",
                        "iat": "1709928131",
                        "iss": "https://cognito-idp.eu-west-2.amazonaws.com/eu-west-2_Wurx6FIUd",
                        "jti": "9d2b1abb-4d44-459b-ab49-b8758f6290cd",
                        "nickname": "bart",
                        "origin_jti": "97c3fd49-7775-41b4-8489-6a2106403f0a",
                        "sub": "3672c59d-5fbc-4e5b-9e7c-19b597ff3603",
                        "token_use": "id",
                    },
                    "scopes": None,
                }
            },
            "domainName": "shorten.rtx.wtf",
            "domainPrefix": "shorten",
            "http": {
                "method": "DELETE",
                "path": "/urls",
                "protocol": "HTTP/1.1",
                "sourceIp": "82.21.32.80",
                "userAgent": "insomnia/8.6.1",
            },
            "requestId": "UU5O0gyJrPEEPpw=",
            "routeKey": "DELETE /urls",
            "stage": "$default",
            "time": "08/Mar/2024:20:03:55 +0000",
            "timeEpoch": 1709928235342,
        },
        "body": '{\n\t"id":"728ed52f"\n}',
        "isBase64Encoded": False,
    }


def api_gw_request_from_rtx_wtf():
    return {
        "version": "2.0",
        "routeKey": "GET /{id+}",
        "rawPath": "/s/s/oRtPrwjaSit",
        "rawQueryString": "",
        "headers": {
            "content-length": "0",
            "host": "efx7utlm0j.execute-api.eu-west-2.amazonaws.com",
            "user-agent": "Amazon CloudFront",
            "via": "2.0 b269fc7bf7bd5b98493a3164ee915228.cloudfront.net (CloudFront)",
            "x-amz-cf-id": "uDsaDyg5fmK8QIAVKsdlY1l4c5NQ4JOE-P_muLz3DInvPk8KWIoKww==",
            "x-amzn-trace-id": "Root=1-65eb6faa-54aa50ef7710582477870402",
            "x-forwarded-for": "82.21.32.80, 3.172.1.111",
            "x-forwarded-port": "443",
            "x-forwarded-proto": "https",
        },
        "requestContext": {
            "accountId": "907824143427",
            "apiId": "efx7utlm0j",
            "domainName": "efx7utlm0j.execute-api.eu-west-2.amazonaws.com",
            "domainPrefix": "efx7utlm0j",
            "http": {
                "method": "GET",
                "path": "/s/s/oRtPrwjaSit",
                "protocol": "HTTP/1.1",
                "sourceIp": "82.21.32.80",
                "userAgent": "Amazon CloudFront",
            },
            "requestId": "UU5itiEorPEEPOQ=",
            "routeKey": "GET /{id+}",
            "stage": "$default",
            "time": "08/Mar/2024:20:06:02 +0000",
            "timeEpoch": 1709928362665,
        },
        "pathParameters": {"id": "s/s/oRtPrwjaSit"},
        "isBase64Encoded": False,
    }


def api_gw_request_from_rtx_wtf_alternative():
    return {
        "version": "2.0",
        "routeKey": "GET /{id+}",
        "rawPath": "/s/s/G3rZi26WMeGnqVvuNSnENu",
        "rawQueryString": "",
        "headers": {
            "cache-control": "no-cache",
            "content-length": "0",
            "host": "efx7utlm0j.execute-api.eu-west-2.amazonaws.com",
            "user-agent": "Amazon CloudFront",
            "via": "1.1 716fd417a527ecd4f9d6cef2c9258582.cloudfront.net (CloudFront)",
            "x-amz-cf-id": "vZUzrviMrXOdCbRbp5uZeE6ct9UbJMqV4uqIOWLc4UR_SqtjCIFuoA==",
            "x-amzn-trace-id": "Root=1-64ec9323-5c593db9447e0a122bd98985",
            "x-forwarded-for": "78.150.27.179, 70.132.46.141",
            "x-forwarded-port": "443",
            "x-forwarded-proto": "https",
        },
        "requestContext": {
            "accountId": "907824143427",
            "apiId": "efx7utlm0j",
            "domainName": "efx7utlm0j.execute-api.eu-west-2.amazonaws.com",
            "domainPrefix": "efx7utlm0j",
            "http": {
                "method": "GET",
                "path": "/s/s/G3rZi26WMeGnqVvuNSnENu",
                "protocol": "HTTP/1.1",
                "sourceIp": "78.150.27.179",
                "userAgent": "Amazon CloudFront",
            },
            "requestId": "KXvtlg6jLPEEJbg=",
            "routeKey": "GET /{id+}",
            "stage": "$default",
            "time": "28/Aug/2023:12:29:23 +0000",
            "timeEpoch": 1693225763423,
        },
        "pathParameters": {"proxy": "s/G3rZi26WMeGnqVvuNSnENu"},
        "isBase64Encoded": False,
    }


def api_gw_request_get_url_stats_trailing_slash():
    return {
        "version": "2.0",
        "routeKey": "GET /stats/{id+}",
        "rawPath": "/stats/bart",
        "rawQueryString": "",
        "headers": {
            "accept": "*/*",
            "authorization": "Bearer eyJraWQiOiJVUjlGTWU0c3pJNWxaK0dNOUZjUnRXeXdEbzNtNnkxMEVOOTByZWdxWDBNPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIzNjcyYzU5ZC01ZmJjLTRlNWItOWU3Yy0xOWI1OTdmZjM2MDMiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmV1LXdlc3QtMi5hbWF6b25hd3MuY29tXC9ldS13ZXN0LTJfV3VyeDZGSVVkIiwiY29nbml0bzp1c2VybmFtZSI6ImJhcnQiLCJvcmlnaW5fanRpIjoiOTdjM2ZkNDktNzc3NS00MWI0LTg0ODktNmEyMTA2NDAzZjBhIiwiYXVkIjoiN3JlNmM5a21yYmRiam1qM3YzM3BubmxzOHMiLCJldmVudF9pZCI6IjEwODI2MjQ1LTdiY2QtNGZlMi05NzA4LTEyODFlOTY4OTcyOSIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNzA5OTI4MTMxLCJuaWNrbmFtZSI6ImJhcnQiLCJleHAiOjE3MDk5MzE3MzEsImlhdCI6MTcwOTkyODEzMSwianRpIjoiOWQyYjFhYmItNGQ0NC00NTliLWFiNDktYjg3NThmNjI5MGNkIiwiZW1haWwiOiJiYXJ0b3N6X3BAaG90bWFpbC5jb20ifQ.lZiKoNXm8LyNftWQm4myOR4QHRwN5X7p9w-iLPchj3vcMeI5jc29OS5bw2OnQKFX7Fk76XNgKRA8byItT3eTnyMD0RhMgohA5PBIguytPwMHeEoWoaQau-UOgrBzMi4XXsWmc5QVtk7B13Cdb_un0GiDe1Xkt7STOsJt8ZazuJ8mHUuv4SRjBrK3x2Z832pOXa1ybiCWCFTMjbIizl-vMQg3SuNTnO8jnjxoyJhEV60jN1NCpPXqh1O2-z2Hjh0_oKhfSGdVKBDL-suvTNkU4OY_XGhIVRT8gNVjVOTMmqExwUx_vGyJ2qhODKyVo1hCqs4TpPVu9XXiQvCpiNMR4w",
            "content-length": "0",
            "host": "shorten.rtx.wtf",
            "user-agent": "insomnia/8.6.1",
            "via": "2.0 550a2e33920b164c7fc3dddc1871c3ba.cloudfront.net (CloudFront)",
            "x-amz-cf-id": "FsIiAExn8aJkZIiQhdqe_zeiEXNfpQsJBDekRoYskHOsFuUQBkNSZw==",
            "x-amzn-trace-id": "Root=1-65eb6fc0-3aca31b4649e52a07a1b8012",
            "x-forwarded-for": "82.21.32.80, 15.158.44.204",
            "x-forwarded-port": "443",
            "x-forwarded-proto": "https",
        },
        "requestContext": {
            "accountId": "907824143427",
            "apiId": "efx7utlm0j",
            "authorizer": {
                "jwt": {
                    "claims": {
                        "aud": "7re6c9kmrbdbjmj3v33pnnls8s",
                        "auth_time": "1709928131",
                        "cognito:username": "bart",
                        "email": "bartosz_p@hotmail.com",
                        "email_verified": "true",
                        "event_id": "10826245-7bcd-4fe2-9708-1281e9689729",
                        "exp": "1709931731",
                        "iat": "1709928131",
                        "iss": "https://cognito-idp.eu-west-2.amazonaws.com/eu-west-2_Wurx6FIUd",
                        "jti": "9d2b1abb-4d44-459b-ab49-b8758f6290cd",
                        "nickname": "bart",
                        "origin_jti": "97c3fd49-7775-41b4-8489-6a2106403f0a",
                        "sub": "3672c59d-5fbc-4e5b-9e7c-19b597ff3603",
                        "token_use": "id",
                    },
                    "scopes": None,
                }
            },
            "domainName": "shorten.rtx.wtf",
            "domainPrefix": "shorten",
            "http": {
                "method": "GET",
                "path": "/stats/bart",
                "protocol": "HTTP/1.1",
                "sourceIp": "82.21.32.80",
                "userAgent": "insomnia/8.6.1",
            },
            "requestId": "UU5mLiN3rPEEPvg=",
            "routeKey": "GET /stats/{id+}",
            "stage": "$default",
            "time": "08/Mar/2024:20:06:24 +0000",
            "timeEpoch": 1709928384860,
        },
        "pathParameters": {"id": "bart"},
        "isBase64Encoded": False,
    }


def api_gw_request_list_users_urls():
    return {
        "version": "2.0",
        "routeKey": "GET /users/{username}/urls",
        "rawPath": "/users/bart/urls",
        "rawQueryString": "",
        "headers": {
            "accept": "*/*",
            "authorization": "Bearer eyJraWQiOiJVUjlGTWU0c3pJNWxaK0dNOUZjUnRXeXdEbzNtNnkxMEVOOTByZWdxWDBNPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIzNjcyYzU5ZC01ZmJjLTRlNWItOWU3Yy0xOWI1OTdmZjM2MDMiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmV1LXdlc3QtMi5hbWF6b25hd3MuY29tXC9ldS13ZXN0LTJfV3VyeDZGSVVkIiwiY29nbml0bzp1c2VybmFtZSI6ImJhcnQiLCJvcmlnaW5fanRpIjoiOTdjM2ZkNDktNzc3NS00MWI0LTg0ODktNmEyMTA2NDAzZjBhIiwiYXVkIjoiN3JlNmM5a21yYmRiam1qM3YzM3BubmxzOHMiLCJldmVudF9pZCI6IjEwODI2MjQ1LTdiY2QtNGZlMi05NzA4LTEyODFlOTY4OTcyOSIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNzA5OTI4MTMxLCJuaWNrbmFtZSI6ImJhcnQiLCJleHAiOjE3MDk5MzE3MzEsImlhdCI6MTcwOTkyODEzMSwianRpIjoiOWQyYjFhYmItNGQ0NC00NTliLWFiNDktYjg3NThmNjI5MGNkIiwiZW1haWwiOiJiYXJ0b3N6X3BAaG90bWFpbC5jb20ifQ.lZiKoNXm8LyNftWQm4myOR4QHRwN5X7p9w-iLPchj3vcMeI5jc29OS5bw2OnQKFX7Fk76XNgKRA8byItT3eTnyMD0RhMgohA5PBIguytPwMHeEoWoaQau-UOgrBzMi4XXsWmc5QVtk7B13Cdb_un0GiDe1Xkt7STOsJt8ZazuJ8mHUuv4SRjBrK3x2Z832pOXa1ybiCWCFTMjbIizl-vMQg3SuNTnO8jnjxoyJhEV60jN1NCpPXqh1O2-z2Hjh0_oKhfSGdVKBDL-suvTNkU4OY_XGhIVRT8gNVjVOTMmqExwUx_vGyJ2qhODKyVo1hCqs4TpPVu9XXiQvCpiNMR4w",
            "content-length": "0",
            "host": "shorten.rtx.wtf",
            "user-agent": "insomnia/8.6.1",
            "via": "2.0 550a2e33920b164c7fc3dddc1871c3ba.cloudfront.net (CloudFront)",
            "x-amz-cf-id": "wUPznjQ4hOs6Dj6tTOFmKYtskUhELTg2pFruWWUew9Irhu6CCT23DA==",
            "x-amzn-trace-id": "Root=1-65eb6fbc-273e63541278a8c213e72111",
            "x-forwarded-for": "82.21.32.80, 15.158.44.204",
            "x-forwarded-port": "443",
            "x-forwarded-proto": "https",
        },
        "requestContext": {
            "accountId": "907824143427",
            "apiId": "efx7utlm0j",
            "authorizer": {
                "jwt": {
                    "claims": {
                        "aud": "7re6c9kmrbdbjmj3v33pnnls8s",
                        "auth_time": "1709928131",
                        "cognito:username": "bart",
                        "email": "bartosz_p@hotmail.com",
                        "email_verified": "true",
                        "event_id": "10826245-7bcd-4fe2-9708-1281e9689729",
                        "exp": "1709931731",
                        "iat": "1709928131",
                        "iss": "https://cognito-idp.eu-west-2.amazonaws.com/eu-west-2_Wurx6FIUd",
                        "jti": "9d2b1abb-4d44-459b-ab49-b8758f6290cd",
                        "nickname": "bart",
                        "origin_jti": "97c3fd49-7775-41b4-8489-6a2106403f0a",
                        "sub": "3672c59d-5fbc-4e5b-9e7c-19b597ff3603",
                        "token_use": "id",
                    },
                    "scopes": None,
                }
            },
            "domainName": "shorten.rtx.wtf",
            "domainPrefix": "shorten",
            "http": {
                "method": "GET",
                "path": "/users/bart/urls",
                "protocol": "HTTP/1.1",
                "sourceIp": "82.21.32.80",
                "userAgent": "insomnia/8.6.1",
            },
            "requestId": "UU5lciFZLPEEPSA=",
            "routeKey": "GET /users/{username}/urls",
            "stage": "$default",
            "time": "08/Mar/2024:20:06:20 +0000",
            "timeEpoch": 1709928380167,
        },
        "pathParameters": {"username": "bart"},
        "isBase64Encoded": False,
    }
