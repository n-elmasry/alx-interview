#!/usr/bin/node
// starwars

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api';
const movieId = process.argv[2];

request(`${url}/films/${movieId}/`, (error, response, body) => {
    if (error) {
        console.error('Error fetching movie:', error);
        return;
    }
    const filmData = JSON.parse(body);
    const characterUrls = filmData.characters;

    const characterRequests = characterUrls.map(url => {
        return new Promise((resolve, reject) => {
            request(url, (charError, charResponse, charBody) => {
                if (charError) {
                    reject(charError);
                } else {
                    resolve(JSON.parse(charBody));
                }
            });
        });
    });

    Promise.all(characterRequests)
        .then(characters => {
            characters.forEach(character => {
                console.log(character.name);
            });
        })
        .catch(error => console.error('Error fetching character:', error));
});
