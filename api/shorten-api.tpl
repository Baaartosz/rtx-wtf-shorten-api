{
  "openapi": "3.0.1",
  "info": {
    "title": "rtx-wtf-shorten-api",
    "description": "API for managing shortened URLs on rtx.wtf shortening platform",
    "version": "2024-08-03",
    "contact": {
      "name": "Bartosz Perczynski",
      "url": "https://shorten.rtx.wtf/"
    }
  },
  "paths": {
    "/{id+}": {
      "get": {
        "summary": "Redirect to original URL",
        "responses": {
          "302": {
            "description": "Found shortened url. Redirecting."
          },
          "404": {
            "description": "Shortened URL not found."
          }
        },
        "parameters": [
          {
            "name": "id+",
            "in": "path",
            "description": "Path parameter to include shortened url identifier",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "x-amazon-apigateway-integration": {
          "payloadFormatVersion": "2.0",
          "type": "aws_proxy",
          "httpMethod": "POST",
          "uri": "${shorten_service_lambda}",
          "connectionType": "INTERNET"
        }
      }
    },
    "/urls/{id+}": {
      "get": {
        "summary": "Redirect to original URL by ID",
        "responses": {
          "302": {
            "description": "Found original URL. Redirecting."
          },
          "404": {
            "description": "URL ID not found."
          },
          "default": {
            "description": "Default response for GET /urls"
          }
        },
        "parameters": [
          {
            "name": "id+",
            "in": "path",
            "description": "Path parameter to include shortened url identifier",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "x-amazon-apigateway-integration": {
          "payloadFormatVersion": "2.0",
          "type": "aws_proxy",
          "httpMethod": "POST",
          "uri": "${shorten_service_lambda}",
          "connectionType": "INTERNET"
        }
      },
      "delete": {
        "summary": "Delete a shortened URL",
        "responses": {
          "204": {
            "description": "URL deleted successfully."
          }
        },
        "parameters": [
          {
            "name": "id+",
            "in": "path",
            "description": "Path parameter to include shortened url identifier",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "security": [
          {
            "jwt-authorizer": []
          }
        ],
        "x-amazon-apigateway-integration": {
          "payloadFormatVersion": "2.0",
          "type": "aws_proxy",
          "httpMethod": "POST",
          "uri": "${shorten_service_lambda}",
          "connectionType": "INTERNET"
        }
      }
    },
    "/urls": {
      "post": {
        "summary": "Create a new shortened URL",
        "responses": {
          "201": {
            "description": "URL created successfully."
          },
          "403": {
            "description": "Unauthorised"
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
          "uri": "${shorten_service_lambda}",
          "connectionType": "INTERNET"
        }
      },
      "options": {
        "summary": "Request options for shortened URLs",
        "responses": {
          "default": {
            "description": "Default response for OPTIONS /urls"
          }
        },
        "x-amazon-apigateway-integration": {
          "payloadFormatVersion": "2.0",
          "type": "aws_proxy",
          "httpMethod": "POST",
          "uri": "${shorten_service_lambda}",
          "connectionType": "INTERNET"
        }
      }
    },
    "/users/{username}/urls": {
      "get": {
        "summary": "Get all URLs for a user",
        "responses": {
          "200": {
            "description": "URLs retrieved successfully."
          },
          "204": {
            "description": "No URLs found"
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
          "uri": "${shorten_service_lambda}",
          "connectionType": "INTERNET"
        }
      },
      "options": {
        "summary": "Request options for shortened URLs",
        "responses": {
          "default": {
            "description": "Default response for OPTIONS /urls"
          }
        },
        "x-amazon-apigateway-integration": {
          "payloadFormatVersion": "2.0",
          "type": "aws_proxy",
          "httpMethod": "POST",
          "uri": "${shorten_service_lambda}",
          "connectionType": "INTERNET"
        }
      },
      "parameters": [
        {
          "name": "username",
          "in": "path",
          "description": "Username parameter",
          "required": true,
          "schema": {
            "type": "string"
          }
        }
      ]
    },
    "/stats/{id+}": {
      "get": {
        "summary": "Get stats on a specific URL for an authenticated user",
        "responses": {
          "200": {
            "description": "Statistics retrieved successfully."
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
          "uri": "${shorten_service_lambda}",
          "connectionType": "INTERNET"
        }
      },
      "parameters": [
        {
          "name": "id+",
          "in": "path",
          "description": "id for stats",
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
    },
    "x-amazon-apigateway-importexport-version": "1.0"
  }
}