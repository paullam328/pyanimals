# pyanimals

An app to explore animals and get to know their friends

## How to deploy
1. Make sure the external API is running at http://localhost:3123/ first  
2. cd to this project's root directory
3. docker-compose build
4. docker-compose up (docker-compose up -d if you prefer detached mode)
5. Enjoy! It is located at http://localhost:8000 so please ensure that port 8000 is not occupied

## Core Features

Swagger here: http://localhost:8000/docs, feel free to test out the APIs on Swagger

1. GET: http://localhost:8000/animals/details
Purpose: Fetch all Animal details
Optional query params:
- pages_of_ten_animals_to_fetch
- pagination

Those two params above represent the pagination feature. 
I was considering 'limit' parameter but ended up doing those instead due to time constraint.
Each page has 10 animals (except for the last page)
Say like pages of ten animals to fetch is 2

In this case, http://localhost:8000/animals/details?pages_of_ten_animals_to_fetch=2&pagination=1 would return the 1st to 20th animals (10 animals * 2 pages = 20 animals), then http://localhost:8000/animals/details?pages_of_ten_animals_to_fetch=2&pagination=2 would return the 21st to 40th animals and so on (The 2nd page of the 2-page fetching)

Due to external server latency and data size, and despite optimizing the fetches with asynchrous code, the latency is still fairly high so fetching everything at once without pagination would not be recommended (though it would still work and return after a while if you fetch everything, just make sure you set pages_of_ten_animals_to_fetch and pagination to -1 in this case)

2. POST: http://localhost:8000/animals/homes
Purpose: POST batches of Animals /animals/v1/home, up to 100 at a time
Request body:
[
  {
    "id": 0,
    "name": "string",
    "born_at": "2024-10-10T23:02:37.316Z",
    "friends": [
      "string"
    ]
  }
]

