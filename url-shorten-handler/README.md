# Shorten API
Url shortening service for the rtx.wtf platform.

### API Routes
```
GET /{shortuuid+} Redirect to original URL

POST /urls Create a new shortened URL
GET /urls Redirect to original URL by ID
DELETE /urls Delete a shortened URL
OPTIONS /urls Request options for shortened URLs

GET /users/{username+}/urls Get all URLs for a user
```

