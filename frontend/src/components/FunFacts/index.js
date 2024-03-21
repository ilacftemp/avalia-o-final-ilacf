import './index.css';
import { useEffect, useState } from 'react';
import axios from 'axios';

function FunFacts() {
    const [fatos, setFatos] = useState([]);

    useEffect(() => {
        pegarFatos();
    }, []);

    async function pegarFatos(){
        const response = await axios.get('http://localhost:8000/api/funfacts');
        setFatos(response.data);
    }

    const criarFato = (event) => {
        const formData = new FormData(event.target);
        const fact = formData.get('fact');
        console.log(fact);
        const data = {
            'fact': fact,
        }
        axios.post(`http://localhost:8000/api/funfacts`, data, {headers:{"Content-Type" : "application/json"}});
    }

    function deletefact(id){
        axios.delete(`http://localhost:8000/api/funfacts/${id}`, {headers:{"Content-Type" : "application/json"}});
        window.location.reload();
    }

    return (
    <div>
        <form onSubmit={criarFato}>
            <input type='text' placeholder='Add a fun fact!' name='fact'></input>
            <button type='submit'>Submit</button>
        </form>
        <div>
            {fatos.length > 0 ? (
                fatos.map((fato) => (
                    <li>
                        <p>{fato.fact}</p>
                        <button className='bin' onClick={() => deletefact(parseInt(fato.id))}><img className="binImage" src='/bin.png' /></button>
                    </li>
                ))
            ) : (
                <p>Ainda não houveram fatos adicionados</p>
            )}
        </div>
    </div> 
  );
}

export default FunFacts;