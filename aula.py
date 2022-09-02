#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import tweepy
 
# Pegando a consulta por parâmetro
 
#Autenticações
consumer_key = 'GvDlyVuSK85rhHZcEFgPZrA6U'
consumer_secret = 'js5ZHqhZqNn2llDbo3ftoHr3T4ukUF86llpAw6S72IB2sFm7jg'
access_token = '37265390-Mp1gMvVk4uOTigJ0dq8XeZ8FlR8YX72h9VWFqPs5C'
access_token_secret = 'HbdMugYjUOyDwBycygqsDI4x6CstgkZLrL8dDhkEzo6Mi'
 
#Coletando tweets
class dados(tweepy.Stream):
 
  def on_status(self, status):
    #Quando receber algum status, esta função pode manipular o objeto tweet. Exemplos:
    print(status.user.screen_name)
    print(status.text.encode('utf-8'))
    #api.create_favorite(status.id)
 
    return True
 
  def on_error(self, status_code):
      print ("Erro com o código:", status_code)
      return True # Não mata o coletor
 
  def on_timeout(self):
      print ("Tempo esgotado!")
      return True # Não mata o coletor

dado = dados (
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

try:
    dado.filter(track=["fatec", "brasil"], languages=["pt"])
except:
    print("falhou")
