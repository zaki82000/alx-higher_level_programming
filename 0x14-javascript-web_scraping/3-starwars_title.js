#!/usr/bin/node
const request = require('request');

request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const film = JSON.parse(body);
    console.log(film.title);
  }
});
