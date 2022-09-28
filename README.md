# EvangelionAPI
I created this API to refresh my knowledge on Django and Python. My interest in Neon Genesis Evangelion inspired me to build this API.

## Endpoints
> Check out the [API](https://ngevangelion.herokuapp.com/api/evangelion) url - deployed on Heroku

|  Method | Endpoints | Response
|---|---| ---|
|GET| `/api/evangelion`| All characters, evangelions, and series data
|GET| `/api/character` | All characters data
|GET| `/api/unit` | All evangelions data
|GET| `/api/character/:id` | View character data by id
|GET| `/api/unit/:id` | View eva unit data by id

## Fetch Example
<img src="https://i.imgur.com/O27ixcW.png" width="700"><br>
* Using `axios` to fetch data from api

<img src="https://i.imgur.com/NTX0wYl.png" width="700"><br>
* Using `fetch` to fetch data from api

## Response
```json
[
  {
    "id": 1,
    "title_en": "Neon Genesis Evangelion",
    "title_jp": "新世紀エヴァンゲリオン",
    "type": "Anime television series",
    "episodes": 26,
    "genre": [
      "Apocalyptic",
      "Mecha",
      "Psychological Drama"
    ],
    "released": "October 4, 1995",
    "logo": "https://static.wikia.nocookie.net/evangelion/images/d/db/Neon_Genesis_Evangelion_Logo_transparent.png/revision/latest?cb=20200521033858",
    "characters": [{...}],
    "units": [{...}]
  }
]
```
