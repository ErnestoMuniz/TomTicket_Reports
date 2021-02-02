#import needed modules
import requests, time, json
from datetime import date

#loads variables from json files
variaveis = json.load(open('variables.json', 'r'))
chaves = json.load(open('keys.json', 'r'))

#request to API
URL = 'https://api.tomticket.com/chamados/' + chaves['tt_key'] + '/1?situacao=0,1,2,3&departament_id=' + chaves['data'][variaveis['arg']]['dp_id']
page = requests.get(URL)

#json from API response
lista = page.json()

#creates time and date objects
hoje = date.today()
t = time.localtime()
hora = time.strftime("%H:%M", t)

#converts number to name of months
def mes(arg):
	if arg == 1:
		return "janeiro"
	if arg == 2:
		return "fevereiro"
	if arg == 3:
		return "março"
	if arg == 4:
		return "abril"
	if arg == 5:
		return "maio"
	if arg == 6:
		return "junho"
	if arg == 7:
		return "julho"
	if arg == 8:
		return "agosto"
	if arg == 9:
		return "setembro"
	if arg == 10:
		return "outubro"
	if arg == 11:
		return "novembro"
	if arg == 12:
		return "dezembro"

#return an emoji for the SLA of the ticket
def sla(arg):
	if arg:
		return chaves['sla_in']
	else:
		return chaves['sla_out']

#counts the tickets
def sla_count(jsonobj):
	est = 0
	for ticket in jsonobj['data']:
		if ticket['sla_deadline_cumprido']:
			pass
		else:
			est += 1
	return est

#create the waiting ticket string
waiting = ''
for item in lista['data']:
	with open('list.txt', 'r') as wmodel:
		wmodel = wmodel.read()
		if item['ultimasituacao'] == 0 or item['ultimasituacao'] == 1:
			wmodel = wmodel.replace('{sla}', sla(item['sla_deadline_cumprido']))
			wmodel = wmodel.replace('{ticket_protocol}', str(item['protocolo']))
			wmodel = wmodel.replace('{ticket_title}', item['titulo'])
			wmodel = wmodel.replace('{ticket_user}', item['atendente'])
			waiting += wmodel + '\n'

#create the in progress ticket string
progress = ''
for item in lista['data']:
	with open('list.txt', 'r') as pmodel:
		pmodel = pmodel.read()
		if item['ultimasituacao'] == 2 or item['ultimasituacao'] == 3:
			pmodel = pmodel.replace('{sla}', sla(item['sla_deadline_cumprido']))
			pmodel = pmodel.replace('{ticket_protocol}', str(item['protocolo']))
			pmodel = pmodel.replace('{ticket_title}', item['titulo'])
			pmodel = pmodel.replace('{ticket_user}', item['atendente'])
			progress += pmodel + '\n'

#creates the message string
mensagem = open('model.txt', 'r').read()
mensagem = mensagem.replace('{dp_name}', chaves['data'][variaveis['arg']]['dp_name'])
mensagem = mensagem.replace('{day}', str(hoje.day).zfill(2))
mensagem = mensagem.replace('{month_name}', mes(hoje.month))
mensagem = mensagem.replace('{time}', str(hora))
mensagem = mensagem.replace('{waiting}', waiting)
mensagem = mensagem.replace('{in_progress}', progress)
mensagem = mensagem.replace('{sla_out}', str(sla_count(lista)))
mensagem = mensagem.replace('{total_tickets}', str(lista['total_itens']))

#dumps the message into the variables json
variaveis['report'] = mensagem
with open('variables.json', 'w') as write_file:
    json.dump(variaveis, write_file)