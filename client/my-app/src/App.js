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
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
      <div>
        <h1>Shopping List</h1>
        <input value={input} onChange={e => setInput(e.target.value)} />
        <button style={{backgroundColor: 'green', marginLeft: '10px'}} onClick={handleAdd}>Add</button>
        <ul>
          {items.map((item, index) => (
            <li key={index}>
              {item}
              <input style={{ margin: '0 10px' }} type="checkbox" checked={checkedItems[index] || false} onChange={() => handleCheck(index)} />
              <button style={{backgroundColor: 'red'}} onClick={handleDelete}>Delete</button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;