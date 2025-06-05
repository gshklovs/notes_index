import { useState } from 'react'

function IndexNotesForm() {
  const [text, setText] = useState('')
  const [status, setStatus] = useState('')

  const submit = async () => {
    if (!text.trim()) {
      setStatus('Please enter text')
      return
    }
    setStatus('Indexing in progress...')
    try {
      const res = await fetch('/api/index', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
      })
      const data = await res.json()
      if (data.status === 'success') {
        setStatus('Indexing complete!')
      } else {
        setStatus('Indexing failed: ' + data.message)
      }
    } catch (err) {
      setStatus('Indexing failed: ' + err.message)
    }
  }

  return (
    <div>
      <h2>Index Notes</h2>
      <textarea value={text} onChange={e => setText(e.target.value)} aria-label="notes-input" />
      <button onClick={submit}>Index Notes</button>
      {status && <p>{status}</p>}
    </div>
  )
}

export default IndexNotesForm
