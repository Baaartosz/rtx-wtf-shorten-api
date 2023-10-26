{
  "openapi": "3.0.1",
  "info": {
    "title": "rtx-wtf-shorten-api",
    "version": "2023-08-16 15:47:17UTC"
  },
  "paths": {
    "/url": {
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
      },
      "options": {
        "responses": {
          "default": {
            "description": "Default response for OPTIONS /shorten"
          }
        },
        "x-amazon-apigateway-integration": {
          "payloadFormatVersion": "2.0",
          "type": "aws_proxy",
          "httpMethod": "OPTIONS",
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
    "/url/{proxy+}": {
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
      "delete": {
        "responses": {
          "default": {
            "description": "Default response for DELETE /url/{proxy+}"
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
  "x-amazon-apigateway-importexport-version": "1.0"
}