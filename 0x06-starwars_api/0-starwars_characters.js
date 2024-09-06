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

    characterUrls.forEach((url) => {
        request(url, (charError, charResponse, charBody) => {
            if (charError) {
                console.error('Error fetching character:', charError);
                return;
            }
            const character = JSON.parse(charBody);
            console.log(character.name);
        });
    });
});
