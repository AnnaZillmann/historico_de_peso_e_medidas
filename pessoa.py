class Informacao:
    def __init__(self):
        print('Bem vindo!')
        print()
   
    def perguntas(self):
        self.nome = input('Qual o seu nome? ')
        self.idade = eval(input('Qual a sua idade? '))
        self.peso = eval(input('Qual o seu peso? '))
        self.massa = eval(input('Qual a porcentagem da sua massa magra? '))
        self.gordura = eval(input('Qual a porcentagem de gordura você tem? '))
        self.altura = eval(input('Qual a sua altura? '))
       
       
    def imc(self):
        imc = self.peso / (self.altura * self.altura) 
        print(f'Seu IMC é {imc:.2f}')  

        if imc > 40:
            print('Seu IMC está no nível de Obesidade grau III (mórbida).')
        if imc < 39.9 and imc > 35:
            print('Seu IMC está no nível de Obesidade grau II (severa).')
        if imc < 34.9 and imc > 30:
            print('Seu IMC está no nível de Obesidade grau I.')
        if imc < 29.9 and imc > 25:
            print('Seu IMC está levemente acima do peso.')
        if imc < 24.9 and imc > 18.6:
            print('Seu IMC está no peso ideal. Parabéns!')
        if imc < 18.5:
            print('Seu IMC está abaixo do peso.')

        print('Vale ressaltar que o IMC não leva em consideração o tipo físico ou a proporção de massa magra.')

    def pesagem_massa(self):
        if self.peso:
            massa_magra = (self.massa / 100) * self.peso
            print(f'O valor {self.massa}% da massa magra em kg é {massa_magra:.2f}.')

    def pesagem_gordura(self):
        if self.peso:
            massa_gorda = (self.gordura / 100) * self.peso
            print(f'O valor {self.gordura}% de gordura em kg é {massa_gorda:.2f}.')
            
        if self.gordura >= 32:
            print(f'A porcentagem {self.gordura} % está MUITO ELEVADO para sua idade.')

        if self.gordura > 30 and self.gordura < 32:
            print(f'A porcentagem {self.gordura} % está ELEVADO para sua idade.')

        if self.gordura > 21 and self.gordura < 29:
            print(f'A porcentagem {self.gordura} % está NORMAL para sua idade.')

        if self.gordura > 17 and self.gordura < 20:
            print(f'A porcentagem {self.gordura} % está BOM para sua idade')

        if self.gordura < 17:
                print(f'A porcentagem {self.gordura} % está ATLETA para sua idade')
        
    