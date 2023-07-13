$(function () {
  $('#js-hamburger-menu, .menu_link').on('click', function () {
    $('.menu').toggleClass('open');
    $('.hamburger-menu').toggleClass('hamburger-menu--open');
  });
});