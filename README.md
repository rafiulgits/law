# law Clinic Server

#### What and How

* ##### Database 

  PostgreSQL

* ##### Server Side Framework

  Django

* ##### API

  * REST

    For form handling 

  * Graph-QL

    For dynamic query support



***

#### Schemas

* #####  Blog Models

![](doc\models_er_update.svg)



* ##### Folder

  ![](doc\folder_update.svg)



* ##### Category Hierarchy 

  ![](doc\category_hierarchy.svg)

***

##### Understand the file structure concept (Folder-Post) schema with this graph query

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

