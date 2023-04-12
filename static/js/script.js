let mybutton = document.getElementById("btn-back-to-top");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (
    document.body.scrollTop > 20 ||
    document.documentElement.scrollTop > 20
  ) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}
// When the user clicks on the button, scroll to the top of the document
mybutton.addEventListener("click", backToTop);

function backToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

// When a message shows, it will automatically disappear after three seconds

setTimeout(function () {
  let messages = document.getElementById("msg");
  let alert = new bootstrap.Alert(messages);
  alert.close();

}, 3000);


// When the update-recipe form is loaded, the fadeIn and transicion delays classes are added to the form elements
// -------------------------------------------------------------------
var title = document.getElementById('id_title');

title.classList.add('fadeIn', 'first');
// -------------------------------------------------------------------
var shortDescription = document.getElementById('id_short_description');

shortDescription.classList.add('fadeIn', 'second');
// -------------------------------------------------------------------
var ingredients = document.getElementById('id_ingredients');

ingredients.classList.add('fadeIn', 'third');
// -------------------------------------------------------------------
var instructions = document.getElementById('id_instructions');

instructions.classList.add('fadeIn', 'fourth');
// -------------------------------------------------------------------
var foodTags = document.getElementById('id_tags');

foodTags.classList.add('fadeIn', 'fifth');
// -------------------------------------------------------------------
var foodImage = document.getElementById('id_food_image');

foodImage.classList.add('fadeIn', 'sixth');
// -------------------------------------------------------------------
var labelOne = document.getElementsByTagName('label')[0];

labelOne.classList.add('fadeIn', 'first');
// -------------------------------------------------------------------
var labelTwo = document.getElementsByTagName('label')[1];

labelTwo.classList.add('fadeIn', 'second');
// -------------------------------------------------------------------
var labelThird = document.getElementsByTagName('label')[2];

labelThird.classList.add('fadeIn', 'third');
// -------------------------------------------------------------------
var labelFourth = document.getElementsByTagName('label')[3];

labelFourth.classList.add('fadeIn', 'fourth');
// -------------------------------------------------------------------
var labelFifth = document.getElementsByTagName('label')[4];

labelFifth.classList.add('fadeIn', 'fifth');
// -------------------------------------------------------------------
var labelSixth = document.getElementsByTagName('label')[5];

labelSixth.classList.add('fadeIn', 'sixth');

