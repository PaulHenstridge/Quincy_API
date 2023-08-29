const getAllBtn = document.querySelector('#get-all-btn')
const getRandomBtn = document.querySelector('#get-random-btn')
const searchDescripBtn = document.querySelector('#search-descrip-btn')
const searchTagsBtn = document.querySelector('#search-tags-btn')
const searchTagsPartialBtn = document.querySelector('#search-tags-partial-btn')
const searchTagsListBtn = document.querySelector('#search-tags-list-btn')
const searchTagsListAllBtn = document.querySelector('#search-tags-list-all-btn')
const toggleFilterBtn = document.querySelector('#toggle-filters')
const filterOptions = document.querySelector('.filter-options')

getAllBtn.addEventListener('click', () => {
    fetch('/links')
      .then(response => response.json())
      .then(data => {
        console.log(data)
        // display data somewhere
      })
      .catch(error => {
        console.error("Error fetching all links:", error)
      });
})


getRandomBtn.addEventListener('click', () => {
    fetch('/links/random')
      .then(response => response.json())
      .then(data => {
        console.log(data)
        // display data somewhere
      })
      .catch(error => {
        console.error("Error fetching all links:", error)
      });
})


searchDescripBtn.addEventListener('click', () => {
    const searchTerm = document.querySelector('#search-descrip-input').value
    const searchUrl = `/links/search?term=${encodeURIComponent(searchTerm)}`

    fetch(searchUrl)
      .then(response => response.json())
      .then(data => {
        console.log(data);
        // display data somewhere
      })
      .catch(error => {
        console.error("Error fetching search results:", error)
      });
})


searchTagsBtn.addEventListener('click', () => {
    const searchTerm = document.querySelector('#search-tags-input').value;
    const searchUrl = `/links/search_by_tag?tag=${encodeURIComponent(searchTerm)}`;
    console.log(searchUrl)
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


searchTagsPartialBtn.addEventListener('click', () => {
    const searchTerm = document.querySelector('#search-tags-partial-input').value;
    const searchUrl = `/links/search_by_tag_partial?term=${encodeURIComponent(searchTerm)}`;
    console.log(searchUrl)
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


searchTagsListBtn.addEventListener('click', () => {
    const searchTerm = document.querySelector('#search-tags-list-input').value;
    const searchUrl = `/links/search_by_tags_list?tags=${encodeURIComponent(searchTerm)}`;
    console.log(searchUrl)
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


searchTagsListAllBtn.addEventListener('click', () => {
    const searchTerm = document.querySelector('#search-tags-list-all-input').value;
    const searchUrl = `/links/search_by_tags_list_all?tags=${encodeURIComponent(searchTerm)}`;
    console.log(searchUrl)
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


toggleFilterBtn.addEventListener('click', e => {
  filterOptions.classList.toggle('hidden')
  }
)