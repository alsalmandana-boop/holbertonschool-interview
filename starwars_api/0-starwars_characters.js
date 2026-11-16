
#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie');
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  function printCharacter (index) {
    if (index >= characters.length) {
      return;
    }

    request(characters[index], function (error, response, body) {
      if (error) {
        console.error(error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Failed to fetch character');
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);

      printCharacter(index + 1);
    });
  }

  printCharacter(0);
});

