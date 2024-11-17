## Models

---
- Category
  - Name: String

- News
  - Title: String
  - Slug: String
  - Image: Image
  - Content: String
  - Category: Category
  - CreatedAt: Date
  - UpdatedAt: Date

- Comment
  - News: News
  - Name: String
  - Email: String
  - Content: String
  - Status: Boolean
  - CreatedAt: Date
