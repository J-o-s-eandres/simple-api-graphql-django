```markdown
# GraphQL API with Graphene and Django

## Overview

This is a basic GraphQL API built using Graphene and Django. It allows you to perform CRUD operations on a collection of books.

## Documentation

### Get List of Books

```graphql
# Get List of Books
{
  books {
    title
    description
    createdAt
    updatedAt
  }
}
```

### Get a Book by ID

```graphql
# Get a Book by ID
{
  book(id: 1) {
    id
    title
    description
  }
}
```

### Create a Book

```graphql
# Create a Book
mutation {
  createBook(
    title: "C++ Developer",
    description: "Libro de C++"
  ) {
    book {
      id
      title
      description
      createdAt
      updatedAt
    }
  }
}
```

### Delete a Book

```graphql
# Delete a Book
mutation {
  deleteBook(id: 3) {
    message
  }
}
```

### Update a Book

```graphql
# Update a Book
mutation {
  updateBook(
    id: 2,
    title: "Project Hadoop",
    description: "Big Data Book"
  ) {
    book {
      id
      title
      description
      createdAt
      updatedAt
    }
  }
}
```

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Django development server: `python manage.py runserver`
4. Access the GraphQL API at [http://localhost:8000/graphql/](http://localhost:8000/graphql/)

## Dependencies

- Django
- Graphene-Django

## Contributing

Feel free to contribute to improve this GraphQL API. Create a fork and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
