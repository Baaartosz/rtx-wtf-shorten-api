{
  "openapi": "3.0.1",
  "info": {
    "title": "rtx-wtf-shorten-api",
    "version": "2024-06-03 15:47:17UTC"
  },
  "paths": {
    "/url": {
      "post": {
        "responses": {
          "default": {
            "description": "Default response for POST /shorten"
          }
        },
        "security": [
          {
            "jwt-authorizer": []
          }
        ],
        "x-amazon-apigateway-integration": {
          "payloadFormatVersion": "2.0",
          "type": "aws_proxy",
          "httpMethod": "POST",
          "uri": "${lambda_function_uri}",
          "connectionType": "INTERNET"
        }
      },
      "options" : {
        "responses" : {
          "default" : {
            "description" : "Default response for OPTIONS /url"
          }
        },
        "x-amazon-apigateway-integration" : {
          "payloadFormatVersion" : "2.0",
          "type" : "aws_proxy",
          "httpMethod" : "POST",
          "uri" : "${lambda_function_uri}",
          "connectionType" : "INTERNET"
        }
      }
    },
    "/url/list": {
      "get": {
        "responses": {
          "default": {
            "description": "Default response for GET /url/list"
          }
        },
        "security": [{
           "jwt-authorizer": []
        }],
        "x-amazon-apigateway-integration": {
          "payloadFormatVersion": "2.0",
          "type": "aws_proxy",
          "httpMethod": "POST",
          "uri": "${lambda_function_uri}",
          "connectionType": "INTERNET"
        }
      }
    },
    "/{proxy+}": {
      "get": {
        "responses": {
          "default": {
            "description": "Default response for GET /url/{proxy+}"
          }
        },
        "x-amazon-apigateway-integration": {
          "payloadFormatVersion": "2.0",
          "type": "aws_proxy",
          "httpMethod": "POST",
          "uri": "${lambda_function_uri}",
          "connectionType": "INTERNET"
        }
      },
      "parameters": [
        {
          "name": "proxy+",
          "in": "path",
          "description": "Path parameter to include shortened url identifier",
          "required": true,
          "schema": {
            "type": "string"
          }
        }
      ]
    },
    "/url/stats/{proxy+}": {
      "get": {
        "responses": {
          "default": {
            "description": "Default response for GET /shorten/stats"
          }
        },
        "x-amazon-apigateway-integration": {
          "payloadFormatVersion": "2.0",
          "type": "aws_proxy",
          "httpMethod": "POST",
          "uri": "${lambda_function_uri}",
          "connectionType": "INTERNET"
        }
      },
      "parameters": [
        {
          "name": "proxy+",
          "in": "path",
          "description": "Path parameter to include shortened url identifier",
          "required": true,
          "schema": {
            "type": "string"
          }
        }
      ]
    }
  },
  "components": {
    "securitySchemes": {
      "jwt-authorizer": {
        "type": "oauth2",
        "x-amazon-apigateway-authorizer": {
          "type": "jwt",
          "identitySource": "$request.header.Authorization",
          "jwtConfiguration": {
            "audience": [
              "${client_id}"
            ],
            "issuer": "https://cognito-idp.${region}.amazonaws.com/${user_pool_id}"
          }
        }
      }
    }
  },
  "x-amazon-apigateway-importexport-version": "1.0"
}