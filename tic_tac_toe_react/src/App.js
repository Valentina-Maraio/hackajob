import BoardGame from './BoardGame';
//import {Preview} from './Preview'
import './App.css';
import ListUsers from './ListUsers';
import MyComp from './MyComp';
import Counter from './Counter';


function App() {
  return (
    <>
    <div className="container">
    <BoardGame />
    <ListUsers users={[{firstName: 'Donald', lastName: 'Knuth'}, {firstName: 'Valentina', lastName: 'Maraio'}, { firstName: 'Ada', lastName: 'Lovelace' }]}/>
    </div>
    <MyComp/>
    <Counter />
    </>
  );
}

export default App;
