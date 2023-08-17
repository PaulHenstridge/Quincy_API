const getAllBtn = document.querySelector('#get-all-btn')
const searchDescripBtn = document.querySelector('#search-descrip-btn')

getAllBtn.addEventListener('click', () => {
    fetch('/links')
      .then(response => response.json())
      .then(data => {
        console.log(data);
        // display data somewhere
      })
      .catch(error => {
        console.error("Error fetching all links:", error);
      });
})


searchDescripBtn.addEventListener('click', () => {
    const searchTerm = document.querySelector('#search-input').value;
    const searchUrl = `/links/search?term=${encodeURIComponent(searchTerm)}`;

    fetch(searchUrl)
      .then(response => response.json())
      .then(data => {
        console.log(data);
        // display data somewhere
      })
      .catch(error => {
        console.error("Error fetching search results:", error);
      });
})
