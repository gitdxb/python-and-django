var myheader = document.querySelector("h1");
myheader.style.color = "red";


// Grab the link and change its URL to another website
var special = document.querySelector('#special'); //Grab the link's container
var specialA = special.querySelector('a'); // grab the smaller container where the link located
    specialA.getAttribute('href'); //grab the mtf link then change it
    specialA.setAttribute('href', 'https://google.com');

// Event listener to H1 headings
var headOne = document.querySelector('#one');
var headTwo = document.querySelector('#two');
var headThree = document.querySelector('#three');
// Change text and color of H1 - one
headOne.addEventListener('mouseover', function () {
  headOne.textContent = "Mouse currently hovering";
  headOne.style.color = 'blue';
})

headOne.addEventListener('mouseout', function(){
  headOne.textContent = 'HOVER OVER ME';
  headOne.style.color = 'red';
})

// Click and double CLICK
headTwo.addEventListener('click', function(){
  headTwo.textContent = "YOU CLICKED ME!";
  headTwo.style.color = 'blue';
})
headThree.addEventListener('dblclick', function(){
  headThree.textContent = 'NOW YOU DOUBLE CLICKED';
  headThree.style.color = 'red';
})
