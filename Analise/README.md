# Descrição

## Pasta filters
Contém todos os arquivos de filtragem de dados. Filtros disponíveis no momento:
- filterByGenre: Retorna todos os títulos de acordo com o gênero
- filterByIntervalStartYear: Filtra todos os títulos onde a data de início (Data de lançamento) está dentro de um determinado intervalo.
- filterByRatingRange: Filtra os títulos onde a avaliação média está dentro de um determinado intervalo.
- filterDirectorsByFilm: Dado um id de um título (tconst) vai retornar os diretores desse título.
- filterWritersByFilme: Dado um id de um título (tconst) vai retornar os escritores desse título.
- getAkasByTitle: Dado um determinado título, vai retornar todos os títulos estrangeiros relacionados a ele.
- getEpisodeSeasonNumber: Dado um id de um episódio de série de TV, vai ser retornado o número da séria que ele pertence.
- getFilmByString: Dado um título original de uma obra, será retornado o objeto que o representa.
- getPersonByName: Dado o nome de uma pessoa, retorna todas as pessoas (ou uma única) que está relacionada com esse nome.
- getPrincipalsByTitle: Dado o id de um título, retorna todas as pessoas que estão relacionadas a ele (cast, crew, etc)
- getTitleById: Retorna um título dado um id (tconst).
- getTitleType: Dado um id de um título, retorna o tipo dele (série de tv, short, filme, etc)
- getEpisodesByTitle: Dado um id de um título de série televisiva, retorna todos os episódios relacionados.
- getTitleRating: Retorna a avaliação média e a quantidades de avaliações que um determinado título tem.

## Pasta insertions
Contém os códigos em python que foram utilizados para realizar manipulação dos arquivos .csv e inserção no MongoDB. 
- Para executar o insertAllEpisodes é necessário estar com o .csv dos episódios na raiz do projeto. Devido ao tamanho do arquivo, não é possível colocá-lo no GitHub. Precisando realizar o download pelo link: https://www.kaggle.com/datasets/komalkhetlani/imdb-dataset 
