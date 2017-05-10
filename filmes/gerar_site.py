# -*- coding: cp1252 -*-
import webbrowser
import os
import re

# Estilos e Script para a página
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Filmes do Jonathas!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# Design da página principal
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Filmes Preferidos do Jonathas</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {conteudo_dos_filmes}
    </div>
  </body>
</html>
'''

# Adiciona um único filme ao código HTML
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''

def criar_conteudo_dos_filmes(filmes):
    content = ''
    for filme in filmes:
        # Extrai o ID do Youtube da URL
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', filme.url_do_trailer)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', filme.url_do_trailer)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Adiciona o titulo do filme com o conteúdo adicional
        content += movie_tile_content.format(
            movie_title = filme.titulo,
            poster_image_url = filme.url_da_capa,
            trailer_youtube_id = trailer_youtube_id
        )
    return content

def abrir_pagina_de_filmes(filmes):
  # Cria ou substitui o arquivo de saida
  output_file = open('filmes_preferidos_do_jonathas.html', 'w')

  # Substitui as informações dos filmes pelas informações geradas dinâmicamente na função criar_conteudo_dos_filmes.
  rendered_content = main_page_content.format(conteudo_dos_filmes = criar_conteudo_dos_filmes(filmes))

  # Arquivo de saída
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # Abre o arquivo de saída no navegador
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # Abre em uma nova aba, se possível
