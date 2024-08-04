import React, {useEffect, useRef, useState} from 'react';

export function usePrevious(value) {
const ref = useRef();

useEffect(() => {
ref.current = value;
}, [value]);
return ref.current;
}

const MyComp = () => {
const [count, setCount] = useState(0);
const prevCount = useState(count);

return (
    <div>
      <div>{`Count: ${count}, Previous Count: ${prevCount}`}</div>
      <button onClick={() => setCount((c) => c + 1)}>
        Press
      </button>
    </div>
)
}

export default MyComp;