const getAllBtn = document.querySelector('#get-all-btn')
const getRandomBtn = document.querySelector('#get-random-btn')
const searchDescripBtn = document.querySelector('#search-descrip-btn')
const searchTagsBtn = document.querySelector('#search-tags-btn')
const searchTagsPartialBtn = document.querySelector('#search-tags-partial-btn')
const searchTagsListBtn = document.querySelector('#search-tags-list-btn')
const searchTagsListAllBtn = document.querySelector('#search-tags-list-all-btn')
const toggleFilterBtn = document.querySelector('#toggle-filters')
const filterOptions = document.querySelector('.filter-options')
const filterStart = document.querySelector('#start-date')
const filterEnd = document.querySelector('#end-date')
const filterMin = document.querySelector('#min-length')
const filterMax = document.querySelector('#max-length')

function getFilterParams(){
  const params = {
    start_date: filterStart.value,
    end_date: filterEnd.value,
    max_length:filterMax.value,
    min_length:filterMin.value
  }
  paramsArray = []

  for (const [key, value] of Object.entries(params)){
    if (value.length){
      paramsArray.push(`&${key}=${value}`)
    }
  }
  return paramsArray.join('')

}


getAllBtn.addEventListener('click', () => {
  const filterParams = getFilterParams()
  const params = `?${filterParams.slice(1)}`
  const url = `/links${params}`
  console.log(url)
  fetch(url)
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
    const filterParams = getFilterParams()
    const params = `?${filterParams.slice(1)}`
    const url = `/links/random${params}`
    console.log(url)
    fetch(url)
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
    const filterParams = getFilterParams()
    const searchUrl = `/links/search?term=${encodeURIComponent(searchTerm)}${filterParams}`
    console.log(searchUrl)

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
    const filterParams = getFilterParams()
    const searchUrl = `/links/search_by_tag?tag=${encodeURIComponent(searchTerm)}${filterParams}`
    console.log(searchUrl)
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


searchTagsPartialBtn.addEventListener('click', () => {
    const searchTerm = document.querySelector('#search-tags-partial-input').value;
    const filterParams = getFilterParams()
    const searchUrl = `/links/search_by_tag_partial?term=${encodeURIComponent(searchTerm)}${filterParams}`
    console.log(searchUrl)
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


searchTagsListBtn.addEventListener('click', () => {
    const searchTerm = document.querySelector('#search-tags-list-input').value;
    const filterParams = getFilterParams()
    const searchUrl = `/links/search_by_tags_list?tags=${encodeURIComponent(searchTerm)}${filterParams}`
    console.log(searchUrl)
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


searchTagsListAllBtn.addEventListener('click', () => {
    const searchTerm = document.querySelector('#search-tags-list-all-input').value;
    const filterParams = getFilterParams()
    const searchUrl = `/links/search_by_tags_list_all?tags=${encodeURIComponent(searchTerm)}${filterParams}`
    console.log(searchUrl)
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


toggleFilterBtn.addEventListener('click', e => {
  filterOptions.classList.toggle('hidden')
  }
)