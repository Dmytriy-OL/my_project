import { expect, userEvent, within } from '@storybook/test';
import { createPage } from './Page';

export default {
  title: 'Shop/Page',
  render: () => createPage(),
  parameters: { layout: 'fullscreen' },
};

export const LoggedOut = {};

export const LoggedIn = {
  play: async ({ canvasElement }) => {
    const canvas = within(canvasElement);
    const loginButton = canvas.getByRole('button', { name: /Увійти/i });
    await expect(loginButton).toBeInTheDocument();
    await userEvent.click(loginButton);
    await expect(loginButton).not.toBeInTheDocument();

    const logoutButton = canvas.getByRole('button', { name: /Вийти/i });
    await expect(logoutButton).toBeInTheDocument();
  },
};
