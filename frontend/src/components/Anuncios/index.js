import './index.css';
import { useEffect, useState } from 'react';
import axios from 'axios';

function Anuncios() {
  const [anuncios, setAnuncios] = useState([]);

  useEffect(() => {
      axios.get('http://localhost:8000/api/anuncios')
      .then((response) => {
        console.log(response.data);
        const shuffle = (lista) => {
          return lista.sort(() => Math.random() - 0.5); 
        };
        const lista_anuncios = response.data;
        const anuncios = shuffle(lista_anuncios);
        console.log(anuncios);
        const tres_primeiros = [];
        if(anuncios[0] !== undefined){
          tres_primeiros.push(anuncios[0]);
        }
        if(anuncios[1] !== undefined){
          tres_primeiros.push(anuncios[1]);
        }
        if(anuncios[2] !== undefined){
          tres_primeiros.push(anuncios[2]);
        }
        console.log(tres_primeiros)
        setAnuncios(tres_primeiros);
      })
    }, [])

    return (
      <div className='container'>
        {anuncios.length > 0 ? (
          anuncios.map((anuncio) => (
            <li className='card'>
              <p>{anuncio.headline}</p>
              <img className='img' src={anuncio.img} />
              <a href={anuncio.link}></a>
            </li>
          ))
        ) : (
            <p>Ainda não há anúncios</p>
         )}
      </div>
    );
}

export default Anuncios;