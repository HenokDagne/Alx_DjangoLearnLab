## API Endpoints Documentation

### Posts

**List Posts**
```
GET /posts/
Headers: Authorization: Token <your_token>
Response:
[
	{
		"id": 1,
		"author": "username",
		"content": "Post content",
		"created_at": "2025-08-21T12:00:00Z",
		"updated_at": "2025-08-21T12:00:00Z"
	},
	...
]
```

**Create Post**
```
POST /posts/
Headers: Authorization: Token <your_token>
Body:
{
	"content": "New post content"
}
Response:
{
	"id": 2,
	"author": "username",
	"content": "New post content",
	"created_at": "2025-08-21T12:05:00Z",
	"updated_at": "2025-08-21T12:05:00Z"
}
```

**Retrieve Post**
```
GET /posts/{id}/
Headers: Authorization: Token <your_token>
Response:
{
	"id": 1,
	"author": "username",
	"content": "Post content",
	"created_at": "2025-08-21T12:00:00Z",
	"updated_at": "2025-08-21T12:00:00Z"
}
```

**Update Post**
```
PUT /posts/{id}/
Headers: Authorization: Token <your_token>
Body:
{
	"content": "Updated post content"
}
Response:
{
	"id": 1,
	"author": "username",
	"content": "Updated post content",
	"created_at": "2025-08-21T12:00:00Z",
	"updated_at": "2025-08-21T12:10:00Z"
}
```

**Delete Post**
```
DELETE /posts/{id}/
Headers: Authorization: Token <your_token>
Response: 204 No Content
```

### Comments

**List Comments**
```
GET /comments/
Headers: Authorization: Token <your_token>
Response:
[
	{
		"id": 1,
		"post": 1,
		"author": "username",
		"content": "Comment content",
		"created_at": "2025-08-21T12:15:00Z",
		"updated_at": "2025-08-21T12:15:00Z"
	},
	...
]
```

**Create Comment**
```
POST /comments/
Headers: Authorization: Token <your_token>
Body:
{
	"post": 1,
	"content": "New comment content"
}
Response:
{
	"id": 2,
	"post": 1,
	"author": "username",
	"content": "New comment content",
	"created_at": "2025-08-21T12:20:00Z",
	"updated_at": "2025-08-21T12:20:00Z"
}
```

**Retrieve Comment**
```
GET /comments/{id}/
Headers: Authorization: Token <your_token>
Response:
{
	"id": 1,
	"post": 1,
	"author": "username",
	"content": "Comment content",
	"created_at": "2025-08-21T12:15:00Z",
	"updated_at": "2025-08-21T12:15:00Z"
}
```

**Update Comment**
```
PUT /comments/{id}/
Headers: Authorization: Token <your_token>
Body:
{
	"content": "Updated comment content"
}
Response:
{
	"id": 1,
	"post": 1,
	"author": "username",
	"content": "Updated comment content",
	"created_at": "2025-08-21T12:15:00Z",
	"updated_at": "2025-08-21T12:25:00Z"
}
```

**Delete Comment**
```
DELETE /comments/{id}/
Headers: Authorization: Token <your_token>
Response: 204 No Content
```
