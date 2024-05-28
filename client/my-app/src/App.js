import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';

function App() {
  const [items, setItems] = useState([]);
  const [input, setInput] = useState('');

  const handleAdd = () => {
    setItems([...items, input]);
    setInput('');
  };

  return (
    <div>
      <h1>Shopping List</h1>
      <input value={input} onChange={e => setInput(e.target.value)} />
      <button onClick={handleAdd}>Add</button>
      <ul>
        {items.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;