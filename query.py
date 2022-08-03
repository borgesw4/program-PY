nomeFunc = input("Digite o nome do funcionário:........")
sexoFunc = input("Digite (F)eminino ou (M)asculino:....")
idadFunc = int("Qual a idade do funcionário:...........")
qtdFilho = int("Quantos filhos possui:.................")
salAtual = float("Digite o salario atual:..............")
tempFunc = int("Digite o tempo de casa do funcionário: ")

print ("...............................................")
print (" {} tem {} anos de idade e é funcionário da empresa há {} ano(s)." .format (nomeFunc, idadeFunc, tempFunc))

if tempFunc <=2:
  reajuste = salAtual * 0.10
  bonus = qtdFilho * 100
elif tempFunc >2 and tempFunc <=5:
  reajuste = salAtual * 0.07
  bonus = qtdFilho * 200
else:
  reajuste = saAtual * 0.05
  bonus = qtdFilho * 300
print ("receberá um bônus mensal de R$ {:.2f} por ter {} filho(s)." .format (bonus, qtdFilho))

if tempFunc <=2:
  reajuste =salAtual * 0.10
  bonus = qtdFilho * 100
  if tempFunc <=1:
    premio = "+ 10 dias de férias"
  else:
    premio = "+ 15 dias de férias"
elif tempFunc > 2 tempFunc <=5:
  reajuste = salAtual * 0.07
  bonus = qtdFilho * 200
  if idadeFunc >=60:
    premio = "plano de saúde gratuito"
  else:
    premio = "plano odontológico"
else:
  reajuste = salAtual * 0.50
  bonus = qtdFilho * 300
  if sexoFunc == "F" or sexoFunc "f":
    premio = "1 dia no Spa"
  else:
    premio = "almoço em churrascaria"

salNovo = salAtual + reajuste
print ("salario atual de R$ {:.2f} foi reajustado para RS {:.2f}" .format (salAtual, salNovo))
salPagar = salNovo + bonus
print ("Total de salario que {} irá receber é de R$ {:.2f}." .format (nomeFunc, salPagar))
print ("o premio a ser recebido é {}!" .format (premio))
print ("...............................................")
