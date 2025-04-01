import { createButton } from './Button';
import './header.css';

export const createHeader = ({ user, onLogout, onLogin, onCreateAccount }) => {
  const header = document.createElement('header');

  const wrapper = document.createElement('div');
  wrapper.className = 'storybook-header';

  const logo = `<h1>FashionShop</h1>`;
  wrapper.insertAdjacentHTML('afterbegin', logo);

  const account = document.createElement('div');
  if (user) {
    account.innerHTML = `<span>Привіт, <b>${user.name}</b>!</span>`;
    account.appendChild(createButton({ size: 'small', label: 'Вийти', onClick: onLogout }));
  } else {
    account.appendChild(createButton({ size: 'small', label: 'Увійти', onClick: onLogin }));
    account.appendChild(createButton({ size: 'small', label: 'Реєстрація', onClick: onCreateAccount }));
  }

  wrapper.appendChild(account);
  header.appendChild(wrapper);

  return header;
};
