// Back to top button code customised from the following link.
// https://dev.to/ljcdev/scroll-to-top-button-in-vanilla-js-beginners-2nc
// BACK TO TOP BUTTON SCRIPT

document.addEventListener("scroll", handleScroll);
// get a reference to our predefined button
var scrollToTopBtn = document.querySelector(".scrollToTopBtn");

function handleScroll() {
  var scrollableHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  var GOLDEN_RATIO = 0.5;

  if ((document.documentElement.scrollTop / scrollableHeight ) > GOLDEN_RATIO) {
    //show button
    if(!scrollToTopBtn.classList.contains("showScrollBtn"))
    scrollToTopBtn.classList.add("showScrollBtn")
  } else {
    //hide button
    if(scrollToTopBtn.classList.contains("showScrollBtn"))
    scrollToTopBtn.classList.remove("showScrollBtn")
  }
}

scrollToTopBtn.addEventListener("click", scrollToTop);

function scrollToTop() {
  window.scrollTo({
    top: 0,
    behavior: "smooth"
  });
}

// Increase and decrease the cart quantity selector
// https://javascript.tutorialink.com/changing-cart-items-quantity-in-shopping-cart-using-vanilla-javascript/
let deductBtnArr = document.getElementsByClassName('dec');
let addButtonArr = document.getElementsByClassName('inc');

for(let deductBtn of deductBtnArr){
  deductBtn.onclick = function(){
    let currentInputBox = deductBtn.nextElementSibling;
    if (currentInputBox.value > 0) {
      currentInputBox.value =  currentInputBox.value - 1;
    }
    
  }
}

for(let addButton of addButtonArr){
  addButton.onclick = () => {
    let currentInputBox = addButton.previousElementSibling;
    currentInputBox.value =  parseInt(currentInputBox.value) + 1;
    
  }
}

