import webbrowser

class Filme():
    """Essa classe armazena informacoes sobre filmes que eu gosto."""

    def __init__(self,
                 titulo_filme,
                 sinopse_filme,
                 imagem_capa,
                 trailer_youtube):
        self.titulo = titulo_filme
        self.sinopse = sinopse_filme
        self.url_da_capa = imagem_capa
        self.url_do_trailer = trailer_youtube

    def exibir_trailer(self):
        webbrowser.open(self.url_do_trailer)
