<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/BookBasket/book_basket_BE">
  </a>

  <h3 align="center">BookBasket Backend</h3>

  <p align="center">
    A backend app built with Python and Flask that consumes the Google Books API and exposes data to its associated frontend app:
    https://github.com/BookBasket/book_basket_FE
    <br />
    <br />
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Challenges](#challenges)
* [Contributors](#contributors)



<!-- ABOUT THE PROJECT -->
## About The Project

![image](https://user-images.githubusercontent.com/48839191/79525569-6df06000-8020-11ea-8265-66b021361fc5.png)

BookBasket Backend is a Flask app run in conjunction with [BookBasket Frontend](https://github.com/BookBasket/book_basket_FE). BookBasket Backend imports data from [Google Books API](https://developers.google.com/books) and exposes data to the frontend through two RESTful endpoints and one GraphQL endpoint. The app allows a user to search for a book based on specific parameters, click on a book to view that book's information, add that book to their "to read" shelf, and search for that book on Amazon.

```sh
'/search'
'/create_book'
```

The backend database stores tables for the resources of books, authors, and genres as well as joins tables for book_authors, book_genres, and book_shelves. The backend consumes the Google Books API and sends information matching a request to the frontend. The search endpoint allows a user to search for a book based on title, author, genre, and isbn. The create_book endpoint allows a user to add a book to their "to read" shelf. In doing so, a POST request is sent from the frontend to the backend and a book is created and stored to the database. When a book is created and saved to the database, the appropriate relationships between a book and its authors, genres, and shelf is also established.

[Heroku Backend](https://book-basket-be.herokuapp.com/)
[Heroku Frontend]()

### Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

Requirements
- Python 3.7.7
- PSQL 11.5

Clone Repository
```
$ git clone git@github.com:BookBasket/book_basket_BE.git
```

Create/Activate Virtual Environment
```
$ cd book_basket_BE
$ python3 -m venv env
$ source env/bin/activate
```

Install Dependencies
```
$ pip install -r requirements.txt
```

Create/Migrate Database
```
$ psql
# create database book_basket_dev;
CREATE DATABASE
# \q

$ python manage.py db upgrade
```

<!-- USAGE EXAMPLES -->
## Usage

To run both apps correctly in a local environment, cd into this backend directory, open a terminal tab, and run the command
```sh
$ python3 -m venv env
$ source env/bin/activate
$ flask run
```
and then open a new terminal tab, cd into the frontend directory and follow all instructions in the frontend app's setup, and run the command
```sh
$ npm run dev
```
The backend server must be started first to allow the frontend to properly make API calls to the backend. Both servers must be running at the same time for the app to work locally.

To interact with the GraphiQL interface: `https://book-basket-be.herokuapp.com/graphql`
To make a request to the GraphQL endpoint:

```javascript
// For a single book node
request = {
  method: 'GET',
	headers: {
	  'Content-Type': 'application/json'
	},
	body: JSON.stringify({
    "query": `{
      book(id: "Qm9va09iamVjdDo2==") {
        id
        title
        summary
        publishedDate
        isbn
        imageUrl
        genres {
          edges {
            node {
              id
              type
            }
          }
        }
        authors {
          edges {
            node {
              id
              name
            }
          }
        }
      }
    }`
	})
}
fetch(`https://book-basket-be.herokuapp.com/graphql`, request)
```
```sh
# Response
{
  "data": {
    "book": {
      "id": "Qm9va09iamVjdDo2",
      "title": "Touching the Void",
      "summary": "Joe Simpson and his climbing partner, Simon Yates, had just reached the top of a 21,000-foot peak in the Andes when disaster struck. Simpson plunged off the vertical face of an ice ledge, breaking his leg. In the hours that followed, darkness fell and a blizzard raged as Yates tried to lower his friend to safety. Finally, Yates was forced to cut the rope, moments before he would have been pulled to his own death.",
      "publishedDate": "1988",
      "isbn": "0060730552",
      "imageUrl": "https://static.metacritic.com/images/products/movies/8/53b03fab6ead4ac3160e5e633715d94b.jpg",
      "genres": {
        "edges": [
          {
            "node": {
              "id": "R2VucmVPYmplY3Q6Mg=="
              "type": "non-fiction"
            }
          },
          {
            "node": {
              "id": "R2VucmVPYmplY3Q6NA=="
              "type": "adventure"
            }
          }
        ]
      },
      "authors": {
        "edges": [
          {
            "node": {
              "id": "QXV0aG9yT2JqZWN0OjI="
              "name": "Joe Simpson"
            }
          }
        ]
      }
    }
  }
}
```

For all nodes of a single resouce, pass this `"query"` into the body.
* allBooks
* allAuthors
* allGenres
* allShelves

```javascript
{
  allBooks {
    edges {
      node {
        id
      }
    }
  }
}
```

To make a request to the search endpoint:
Valid types: `title`, `author`, `genre`, `isbn`
```javascript
fetch( `https://book-basket-be.herokuapp.com/search?type=${type}&q=${userInput}` )
```

To add a book to the user's to_read shelf
```javascript
let header = { method: "POST" };
fetch(
  `https://book-basket-be.herokuapp.com/create_book?author=${author_name}&genre=${genre_type}&title=${title}&isbn=${isbn}&published_date=${published_date}&summary=${description}&image_url=${image_url}`,
  header
)
```

To move a book from the to_read shelf to the already_read shelf:
```javascript
let header = { method: 'PATCH' };
fetch( `https://book-basket-be.herokuapp.com/switch_shelves?isbn=${isbn}`, header )
```


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/BookBasket/book_basket_BE/issues) for a list of proposed features (and known issues).


<!-- CHALLENGES -->
## Challenges

* Working in technologies we had not previously used (Python, Flask, GraphQL, Svelte)
* Communicating and working completely remotely
* Connecting the frontend and backend

<!-- NEXT STEPS -->
## Next Steps

* Research and solve the issue of [mixed content](https://developers.google.com/web/fundamentals/security/prevent-mixed-content/what-is-mixed-content)
* Improve functionality to switch a book from "to read" shelf to "already read" shelf. This works for some books but not for all, so it is not included in this iteration.
* Implement use functionality. Tables and password encryption for Users have been implemented, but no endpoint built out to utilize them.
* Utilize GraphQL mutations to modify the database

<!-- CONTRIBUTORS -->
## Contributors

* [Jomah Fangonilo](https://github/jfangonilo)
* [Madelyn Romero](https://github/madelynrr)
* [Rachel Lew](https://github/rlew421)
* [Virginia Ladd](https://github.com/vladd-png)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
