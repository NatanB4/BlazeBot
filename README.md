# BlazeBot
<div align="">
  <p> Esse é um projeto com foco em web scraping utilizando selenium e BeautifulSoup em sites dinamicos aonde eu pego as informações do site de apostas da <a href="https://blaze.com/pt/games/double" target="_blank">Blaze</a> e colocar em um algoritmo para tentar adivinhar a proxima cor e logo comunicar a pessoa por um bot no Telegram</p>
</div>

# Mais sobre o BlazeBot
<ul>
  <li>
    <h2>Todas tecnologias/bibliotecas usadas</h2>
    <ul>
      <li>
        Python - Linguagem escolhida para o projeto
      </li>
      <li>
        Selenium - Fazer o webscraping
      </li>
      <li>
        BeautifulSoup - Realizar o filtro de elementos
      </li>
      <li>
        Schedule - para automatizar de acordo com minha preferencia
      </li>
      <li>
        Telegram - enviar mensagens com um bot
      </li>
      <li>
        Webdriver firefox
      </li>
    </ul>
  </li>
  <li>
    <h2>O projeto</h2>
    <ul>
      <li>
        <h2>Imagens do processo</h2>
        <ul>
          <li>
            <h4>O começo</h4>
            <p>Primeiro ele analisa todos os elementos que precisamos, no caso aqui são os numeros ou as cores.</p>
            <img width="360" heigth="360" src="https://i.imgur.com/YFrPzIe.png" alt="numeros" />                                            
            <img width="420" heigth="420" src="https://i.imgur.com/5xmOWyS.png" alt="numeros" />                                         
          </li>
           <li>
             <h4>Verificar qual é o proximo elemento (configuração)</h4>
             <p>Confesso que adoraria fazer isso com machine-learning (e espero fazer isso no futuro, por que ainda não sei) mas eu preferi fazer por um arquivo Config.json que eu posso definir os padrões a ser observados pelo algoritmo.</p>
             <img width="500" heigth="500"  src="https://i.imgur.com/FJ1Lh4p.png" />
             <ul>
               <li>
                 Cor -> A cor a ser analizada
               </li>
               <li>
                 Vezes -> A quantidade que a Cor se repete
               </li>
               <li>
                 Jogar -> Se a cor vermelha repetiu 3x então jogar preto
               </li>
               </ul>
          </li>
          <li>
            <h4>O final</h4>
            <p>Logo depois dele passar por toda a verificação em busca de um padrão que seja coerente com a configuração ele envia a mensagem para uma pessoa que tenha telegram</p>
            <img src="https://i.imgur.com/YaybikO.png"/>
            <p>Em seguida para nossa felicidade ou pra pessoa que confiou no bot:</p>
            <img src="https://i.imgur.com/zDqYAOh.png"/>
          </li>
        </ul>
      </li>
  </li>
  </ul>



# Considerações finais
<p>Foi sem duvidas um projeto divertido de se fazer e espero que eu tenha mais chance de realizar outros do mesmo tipo.</p>
<p>(Esse site foi escolhido aleatoriamente ou seja <b>não faço apostas e nem compactuo com a ideia</b>. O projeto foi desenvolvido exclusivamente para aprendizagem.)</p>
