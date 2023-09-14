const getAllBtn = document.querySelector('#get-all-btn')
const getRandomBtn = document.querySelector('#get-random-btn')
const searchDescripBtn = document.querySelector('#search-descrip-btn')
const searchTagsBtn = document.querySelector('#search-tags-btn')
const searchTagsPartialBtn = document.querySelector('#search-tags-partial-btn')
const searchTagsListBtn = document.querySelector('#search-tags-list-btn')
const searchTagsListAllBtn = document.querySelector('#search-tags-list-all-btn')

const getAllQuoteBtn = document.querySelector('#get-all-quote-btn')
const getRandomQuoteBtn = document.querySelector('#get-random-quote-btn')

const toggleFilterBtn = document.querySelector('#toggle-filters')
const filterOptions = document.querySelector('.filter-options')
const filterStart = document.querySelector('#start-date')
const filterEnd = document.querySelector('#end-date')
const filterMin = document.querySelector('#min-length')
const filterMax = document.querySelector('#max-length')
const clearFiltersBtn = document.querySelector('#clear-filters')

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


getAllBtn.addEventListener('click', (event) => {
  const filterParams = getFilterParams()
  const params = `?${filterParams.slice(1)}`
  const url = `/links${params}`
  console.log(url)
  const displayId = event.currentTarget.getAttribute('data-result-id')
  const displayElement = document.getElementById(displayId)

  fetchAndDisplay(url, displayElement)
})


getRandomBtn.addEventListener('click', (event) => {
    const filterParams = getFilterParams()
    const params = `?${filterParams.slice(1)}`
    const url = `/links/random${params}`
    console.log(url)
    const displayId = event.currentTarget.getAttribute('data-result-id')
    const displayElement = document.getElementById(displayId)

    fetchAndDisplay(url, displayElement)

})


searchDescripBtn.addEventListener('click', (event) => {
    const searchTerm = document.querySelector('#search-descrip-input').value
    const filterParams = getFilterParams()
    const url = `/links/search?term=${encodeURIComponent(searchTerm)}${filterParams}`
    console.log(url)
    const displayId = event.currentTarget.getAttribute('data-result-id')
    const displayElement = document.getElementById(displayId)

    fetchAndDisplay(url, displayElement)
})


searchTagsBtn.addEventListener('click', (event) => {
    const searchTerm = document.querySelector('#search-tags-input').value;
    const filterParams = getFilterParams()
    const url = `/links/search_by_tag?tag=${encodeURIComponent(searchTerm)}${filterParams}`
    console.log(url)
    const displayId = event.currentTarget.getAttribute('data-result-id')
    const displayElement = document.getElementById(displayId)

    fetchAndDisplay(url, displayElement)
})


// searchTagsPartialBtn.addEventListener('click', (event) => {
//     const searchTerm = document.querySelector('#search-tags-partial-input').value;
//     const filterParams = getFilterParams()
//     const url = `/links/search_by_tag_partial?term=${encodeURIComponent(searchTerm)}${filterParams}`
//     console.log(url)
//     const displayId = event.currentTarget.getAttribute('data-result-id')
//     const displayElement = document.getElementById(displayId)

//     fetchAndDisplay(url, displayElement)
// })


searchTagsListBtn.addEventListener('click', (event) => {
    const searchTerm = document.querySelector('#search-tags-list-input').value;
    const filterParams = getFilterParams()
    const url = `/links/search_by_tags_list?tags=${encodeURIComponent(searchTerm)}${filterParams}`
    console.log(url)
    const displayId = event.currentTarget.getAttribute('data-result-id')
    const displayElement = document.getElementById(displayId)

    fetchAndDisplay(url, displayElement)
})


searchTagsListAllBtn.addEventListener('click', (event) => {
    const searchTerm = document.querySelector('#search-tags-list-all-input').value;
    const filterParams = getFilterParams()
    const url = `/links/search_by_tags_list_all?tags=${encodeURIComponent(searchTerm)}${filterParams}`
    console.log(url)
    const displayId = event.currentTarget.getAttribute('data-result-id')
    const displayElement = document.getElementById(displayId)

    fetchAndDisplay(url, displayElement)
})

// Quote endpoints

getAllQuoteBtn.addEventListener('click', (event) => {
  const filterParams = getFilterParams()
  const params = `?${filterParams.slice(1)}`
  const url = `/quotes${params}`
  console.log(url)
  const displayId = event.currentTarget.getAttribute('data-result-id')
  const displayElement = document.getElementById(displayId)

  fetchAndDisplay(url, displayElement)
})


getRandomQuoteBtn.addEventListener('click', (event) => {
    const filterParams = getFilterParams()
    const params = `?${filterParams.slice(1)}`
    const url = `/quotes/random${params}`
    console.log(url)
    const displayId = event.currentTarget.getAttribute('data-result-id')
    const displayElement = document.getElementById(displayId)

    fetchAndDisplay(url, displayElement)

})



toggleFilterBtn.addEventListener('click', () => {
  filterOptions.classList.toggle('hidden')
  }
)

clearFiltersBtn.addEventListener('click', () => {
    filterStart.value = ''
    filterEnd.value = ''
    filterMin.value = ''
    filterMax.value = ''
})

function fetchAndDisplay(url, displayElement){

  // removing the link count if still visible
  let lastElement = displayElement.parentNode.lastElementChild
  if(lastElement.classList.contains( 'count')) lastElement.innerText = ''

  fetch(url)
  .then(response => response.json())
  .then(data => {
    console.log(data)
    if (!data.length) {
      displayElement.innerText = "  Sorry, no matches"
    }else{
          displayElement.innerText = JSON.stringify(data, null, 2)
    }
    displayElement.classList.remove('hidden')

    const count = document.createElement('span')
    count.classList.add('count')
    count.innerText = `${data.length} ${data.length>1? 'results' : 'result'} found`
    displayElement.parentNode.appendChild(count)
    
    const clearBtn = document.createElement('button')
    clearBtn.innerText = 'Hide'
    clearBtn.classList.add('clear-btn')
    clearBtn.addEventListener('click', event => {
      displayElement.classList.add('hidden')
      count.innerText = ''
    })
    displayElement.appendChild(clearBtn)
  })
  .catch(error => {
    console.error("Error fetching all links:", error)
  });
}