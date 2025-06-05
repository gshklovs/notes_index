import { useEffect, useState } from 'react'
import IndexNotesForm from './IndexNotesForm'

function App() {
  const [message, setMessage] = useState('')

  useEffect(() => {
    fetch('/api/hello')
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch((err) => console.error(err))
  }, [])

  return (
    <>
      <h1>Hello World</h1>
      {message && <p>{message}</p>}
      <IndexNotesForm />
    </>
  )
}

export default App
