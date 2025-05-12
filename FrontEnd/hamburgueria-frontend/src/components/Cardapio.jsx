import React, { useEffect, useState } from 'react';
import api from '../services/api';
import './Cardapio.css';

const Cardapio = () => {
  const [cardapio, setCardapio] = useState([]);

  useEffect(() => {
    const fetchCardapio = async () => {
      try {
        const response = await api.get('/api/cardapio/cardapio/');
        console.log('Dados do cardápio recebidos:', response.data);

        // Agrupar itens por categoria
        const agrupado = response.data.reduce((acc, item) => {
          const categoria = item.categoria || 'Outros'; // Use 'Outros' como fallback
          if (!acc[categoria]) acc[categoria] = [];
          acc[categoria].push(item);
          return acc;
        }, {});

        // Ordem personalizada das categorias
        const ordemCategorias = [
          'PORÇOES',
          'CLASSICOS DE CARNE',
          'CLASSICOS DE RUCULA',
          'CLASSICOS DE PICANHA',
          'CLASSICOS DE COSTELA',
          'CLASSICOS DE FRANGO',
          'CLASSICOS DE CALABRESA',
          'CLASSICOS RECHEADOS',
          'ESPECIAIS',
          'SEM CARNE',
          'EXTRAS',
          'BEBIDAS',
          'CERVEJA',
          'VINHOS',
          'PARA DEPOIS',
        ];

        // Reordenar categorias
        const cardapioOrdenado = {};
        ordemCategorias.forEach((categoria) => {
          if (agrupado[categoria]) {
            cardapioOrdenado[categoria] = agrupado[categoria];
          }
        });

        setCardapio(cardapioOrdenado);
      } catch (error) {
        console.error('Erro ao carregar o cardápio:', error);
      }
    };

    fetchCardapio();
  }, []);

  return (
    <div className="cardapio-container">
      <h1 className="cardapio-titulo">CARDÁPIO COMPLETO</h1>
      {Object.entries(cardapio).length > 0 ? (
        Object.entries(cardapio).map(([categoria, itens]) => (
          <div key={categoria} className="categoria-container">
            <h2 className="categoria-titulo">{categoria}</h2>
            <ul className="cardapio-lista">
              {itens.map((item) => (
                <li key={item.id} className="cardapio-item">
                  <div className="item-detalhes">
                    <span className="item-nome">{item.nome}</span>
                    <span className="item-preco">
                      R$ {isNaN(Number(item.preco)) ? '' : Number(item.preco).toFixed(2)}
                    </span>
                  </div>
                  {item.descricao &&
                    item.descricao.trim().toLowerCase() !== 'nan' &&
                    item.descricao.trim() !== '' && (
                      <p className="item-descricao">{item.descricao}</p>
                    )}
                </li>
              ))}
            </ul>
          </div>
        ))
      ) : (
        <p className="cardapio-carregando">Carregando cardápio...</p>
      )}
    </div>
  );
};

export default Cardapio;