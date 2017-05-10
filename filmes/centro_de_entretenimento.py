import gerar_site
import midia

avatar = midia.Filme("Avatar",
                     "Um oficial é enviado para explorar as riquezas de um planeta alienígena desconhecido, mas acaba gostando mais deles.",
                     "capas/Avatar.jpg",
                     "https://www.youtube.com/watch?v=WNW9Wz7k4pM")

escola_de_rock = midia.Filme("Escola de Rock",
                             "Um guitarrista fracassado é expulso da sua banda de rock, e descobre um novo caminho ao ensinar crianças a arte do Rock n' Roll.",
                             "capas/Escola-de-rock.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

matrix = midia.Filme("Matrix",
                     "Um programador talentoso dedica a vida a descubrir o que é Matrix.",
                     "capas/Matrix.jpg",
                     "https://www.youtube.com/watch?v=vKQi3bBA1y8")

invasores = midia.Filme("Invasores",
                        "Um jovem hacker órfão quer ser reconhecido na Dark Net, e está disposta a arriscar sua liberdade para isso.",
                        "capas/Invasores.jpg",
                        "https://www.youtube.com/watch?v=ZmRTPmHUFr4")


filmes = [avatar, escola_de_rock, matrix, invasores]
gerar_site.abrir_pagina_de_filmes(filmes)
