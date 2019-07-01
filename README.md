# law Clinic Server

Blog Models Schema from GraphQL

```
query {
  allFolders {
    name
    distance
    category {
      name
    }
    root {
      node {
        name
      }
    }
    postSet {
      title
      body
      dateTime
    }
  }
}
```

