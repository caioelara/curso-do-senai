import streamlit  as st
#------------------------------------------------------------saidbar
st.sidebar.title('Esportes')
opcao=['Jogos','Noticias']
opcao=st.sidebar.selectbox('Selecione uma opçao',opcao)
#-------------------------------------------------------------principal
st.title('Esportes')


tab1, tab2, tab3, tab4 = st.tabs(['FIFA', 'NBA', 'NFL', 'MBL'])

with tab1:
    if opcao == 'Jogos':
        st.subheader('FIFA ')
        st.subheader('Paris Saint-Germain vs Internazionale')
        st.video('https://www.youtube.com/watch?v=fUhS56AF0A8')
        st.write('Na final da Champions League, o PSG venceu com uma goleada impressionante de 5 a 0. O time dominou o jogo do começo ao fim, com um ataque eficiente, muita posse de bola e uma defesa sólida. Essa vitória histórica garantiu ao PSG seu primeiro título da competição, mostrando sua força no futebol europeu.')
        st.subheader('Bahia vs São Paulo FC SP ')
        st.video('https://www.youtube.com/watch?v=_81bX65Lcp4')
        st.write('O Bahia venceu o São Paulo por 2 a 1 em uma partida emocionante. O time baiano mostrou muita garra e conseguiu marcar os gols decisivos, segurando a pressão do adversário até o fim. Com essa vitória, o Bahia conquistou um resultado importante contra um rival forte.')
    elif opcao == 'Noticias':
        st.subheader('FIFA NOTICIAS')
        st.image('brasil.png')
        st.write('Carlo Ancelotti foi oficialmente apresentado como novo técnico da Seleção Brasileira em maio de 2025, após encerrar sua vitoriosa passagem pelo Real Madrid. Ele assinou contrato até o final da Copa do Mundo de 2026, com a missão de reconduzir o Brasil ao protagonismo no futebol mundial e buscar o tão sonhado hexacampeonato.')
        st.write('O treinador italiano chegou ao Rio de Janeiro no fim de maio e já iniciou os primeiros treinamentos com o elenco. Apesar da ausência de algumas estrelas na fase inicial de preparação, como Vinícius Júnior e Marquinhos, Ancelotti demonstrou otimismo e afirmou estar motivado para liderar a seleção.')
        st.write('A contratação foi vista como uma tentativa da CBF de recuperar a identidade da equipe após uma fase turbulenta, marcada por eliminações e uma derrota expressiva para a Argentina. O presidente da entidade, Samir Xaud, destacou que Ancelotti tem o perfil ideal para unir o grupo e reacender a paixão da torcida.')
        st.write('Com vasta experiência e títulos em grandes clubes da Europa, Ancelotti representa uma aposta de alto nível para renovar o estilo de jogo da Seleção Brasileira, mantendo o talento tradicional com maior equilíbrio tático. Ele fará sua estreia nos jogos contra Equador e Paraguai pelas Eliminatórias da Copa do Mundo.')
    with tab2:
        if opcao == 'Jogos':
            st.subheader('NBA')
            st.subheader('NY Knicks vs Indiana Pacers')
            st.video('https://www.youtube.com/watch?v=k43nVp7oUic')
            st.write('No dia 31 de maio de 2025, o Indiana Pacers venceu o New York Knicks por 125 a 108 no Jogo 6 das finais da Conferência Leste, fechando a série em 4 a 2 e avançando às finais da NBA pela primeira vez desde 2000. Pascal Siakam brilhou com 31 pontos e foi eleito MVP da série. Tyrese Haliburton também se destacou com 21 pontos, sendo 11 deles no último quarto.')
            st.write('Apesar da eliminação, os Knicks fizeram uma campanha marcante, chegando à final do Leste após 25 anos. Agora, os Pacers enfrentam o Oklahoma City Thunder nas finais da NBA, em busca do título inédito.')
            st.subheader('Minnesota Timberwolves vs Oklahoma City Thunder')
            st.video('https://www.youtube.com/watch?v=jng84yQ41nI')
            st.write('Em 29 de maio de 2025, o Oklahoma City Thunder venceu o Minnesota Timberwolves por 124 a 94 no Jogo 5 das finais da Conferência Oeste, encerrando a série por 4 a 1 e garantindo vaga nas finais da NBA.')
            st.write('Shai Gilgeous-Alexander liderou com 34 pontos e foi eleito MVP da série. Chet Holmgren e Jalen Williams também se destacaram. A defesa do Thunder foi dominante, forçando 21 turnovers dos Timberwolves.')
            st.write('Agora, o Thunder enfrenta o Indiana Pacers nas finais, em busca de seu primeiro título desde 2012.')
        elif opcao == 'Noticias':
            st.subheader('NBA NOTICIAS')
            st.image('taça.png')
            st.write('As Finais da NBA 2025 começam no dia 5 de junho com um confronto inédito entre Indiana Pacers e Oklahoma City Thunder, duas franquias que buscam conquistar o primeiro título da NBA de suas histórias. A série será disputada em até sete jogos, com o Thunder tendo a vantagem do mando de quadra.')
            st.write('O Oklahoma City Thunder chega como favorito, após uma campanha impressionante na temporada regular e uma trajetória dominante nos playoffs. Liderado por Shai Gilgeous-Alexander, eleito MVP da temporada, o time também conta com jovens talentos como Jalen Williams e Chet Holmgren, além de uma defesa sólida e um jogo coletivo eficiente.')
            st.write('Do outro lado, o Indiana Pacers surpreendeu ao eliminar favoritos como os Knicks e conquistar o título da Conferência Leste. Comandados por Tyrese Haliburton, um dos armadores mais criativos da liga, e pelo experiente Pascal Siakam, os Pacers chegam motivados e em grande forma para tentar fazer história.')
            st.write('A final promete uma disputa intensa entre duas equipes jovens, atléticas e com estilos de jogo agressivos. A expectativa é alta, não só pelo título inédito em jogo, mas também pela qualidade dos elencos e o equilíbrio da série.')
            st.write('Os jogos serão transmitidos pela ESPN e ABC, e também estarão disponíveis no NBA League Pass. A torcida aguarda uma das finais mais empolgantes dos últimos anos.')
    

with tab3:
    if opcao == 'Jogos':
        st.subheader('NFL')
        st.subheader('Kansas City vs Philadelphia')
        st.video('https://www.youtube.com/watch?v=osBs-8tMqaU&t=5s')
        st.write('Philadelphia Eagles venceram o Kansas City Chiefs por 40 a 22 no Super Bowl LIX, realizado em fevereiro de 2025. O quarterback Jalen Hurts foi o MVP, com três touchdowns e um recorde de jardas corridas por um QB em Super Bowls. A defesa dos Eagles brilhou, com duas interceptações sobre Patrick Mahomes, incluindo um touchdown defensivo. Foi o segundo título de Super Bowl da história dos Eagles.')
        st.subheader('Washington vs Philadelphia')
        st.image('nfl.jfif')
        st.write('Philadelphia Eagles venceram o Washington Commanders por 55 a 23 na final da Conferência Nacional (NFC) em janeiro de 2025. Jalen Hurts brilhou com 4 touchdowns, e Saquon Barkley marcou 3. A defesa dos Eagles forçou 4 turnovers. Com essa vitória dominante, os Eagles garantiram vaga no Super Bowl LIX.')
    elif opcao == 'Noticias':
        st.subheader('NFL NOTICIAS')
        st.image('jogador.jpeg')
        st.subheader('Justin Jefferson é trocado para o New York Jets em negociação bombástica')
        st.write('Em uma das movimentações mais surpreendentes dos últimos anos na NFL, o wide receiver Justin Jefferson, estrela do Minnesota Vikings, foi trocado para o New York Jets. A troca envolve três escolhas de Draft – uma de 1ª rodada e outra de 2ª rodada em 2026, além de uma escolha de 3ª rodada em 2027 – e o wide receiver Garrett Wilson, que agora fará parte do elenco dos Vikings.')
        st.write('A chegada de Jefferson em Nova York representa um novo momento para os Jets, que buscam fortalecer seu ataque após uma temporada instável. A expectativa é que Jefferson assuma imediatamente o papel de principal alvo ofensivo, aumentando consideravelmente o poder de fogo da equipe.')
        st.write('“É uma nova fase para mim. Estou animado para jogar em um novo sistema e ajudar os Jets a lutar por grandes coisas,” disse Jefferson em sua apresentação oficial.')
        st.write('Já o Minnesota Vikings aposta em uma reestruturação a longo prazo. Com a chegada de Garrett Wilson, jovem e promissor, além das escolhas de Draft, a franquia abre espaço para uma renovação completa no elenco.')
        st.write('Essa troca já está sendo considerada uma das maiores dos últimos tempos envolvendo um wide receiver, comparável à transferência de Davante Adams para o Las Vegas Raiders em 2022. A temporada 2025 promete, e os olhos agora se voltam para como Jefferson se encaixará no ataque dos Jets.')
    
with tab4:
    if opcao == 'Jogos':
        st.subheader('MLB')
        st.subheader('LA Dodgers vs Chicago Cubs')
        st.video('https://www.youtube.com/watch?v=plF6vq-FWPs')
        st.write('Los Angeles Dodgers e Chicago Cubs se enfrentaram no Tokyo Dome em março de 2025, na abertura da temporada da MLB. O jogo marcou o retorno de Shohei Ohtani ao Japão, agora jogando pelos Dodgers, e teve grande apoio para o também japonês Seiya Suzuki, dos Cubs. Em um confronto equilibrado, os Cubs venceram por 5 a 4, com um home run decisivo de Christopher Morel. A partida foi histórica e celebrou o retorno da MLB ao Japão após seis anos.')
        st.subheader('New York Mets vs LA Dodgers')
        st.video('https://www.youtube.com/watch?v=bv0dWSY5-PE')
        st.write('No emocionante jogo de 2 de junho de 2025, o New York Mets enfrentaram o Los Angeles Dodgers em uma partida cheia de tensão e reviravoltas. O destaque foi o pitcher dos Mets, Paul Blackburn, que, em sua estreia na temporada, conseguiu dominar o forte lineup dos Dodgers, eliminando inclusive Shohei Ohtani duas vezes. Apesar disso, Ohtani não desistiu e conseguiu empatar o jogo com um home run contra o bullpen dos Mets. A partida seguiu equilibrada até as entradas extras, quando os Mets garantiram a vitória por 4 a 3, mostrando força e resistência para superar uma das equipes mais competitivas da Liga Nacional.')
    elif opcao == 'Noticias':
        st.subheader('MBL NOTICIAS')
        st.image('mbl.jpg')
        st.subheader('Shohei Ohtani brilha na MLB Tokyo Series 2025 com vitória dos Dodgers sobre os Cubs')
        st.write('A temporada 2025 da MLB começou de forma histórica com a realização da Tokyo Series, disputada no Tokyo Dome, no Japão. Os Los Angeles Dodgers enfrentaram os Chicago Cubs em uma série de dois jogos que atraiu uma multidão entusiasmada e marcou o retorno da liga americana ao país após seis anos.')
        st.write('Os Dodgers saíram vitoriosos em ambas as partidas, vencendo o primeiro jogo por 4 a 1 e o segundo por 6 a 3. O grande destaque foi o astro japonês Shohei Ohtani, que teve atuações impressionantes em ambos os confrontos. No primeiro jogo, Ohtani conseguiu duas rebatidas e impulsionou duas corridas, enquanto no segundo fez um home run que ajudou a consolidar a vitória da sua equipe.')
        st.write('Além de Ohtani, outros jogadores japoneses também chamaram a atenção. O arremessador Yoshinobu Yamamoto, dos Dodgers, foi responsável pela vitória no primeiro jogo, enquanto o arremessador Shota Imanaga, dos Cubs, teve uma performance sólida ao lançar quatro entradas sem ceder corridas.')
        st.write('A série também marcou a estreia de Roki Sasaki, jovem promessa japonesa dos Dodgers, que impressionou os torcedores com seu talento e potencial.')
        st.write('A MLB Tokyo Series 2025 não só celebrou o início da temporada como também reforçou a forte conexão entre o beisebol americano e japonês, demonstrando o impacto global e a paixão pelo esporte.')



