import { useState } from "react";
import ChunkedDisplay from "./components/ChunkedDisplay";

function IndexNotesForm() {
  const [debug, setDebug] = useState(false);
  const [text, setText] = useState("");
  const [sample, setSample] = useState("");
  const [status, setStatus] = useState("");

  const submit = async () => {
    if (!text.trim()) {
      setStatus("Please enter text");
      return;
    }
    setStatus("Indexing in progress...");
    try {
      const res = await fetch("/api/index", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });
      const data = await res.json();
      if (data.status === "success") {
        setStatus("Indexing complete!");
        setSample(data.sample);
      } else {
        setStatus("Indexing failed: " + data.message);
      }
    } catch (err) {
      setStatus("Indexing failed: " + err.message);
    }
  };

  const clearDB = async () => {
    const res = await fetch("/api/clear", {
      method: "POST",
    });
    const data = await res.json();
    if (data.status === "success") {
      setStatus("Database cleared!");
    } else {
      setStatus("Database clearing failed: " + data.message);
    }
  };

  return (
    <div>
      <h2>Index Notes</h2>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        aria-label="notes-input"
      />
      <button onClick={submit}>Index Notes</button>
      <button onClick={clearDB}>Clear DB</button>
      <button onClick={() => setDebug(!debug)}>
        {debug ? "Hide Debug" : "Show Debug"}
      </button>
      {status && <p>{status}</p>}
      {debug && sample && (
        <div>
          <h3>Debug</h3>
          <ChunkedDisplay items={sample.documents} title="Sample documents" />
          <ChunkedDisplay items={sample.paragraphs} title="Sample paragraphs" />
          <ChunkedDisplay items={sample.sentences} title="Sample sentences" />
        </div>
      )}
    </div>
  );
}

export default IndexNotesForm;
