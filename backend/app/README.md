## Setup

`pip install -r requirements.txt`

You will also need to have firebase credentials in `secret.json`

## Run

`flask run`

The application will run under `localhost:5000`

## API

### Create User
Creates a user

* **URL**

  /users

* **Method:**

  `POST`

* **Data Params**

    **Required:**
 
   `username: String`

* **Success Response:**

  * **Code:** 200 OK
 
* **Error Response:**

  * **Code:** 409 CONFLICT <br/>
    **Reason:** Username exists
    
### Get User
Get user's links

* **URL**

  /users/{username}

* **Method:**

  `POST`

* **URL Params**

    **Required:**
 
   `username: String`

* **Success Response:**

  * **Code:** 200 OK <br/>
  **Content** `{shirts: [imageUrls], pants: [imageUrls]}`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br/>
    **Reason:** User with given username does not exist
    
### Add Pants
Add a pants image to user's pants list 

* **URL**

  /users/{username}/pants

* **Method:**

  `POST`

* **Data Params**

    **Required:**
 
   `username: String`

* **Success Response:**

  * **Code:** 200 OK<br/>
  **Content** `imageLink`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br/>
    **Reason:** User with given username does not exist
    
### Add Pants
Add a pants image to user's pants list 

* **URL**

  /users/{username}/shirts

* **Method:**

  `POST`

* **Data Params**

    **Required:**
 
   `username: String`
   
   `{key: "file", value: file}` as form-data

* **Success Response:**

  * **Code:** 200 OK<br/>
  **Content** `imageLink`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br/>
    **Reason:** User with given username does not exist