class JogoDaVelha:
  def __init__(self):
    self.tamanho = 3
    self.total_jogadas = 1
    self.jogador_atual = 1
    self.tabuleiro = [['-' for x in range(self.tamanho)] for y in range(self.tamanho)]

  def jogo(self):
    while True:
      res = int(input("Ola! Gostaria de jogar uma partida?\nDigite 1 para JOGAR\nDigite 2 para SAIR\n:"))
      if res == 1:
        self.iniciarPartida()
      else:
        exit(0)
  
  def iniciarPartida(self):

    while self.total_jogadas != 9:
      self.exibirJogo()
      linha = int(input("Jogador %s, faca a sua jogada em um slot vazio, digitando um numero entre 1 e 3 para selecionar a linha.\n" %self.jogador_atual))
      coluna = int(input("Jogador %s, faca a sua jogada em um slot vazio, digitando um numero entre 1 e 3 para selecionar a coluna.\n" %self.jogador_atual))
      linha = linha - 1
      coluna = coluna - 1
      self.jogar(linha, coluna)

  def exibirJogo(self):
    print(" %s | %s | %s      1 | 2 | 3" %(self.tabuleiro[0][0],self.tabuleiro[0][1],self.tabuleiro[0][2]))
    print("-----------")
    print(" %s | %s | %s      4 | 5 | 6" %(self.tabuleiro[1][0],self.tabuleiro[1][1],self.tabuleiro[1][2]))
    print("-----------")
    print(" %s | %s | %s      7 | 8 | 9\n" %(self.tabuleiro[2][0],self.tabuleiro[2][1],self.tabuleiro[2][2]))

  def jogar(self, linha=1, coluna=1):

      if self.tabuleiro[linha][coluna] == "-":
        if self.jogador_atual == 1:
          self.tabuleiro[linha][coluna] = "X"
        else:
          self.tabuleiro[linha][coluna] = "O"
        print("Jogada feita pelo jogador %s efetuada com sucesso." %(self.jogador_atual))
        temVencedor = self.verificarVencedor()
        if temVencedor:
          self.exibirJogo()
          print("Fim de jogo.")
          exit(0)
        if self.jogador_atual == 1:
          self.jogador_atual = 2
        else:
          self.jogador_atual = 1
        return True
      else:
        print("Jogada feita pelo jogador %s invalida. Tente outra posicao!" %(self.jogador_atual))
        return False
  
  def verificarVencedor(self):
    print('vetor')
    print(self.tabuleiro)
    for i in range(self.tamanho):
      if self.tabuleiro[i][0] == "X" and self.tabuleiro[i][1] == "X" and self.tabuleiro[i][2] == "X" or self.tabuleiro[i][0] == "O" and self.tabuleiro[i][1] == "O" and self.tabuleiro[i][2] == "O":
        print("Jogador %s venceu." %(self.jogador_atual))
        return True
      elif self.tabuleiro[0][i] == "X" and self.tabuleiro[1][i] == "X" and self.tabuleiro[2][i] == "X" or self.tabuleiro[0][i] == "O" and self.tabuleiro[1][i] == "O" and self.tabuleiro[2][i] == "O":
        print("Jogador %s venceu." %(self.jogador_atual))
        return True
    
    if self.tabuleiro[0][0] == "X" and self.tabuleiro[1][1] == "X" and self.tabuleiro[2][2] == "X" or self.tabuleiro[0][0] == "O" and self.tabuleiro[1][1] == "O" and self.tabuleiro[2][2] == "O":
      print("Jogador %s venceu." %(self.jogador_atual))
      return True
    elif self.tabuleiro[0][2] == "X" and self.tabuleiro[1][1] == "X" and self.tabuleiro[2][0] == "X" or self.tabuleiro[0][2] == "O" and self.tabuleiro[1][1] == "O" and self.tabuleiro[2][0] == "O":
      print("Jogador %s venceu." %(self.jogador_atual))
      return True

    return False