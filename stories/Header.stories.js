import { fn } from '@storybook/test';
import { createHeader } from './Header';

export default {
  title: 'Shop/Header',
  tags: ['autodocs'],
  render: (args) => createHeader(args),
  parameters: { layout: 'fullscreen' },
  args: {
    onLogin: fn(),
    onLogout: fn(),
    onCreateAccount: fn(),
  },
};

export const LoggedIn = {
  args: { user: { name: 'Dima' } },
};

export const LoggedOut = {};
