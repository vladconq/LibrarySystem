$(document).on('click', "button", function () {
    fetch('http://127.0.0.1:8000/api/shelves/' + this.innerHTML + '/shelves/')
        .then(function (response) {
            return response.json()
        })
        .then(function (shelves) {
            document.getElementById('shelfInfo').style.display = 'none';

            const ul = document.getElementById('listBooks');
            ul.innerHTML = "";

            shelves.forEach(shelf => {
                const button = document.createElement("button");

                button.appendChild(document.createTextNode(shelf['name']));
                button.classList.add('list-group-item');
                button.classList.add('list-group-item-action');
                ul.appendChild(button);
            })
        })
});


fetch('http://127.0.0.1:8000/api/shelves/')
    .then(function (response) {
        return response.json()
    })
    .then(function (shelves) {
        const ul = document.getElementById('listShelves');
        shelves.forEach(shelf => {
            const button = document.createElement("button");

            button.appendChild(document.createTextNode(shelf['name']));
            button.classList.add('list-group-item');
            button.classList.add('list-group-item-action');
            ul.appendChild(button);
        })
    });







