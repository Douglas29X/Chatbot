from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from datetime import datetime

bot = ChatBot('TW Chat Bot')

conversa = ['Oi! Me chamo Alírio, e sou o auxiliar da Excellência Acadêmica! Você gostaria de um atendimento personalizado? Digite Sim ou Não',
            'Sim']

bot.set_trainer(ListTrainer)
bot.train(conversa)

dia_de_atendimento = (1,2,3,4,5)
hoje = datetime.today().isoweekday()

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) == "Sim" and hoje in dia_de_atendimento:
        print('Alírio: Muito bem, redirecionando para um de nossos atendentes...')
    else:
        print('Alírio: Me desculpe, mas por enquanto estamos fora do dia de atendimento. Peço que retorne em horário de serviço, ok? Até logo!')
