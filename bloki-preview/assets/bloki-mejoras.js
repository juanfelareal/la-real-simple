// Plan Individual: al elegir un color (o el plan), la galería salta a la foto de ese color.
(function () {
  var slides = [].slice.call(document.querySelectorAll('.gal__slide'));
  var thumbs = document.querySelectorAll('.thumbs button');
  var single = document.querySelector('.plan[data-qty="1"]');
  if (!single) return;

  function showColor(color) {
    var k = slides.findIndex(function (s) { return s.dataset.color === color; });
    if (k < 0 || !thumbs[k]) return;
    thumbs[k].click();
    thumbs[k].scrollIntoView({ block: 'nearest', inline: 'center', behavior: 'smooth' });
  }

  single.querySelectorAll('.sw button').forEach(function (b) {
    b.addEventListener('click', function () { showColor(b.dataset.color); });
  });
  single.addEventListener('click', function (e) {
    if (e.target.closest('.sw')) return;
    var on = single.querySelector('.sw button.on');
    if (on) showColor(on.dataset.color);
  });
})();
