import { createHeader } from './Header';
import './page.css';

export const createPage = () => {
  const article = document.createElement('article');

  let user = null;

  const rerenderHeader = () => {
    const wrapper = document.getElementsByTagName('article')[0];
    wrapper.replaceChild(createHeaderElement(), wrapper.firstChild);
  };

  const onLogin = () => {
    user = { name: 'Dima' };
    rerenderHeader();
  };

  const onLogout = () => {
    user = null;
    rerenderHeader();
  };

  const onCreateAccount = () => {
    user = { name: 'Dima' };
    rerenderHeader();
  };

  const createHeaderElement = () => createHeader({ onLogin, onLogout, onCreateAccount, user });

  article.appendChild(createHeaderElement());

  const section = `
    <section class="storybook-page">
      <h2>Ласкаво просимо в FashionShop</h2>
      <p>Ви можете переглянути наш асортимент, додати товари в кошик і здійснити покупку.</p>
    </section>
  `;

  article.insertAdjacentHTML('beforeend', section);

  return article;
};
