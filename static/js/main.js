var slide = document.getElementById('slider');
var BackBtn = document.getElementById('BackBtn');
var NextBtn = document.getElementById('NextBtn');

var slideimages = new Array(
  "{% static 'images/pic-1.jpg' %}",
  "{% static 'images/pic-2.jpg' %}",
  "{% static 'images/pic-3.jpg' %}",
  "{% static 'images/pic-4.jpg' %}",
)

let i = 0;
NextBtn.onclick = function() {
  if (i<3) {
    slide.src = slideimages[i+1];
    i++;
  }
}

BackBtn.onclick = function() {
  if (i<3) {
    slide.src = slideimages[i-1];
    i--;
  }
}