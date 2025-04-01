import { action } from '@storybook/addon-actions';
import { createButton } from './Button';

export default {
  title: 'Shop/Button',
  tags: ['autodocs'],
  render: ({ label, ...args }) => createButton({ label, ...args }),
  argTypes: {
    backgroundColor: { control: 'color' },
    label: { control: 'text' },
    onClick: { action: 'clicked' },
    primary: { control: 'boolean' },
    size: { control: { type: 'select' }, options: ['small', 'medium', 'large'] },
  },
  args: { onClick: action('clicked') },
};

export const Primary = {
  args: { primary: true, label: 'Купити' },
};

export const Secondary = {
  args: { label: 'Додати в кошик' },
};

export const Large = {
  args: { size: 'large', label: 'Замовити' },
};

export const Small = {
  args: { size: 'small', label: 'Переглянути' },
};
