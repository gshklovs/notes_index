import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import IndexNotesForm from './IndexNotesForm'
import { describe, it, expect, vi } from 'vitest'

describe('IndexNotesForm', () => {
  it('submits text to backend', async () => {
    const fetchMock = vi.spyOn(window, 'fetch').mockResolvedValue({
      json: async () => ({ status: 'success', counts: { documents: 1, paragraphs: 1, sentences: 1 } })
    })
    render(<IndexNotesForm />)
    const textbox = screen.getByLabelText('notes-input')
    fireEvent.change(textbox, { target: { value: 'Test note' } })
    fireEvent.click(screen.getByRole('button', { name: /index notes/i }))
    expect(fetchMock).toHaveBeenCalledTimes(1)
    expect(fetchMock.mock.calls[0][0]).toBe('/api/index')
    await waitFor(() => {
      expect(screen.getByText('Indexing complete!')).toBeInTheDocument()
    })
    fetchMock.mockRestore()
  })
})
