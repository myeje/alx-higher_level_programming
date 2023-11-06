$(document).ready(function () {
	$.get(
		"https://swapi-api.alx-tools.com/api/films/?format=json",
		function (data) {
			data.results.forEach(function (film) {
				$('UL#list_movies').append(...data.results.map(film => `<li>${film.title}</li>`));
			});
		}
	);
});