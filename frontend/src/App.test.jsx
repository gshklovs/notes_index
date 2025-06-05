import { render, screen } from '@testing-library/react';
import App from './App';
import { describe, it, expect } from 'vitest';

describe('App component', () => {
  it('renders Hello World', () => {
    render(<App />);
    // Check if the "Hello World" heading is present
    const headingElement = screen.getByRole('heading', { name: /Hello World/i });
    expect(headingElement).toBeInTheDocument();
  });
});
