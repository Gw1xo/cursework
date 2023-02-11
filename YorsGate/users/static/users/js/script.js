const button = document.querySelector('button');
const form = document.querySelector('#blablabla');
const popup = document.querySelector('.popup');

button.addEventListener('click', () => {
  form.classList.add('open');
  popup.classList.add('popup_open');
});