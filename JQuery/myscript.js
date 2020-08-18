$('h1').click(function () {
  $(this).text('I was changed!')
})

// $('input').eq(0).keypress(function () {
//   $('h3').toggleClass('turnBlue');
// })
//keypress

$('input').eq(0).keypress(function(event){
if (event.which === 13) {
  $('h3').toggleClass('turnBlue');
  }
})
//13 is the Enter key

//on() method

$('h1').on('dblclick', function () {
  $(this).toggleClass('turnBlue');
})

//When click, whole body disappear
$('input').eq(1).on('click', function () {
  $('.container').fadeOut(3000);
})

//Slidup $('.container').slideUp(3000);
