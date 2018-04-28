import 'bootstrap/js/dist/modal';
/* globals $ */

const getClosest = (positions, currentPos, windowHeight) => {
  // finds the yPos of a placeholder that is closest to the current viewport.
  const diffs = positions.map(position => {
    if (position > currentPos && position < (currentPos + windowHeight)) {
      // in viewport
      return 0;
    }
    const distanceToTop = Math.abs(position - currentPos);
    const distanceToBottom = Math.abs(position - (currentPos + windowHeight));
    return Math.min(distanceToTop, distanceToBottom);
  });
  const smallest = Math.min(...diffs);
  return diffs.indexOf(smallest);
};

const animateFlying = (elem, left, top) => {
  $(elem).css({
    transform: `translate(${left}px, ${top}px)`,
    opacity: 1
  });
};

let movingTo = { left: 0, top: 0 };
const flyTo = (destination) => {
  const { left, top } = destination;
  if (movingTo.left === left && movingTo.top === top) {
    // currently flying to this destination, so don't do anything.
    return;
  }
  // a new destination! interesting...
  const ufo = $('.ufo');
  const lookLeft = left > ($(window).width() / 2);
  ufo.toggleClass('lookleft', lookLeft);
  movingTo = destination;
  animateFlying(ufo[0], left, top);
};

const moveUFO = (newPos, placeholders) => {
  const yPositions = $.map(placeholders, elem => $(elem).offset().top);
  // what is the closest placeholder to the current scrollPosition?
  const windowHeight = $(window).height();
  const closest = getClosest(yPositions, newPos, windowHeight);
  flyTo($(placeholders[closest]).offset());
};

$(() => {
  $('.readmore__button').on('click', () => {
    const scrollTop = $('header').height();
    $('html, body').animate({ scrollTop }, 800);
  });


  $(window).on('scroll', () => {
    const placeholders = $('.ufo--placeholder:visible');
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    moveUFO(scrollTop, placeholders);
  });
  window.scrollTo(0, 1);

  $('.signup').on('click', (evt) => {
    evt.preventDefault();
    const elem = $(evt.currentTarget);
    const url = elem.data('url');
    $.get(url, (response) => {
      $('#registration').modal({
        backdrop: 'static',
        keyboard: false,
        focus: true,
        show: true,
      });
      $('#registration').find('.modal-content').html(response);
      $('#div_id_give_a_talk input').trigger('change');
    });
  });

  $('body').on('submit', '#registration form', (evt) => {
    const form = evt.currentTarget;
    evt.preventDefault();
    const url = $(form).attr('action');
    $.post(url, $(form).serialize(), (response) => {
      $('#registration').find('.modal-content').html(response);
    });
  });

  $('body').on('change', '#div_id_give_a_talk input', (evt) => {
    const checked = $(evt.currentTarget).is(':checked');
    if (checked) {
      $('#div_id_talk_title').fadeIn();
    } else {
      $('#div_id_talk_title').fadeOut();
    }
  });
  $('body').on('click', '.button--done', () => {
    window.location.reload();
  });
});
