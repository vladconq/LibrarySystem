$(document).on('click', "button", function () {
    fetch('http://127.0.0.1:8000/api/authors/' + this.innerHTML + '/books/')
        .then(function (response) {
            return response.json()
        })
        .then(function (books) {
            document.getElementById('authorInfo').style.display = 'none';

            const ul = document.getElementById('listBooks');
            ul.innerHTML = "";

            books.forEach(book => {
                const button = document.createElement("button");

                button.appendChild(document.createTextNode(book['name']));
                button.classList.add('list-group-item');
                button.classList.add('list-group-item-action');
                ul.appendChild(button);
            })
        })
});


fetch('http://127.0.0.1:8000/api/authors/')
    .then(function (response) {
        return response.json()
    })
    .then(function (authors) {
        const ul = document.getElementById('listAuthors');
        authors.forEach(author => {
            const button = document.createElement("button");

            button.appendChild(document.createTextNode(author['name']));
            button.classList.add('list-group-item');
            button.classList.add('list-group-item-action');
            ul.appendChild(button);
        })
    });







