# Лабораторная работа 4

## API

### Users

<details>
<summary>
    <code>GET</code> <b><code>/users</code></b> Get all users
</summary>

#### Parameters
> None

#### Responses
> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `text/plain;charset=UTF-8`        | JSON-objects                                                        |
> | `401`         | `text/plain;charset=UTF-8`        | `You are not authorized`                                            |
> | `403`         | `text/plain;charset=UTF-8`        | `You don't have access rights to this content`                      |

##### Example Value
```json
[
    {
        "SNILS": "string",
        "Login": "string",
        "Email": "string",
        "HashPassword": "string",
        "Name": "string",
        "Surname": "string",
        "Patronymic": "string",
        "RoleId": 0
    }
]
```
</details>


<details>
<summary>
    <code>GET</code> <b><code>/users/{snils}</code></b> Get user by SNILS
</summary>

#### Parameters
> | name              |  type     | data type      | description                         |
> |-------------------|-----------|----------------|-------------------------------------|
> | `snils`           |  required | string         | `SNILS`                             |

#### Responses
> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `text/plain;charset=UTF-8`        | JSON-object                                                         |
> | `400`         | `text/plain;charset=UTF-8`        | `Invalid SNILS value`                                               |
> | `401`         | `text/plain;charset=UTF-8`        | `You are not authorized`                                            |
> | `403`         | `text/plain;charset=UTF-8`        | `You don't have access rights to this content`                      |
> | `404`         | `text/plain;charset=UTF-8`        | `User with such SNILS not found`                                    |

##### Example Value
```json
{
    "SNILS": "string",
    "Login": "string",
    "Email": "string",
    "HashPassword": "string",
    "Name": "string",
    "Surname": "string",
    "Patronymic": "string",
    "RoleId": 0
}
```
</details>


<details>
<summary>
    <code>POST</code> <b><code>/users</code></b> Create user
</summary>

#### Parameters
> None

#### Body
```json
{
    "SNILS": "string",
    "Login": "string",
    "Email": "string",
    "HashPassword": "string",
    "Name": "string",
    "Surname": "string",
    "Patronymic": "string",
    "RoleId": 0
}
```

#### Responses
> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `201`         | `text/plain;charset=UTF-8`        | `User created successfully`                                         |
> | `400`         | `text/plain;charset=UTF-8`        | `Invalid user info`                                                 |
> | `401`         | `text/plain;charset=UTF-8`        | `You are not authorized`                                            |
> | `403`         | `text/plain;charset=UTF-8`        | `You don't have access rights to this action`                       |
> | `409`         | `text/plain;charset=UTF-8`        | `User with such SNILS already exists`                               |
</details>


<details>
<summary>
    <code>PUT</code> <b><code>/users/{snils}</code></b> Update existing user by SNILS
</summary>

#### Parameters
> | name              |  type     | data type      | description                         |
> |-------------------|-----------|----------------|-------------------------------------|
> | `snils`           |  required | string         | `SNILS`                             |

#### Body
```json
{
    "Login": "string",
    "Email": "string",
    "HashPassword": "string",
    "Name": "string",
    "Surname": "string",
    "Patronymic": "string",
    "RoleId": 0
}
```

#### Responses
> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `text/plain;charset=UTF-8`        | `User updated successfully`                                         |
> | `400`         | `text/plain;charset=UTF-8`        | `Invalid user info`                                                 |
> | `401`         | `text/plain;charset=UTF-8`        | `You are not authorized`                                            |
> | `403`         | `text/plain;charset=UTF-8`        | `You don't have access rights to this action`                       |
> | `404`         | `text/plain;charset=UTF-8`        | `User with such SNILS not found`                                    |
</details>


<details>
<summary>
    <code>DELETE</code> <b><code>/users/{snils}</code></b> Delete user by SNILS
</summary>

#### Parameters
> | name              |  type     | data type      | description                         |
> |-------------------|-----------|----------------|-------------------------------------|
> | `snils`           |  required | string         | `SNILS`                             |

#### Responses
> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `204`         | `text/plain;charset=UTF-8`        | `User deleted successfully`                                         |
> | `400`         | `text/plain;charset=UTF-8`        | `Invalid SNILS value`                                               |
> | `401`         | `text/plain;charset=UTF-8`        | `You are not authorized`                                            |
> | `403`         | `text/plain;charset=UTF-8`        | `You don't have access rights to this action`                       |
> | `404`         | `text/plain;charset=UTF-8`        | `User with such SNILS not found`                                    |
</details>



### Tests

<details>
<summary>
    <code>GET</code> <b><code>/tests</code></b> Get all tests
</summary>

#### Parameters
> None

#### Responses
> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `text/plain;charset=UTF-8`        | JSON-objects                                                        |
> | `401`         | `text/plain;charset=UTF-8`        | `You are not authorized`                                            |
> | `403`         | `text/plain;charset=UTF-8`        | `You don't have access rights to this content`                      |

##### Example Value
```json
[
    {
        "Id": 0,
        "Name": "string",
        "CreationDate": 01/01/2000 00:00:00
    }
]
```
</details>


<details>
<summary>
    <code>GET</code> <b><code>/tests/{id}</code></b> Get test by id
</summary>

#### Parameters
> | name              |  type     | data type      | description                         |
> |-------------------|-----------|----------------|-------------------------------------|
> | `id`              |  required | int            | `Unique test id`                    |

#### Responses
> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `text/plain;charset=UTF-8`        | JSON-object                                                         |
> | `400`         | `text/plain;charset=UTF-8`        | `Invalid id`                                                        |
> | `401`         | `text/plain;charset=UTF-8`        | `You are not authorized`                                            |
> | `403`         | `text/plain;charset=UTF-8`        | `You don't have access rights to this content`                      |
> | `404`         | `text/plain;charset=UTF-8`        | `Test with such id not found`                                       |

##### Example Value
```json
{
    "Id": 0,
    "Name": "string",
    "CreationDate": 01/01/2000 00:00:00
}
```
</details>


<details>
<summary>
    <code>POST</code> <b><code>/tests</code></b> Create test
</summary>

#### Parameters
> None

#### Body
```json
{
    "Name": "string",
    "CreationDate": 01/01/2000 00:00:00
}
```

#### Responses
> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `201`         | `text/plain;charset=UTF-8`        | Id of the created test                                              |
> | `400`         | `text/plain;charset=UTF-8`        | `Invalid test info`                                                 |
> | `401`         | `text/plain;charset=UTF-8`        | `You are not authorized`                                            |
> | `403`         | `text/plain;charset=UTF-8`        | `You don't have access rights to this action`                       |
</details>


<details>
<summary>
    <code>PUT</code> <b><code>/tests/{id}</code></b> Update existing test by id
</summary>

#### Parameters
> | name              |  type     | data type      | description                         |
> |-------------------|-----------|----------------|-------------------------------------|
> | `id`              |  required | int            | `Unique test id`                    |

#### Body
```json
{
    "Name": "string",
    "CreationDate": 01/01/2000 00:00:00
}
```

#### Responses
> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `text/plain;charset=UTF-8`        | `Test updated successfully`                                         |
> | `400`         | `text/plain;charset=UTF-8`        | `Invalid test info`                                                 |
> | `401`         | `text/plain;charset=UTF-8`        | `You are not authorized`                                            |
> | `403`         | `text/plain;charset=UTF-8`        | `You don't have access rights to this action`                       |
> | `404`         | `text/plain;charset=UTF-8`        | `Test with such id not found`                                       |
</details>


<details>
<summary>
    <code>DELETE</code> <b><code>/tests/{id}</code></b> Delete test by id
</summary>

#### Parameters
> | name              |  type     | data type      | description                         |
> |-------------------|-----------|----------------|-------------------------------------|
> | `id`              |  required | int            | `Unique test id`                    |

#### Responses
> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `204`         | `text/plain;charset=UTF-8`        | `Test deleted successfully`                                         |
> | `401`         | `text/plain;charset=UTF-8`        | `You are not authorized`                                            |
> | `403`         | `text/plain;charset=UTF-8`        | `You don't have access rights to this action`                       |
> | `404`         | `text/plain;charset=UTF-8`        | `Test with such id not found`                                       |
</details>



### Test questions

<details>
<summary>
    <code>GET</code> <b><code>/testQuestions/{testId}</code></b> Get all test questions by test id
</summary>

#### Parameters
> | name              |  type     | data type      | description                         |
> |-------------------|-----------|----------------|-------------------------------------|
> | `testId`          |  required | int            | `Unique test id`                    |

#### Responses
> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `text/plain;charset=UTF-8`        | JSON-objects                                                        |
> | `401`         | `text/plain;charset=UTF-8`        | `You are not authorized`                                            |
> | `403`         | `text/plain;charset=UTF-8`        | `You don't have access rights to this content`                      |
> | `404`         | `text/plain;charset=UTF-8`        | `Test with such id not found`                                       |

##### Example Value
```json
[
    {
        "Id": 0,
        "TestId": 0,
        "Question": "string",
        "Answer": "string",
        "DetailedAnswer": false
    }
]
```
</details>


<details>
<summary>
    <code>GET</code> <b><code>/questions/{id}</code></b> Get question by id
</summary>

#### Parameters
> | name              |  type     | data type      | description                         |
> |-------------------|-----------|----------------|-------------------------------------|
> | `id`              |  required | int            | `Unique question id`                |

#### Responses
> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `text/plain;charset=UTF-8`        | JSON-object                                                         |
> | `400`         | `text/plain;charset=UTF-8`        | `Invalid id`                                                        |
> | `401`         | `text/plain;charset=UTF-8`        | `You are not authorized`                                            |
> | `403`         | `text/plain;charset=UTF-8`        | `You don't have access rights to this content`                      |
> | `404`         | `text/plain;charset=UTF-8`        | `Question with such id not found`                                   |

##### Example Value
```json
{
    "Id": 0,
    "TestId": 0,
    "Question": "string",
    "Answer": "string",
    "DetailedAnswer": false
}
```
</details>


<details>
<summary>
    <code>POST</code> <b><code>/testQuestions/{testId}</code></b> Create question for test with such id
</summary>

#### Parameters
> | name              |  type     | data type      | description                         |
> |-------------------|-----------|----------------|-------------------------------------|
> | `testId`          |  required | int            | `Unique test id`                    |

#### Body
```json
{
    "Question": "string",
    "Answer": "string",
    "DetailedAnswer": false
}
```

#### Responses
> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `201`         | `text/plain;charset=UTF-8`        | Id of the created question                                          |
> | `400`         | `text/plain;charset=UTF-8`        | `Invalid test info`                                                 |
> | `401`         | `text/plain;charset=UTF-8`        | `You are not authorized`                                            |
> | `403`         | `text/plain;charset=UTF-8`        | `You don't have access rights to this action`                       |
</details>


<details>
<summary>
    <code>PUT</code> <b><code>/questions/{id}</code></b> Update existing question by id
</summary>

#### Parameters
> | name              |  type     | data type      | description                         |
> |-------------------|-----------|----------------|-------------------------------------|
> | `id`              |  required | int            | `Unique question id`                |

#### Body
```json
{
    "TestId": 0,
    "Question": "string",
    "Answer": "string",
    "DetailedAnswer": false
}
```

#### Responses
> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `text/plain;charset=UTF-8`        | `Question updated successfully`                                     |
> | `400`         | `text/plain;charset=UTF-8`        | `Invalid question info`                                             |
> | `401`         | `text/plain;charset=UTF-8`        | `You are not authorized`                                            |
> | `403`         | `text/plain;charset=UTF-8`        | `You don't have access rights to this action`                       |
> | `404`         | `text/plain;charset=UTF-8`        | `Question with such id not found`                                   |
</details>


<details>
<summary>
    <code>DELETE</code> <b><code>/questions/{id}</code></b> Delete question by id
</summary>

#### Parameters
> | name              |  type     | data type      | description                         |
> |-------------------|-----------|----------------|-------------------------------------|
> | `id`              |  required | int            | `Unique question id`                |

#### Responses
> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `204`         | `text/plain;charset=UTF-8`        | `Question deleted successfully`                                     |
> | `401`         | `text/plain;charset=UTF-8`        | `You are not authorized`                                            |
> | `403`         | `text/plain;charset=UTF-8`        | `You don't have access rights to this action`                       |
> | `404`         | `text/plain;charset=UTF-8`        | `Question with such id not found`                                   |
</details>