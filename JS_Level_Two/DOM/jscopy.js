var headTwo = document.querySelector('#two');

var ton = false;
var ton2 = false;
headTwo.addEventListener('click', function(){
    if(ton === false) {
     headTwo.textContent = "Whatever it was before you clicked it";
     headTwo.style.color = 'black';
     ton = true;
    } else {
     headTwo.textContent = "YOU CLICKED ME!";
     headTwo.style.color = 'blue';
     ton = false;
    }
})
headTwo.addEventListener('click', function(){
    if(ton === false) {
     headTwo.textContent = "Whatever it was before you clicked it";
     headTwo.style.color = 'black';
     ton2 = true;
    } else {
     headTwo.textContent = 'CLICK ME';
     headTwo.style.color = 'black';
     ton2 = false;
    }
})
