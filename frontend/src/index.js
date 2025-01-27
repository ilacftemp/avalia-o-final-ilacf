import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import PagFilme from './components/PagFilme';
import FunFacts from './components/FunFacts';
import Anuncios from './components/Anuncios';

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "pagfilme/:titulo",
    element: <PagFilme/>,
  },
  {
    path: "funfacts",
    element: <FunFacts />,
  },
  {
    path: "anuncios",
    element: <Anuncios />,
  },
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
