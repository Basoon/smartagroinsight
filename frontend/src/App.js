import React from 'react';
import DropzoneUploader from './components/DropzoneUploader';
import ChartCard from './components/ChartCard';
import headerImg from './assets/analiza-gleby.jpg';

function App() {
  return (
    <div>
      <img src={headerImg} alt="Analiza gleby" style={{ width: '100%' }} />
      <DropzoneUploader />
      <ChartCard title="Przykładowy wykres" />
    </div>
  );
}

export default App;
