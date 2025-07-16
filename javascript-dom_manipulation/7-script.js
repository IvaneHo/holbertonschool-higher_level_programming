fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    const ul = document.querySelector('#list_movies');
    data.results.forEach(function (film) {
      const li = document.createElement('li');
      li.textContent = film.title;
      ul.appendChild(li);
    });
  });
