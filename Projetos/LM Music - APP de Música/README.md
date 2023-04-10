# __LM Music__

### App de música
Uma das formas mais populares de se escutar música atualmente possivelmente é através de aplicativos de streaming.

Estes aplicativos se comunicam com bancos de dados contendo bibliotecas muito vastas de álbuns dos mais diversos artistas e gêneros.

Um diferencial desses aplicativos costuma ser a possibilidade do usuário criar playlists: o usuário pode buscar por músicas de diferentes artistas, salvá-las em uma ordem específica e ouvi-las sempre que quiser.

Vamos fazer um programa simulando um aplicativo de streaming. Ele terá uma base de dados de músicas, artistas, álbuns e playlists. Um administrador poderá salvar novos artistas, músicas e álbuns, enquanto um usuário comum poderá criar playlists.

Segue uma breve descrição do que será feito.

#### 1. Fluxos
Ao abrir o programa, ele deverá oferecer um menu com exatamente 3 opções: logar como usuário, logar como administrador ou sair.

Não se preocupe com criar um sistema real de login ou senha no momento, apenas valide a opção digitada e siga para o próximo menu.

###### __1.1. Admin__
O menu de admin oferecerá 2 opções:

Registrar artista
Registrar álbum
Sair
No primeiro caso, o admin irá digitar o nome de um novo artista. Caso o nome ainda não exista na base, ele será criado. Caso contrário, erro.

No segundo caso, o admin deverá digitar primeiramente o artista - o artista precisa já existir. Em seguida o programa perguntará quantas músicas teremos e irá perguntar as informações de cada uma, uma por uma. O álbum deverá ser criado, e a estrutura do artista deve ser atualizada para contabilizar o álbum novo.

###### __1.2. Usuário__
O menu de usuário também oferecerá 2 opções:

Buscar playlist
Criar playlist
Sair
Caso o usuário opte por buscar uma playlist, mais um menu será exibido:

Buscar por música
Buscar por artista
Buscar por nome
Caso o usuário escolha a primeira opção, peça para ele digitar uma música e exiba todas as playlists contendo músicas com aquele nome. Adote um procedimento análogo para a busca de artista, e por fim, na última opção, apenas o nome da playlist será considerado. Se a playlist for encontrada, as informações completas dela deverão ser exibidas (todas as informações sobre todas as músicas da mesma).

Caso o usuário opte por criar uma playlist, ele deverá primeiro digitar seu nome. Em seguida, deverá oferecer em loop para o usuário buscar - necessariamente nessa ordem - o artista, o álbum e a música. Sendo encontrada, a música será adicionada à playlist. Se em qualquer um dos níveis não for encontrado, informe o erro e torne a perguntar o artista. Quando o usuário sinalizar que finalizou, volte para o menu inicial de usuário.

#### 2. Dados
O seu programa deverá ter persistência de dados. Isso significa que, ao fechar o programa, os dados (ex: novas playlists criadas) deverão ser salvas em um arquivo de modo que ao carregar novamente o programa, teremos os nossos dados preservados.

Você deverá utilizar necessariamente os formatos .json ou .csv - utilize aquele que você preferir. Crie 3 arquivos: um para os artistas, um para os álbuns e um para as playlists.
