import React, { useState } from 'react';

function Counter() {
  const [value, setValue] = useState(0);

  const increment = () => {
    setValue(prevValue => prevValue + 1);
  };

  const decrement = () => {
    setValue(prevValue => prevValue - 1);
  };

  return (
    <div>
      <p id="value">{value}</p>
      <button id="increment" onClick={increment}>+</button>
      <button id="decrement" onClick={decrement}>-</button>
    </div>
  );
}

export default Counter;
