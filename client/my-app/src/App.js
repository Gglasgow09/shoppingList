import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';

function App() {
  const [items, setItems] = useState([]);
  const [input, setInput] = useState('');
  const [checkedItems, setCheckedItems] = useState({}); // new state variable

  const handleAdd = () => {
    setItems([...items, input]);
    setInput('');
  };

  const handleDelete = (indexToDelete) => {
    setItems(items.filter((_, index) => index !== indexToDelete));
  };

  const handleCheck = (index) => { // new function to handle checkbox
    setCheckedItems({...checkedItems, [index]: !checkedItems[index]});
  };

  return (
    <div>
      <h1>Shopping List</h1>
      <input value={input} onChange={e => setInput(e.target.value)} />
      <button onClick={handleAdd}>Add</button>
      <ul>
      {items.map((item, index) => (
        <li key={index}>
          {item}
          <input type="checkbox" checked={checkedItems[index] || false} onChange={() => handleCheck(index)} />
          <button onClick={() => handleDelete(index)}>Delete</button>
        </li>
      ))}
      </ul>
    </div>
  );
}

export default App;