{
  "openapi": "3.0.1",
  "info": {
    "title": "rtx-wtf-shorten-api",
    "version": "2023-08-16 15:47:17UTC"
  },
  "paths": {
    "/url": {
      "get": {
        "responses": {
          "default": {
            "description": "Default response for GET /shorten"
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
      "post": {
        "responses": {
          "default": {
            "description": "Default response for POST /shorten"
          }
        },
        "x-amazon-apigateway-integration": {
          "payloadFormatVersion": "2.0",
          "type": "aws_proxy",
          "httpMethod": "POST",
          "uri": "${lambda_function_uri}",
          "connectionType": "INTERNET"
        }
      }
    },
    "/url/stats": {
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
      }
    }
  },
  "x-amazon-apigateway-importexport-version": "1.0"
}