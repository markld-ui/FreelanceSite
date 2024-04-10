import logo from './logo.svg';
import Reac, {useState, useEffect} from 'react';
import './App.css';

function App() {
  const [initialData, setInitialData] = useState([{}])


  useEffect(() => {
    fetch('/index').then(
      response=> response.json()
    ).then(data => setInitialData(data))
  }, []);

  return (
    <div className="App">
    </div>
  );
}

export default App;
