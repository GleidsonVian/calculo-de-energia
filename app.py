def preco_energia():
    # Solicita a quantidade de kWh consumida e o tipo de instalação ao usuário
    kWh_consumida = float(input('Quantidade de kWh consumida: '))
    tipo_de_instalacao = input('Qual o tipo de instalação?\nR para Residências\nI para Indústrias\nC para Comércios\n')

    # Verifica o tipo de instalação e calcula o preço da energia elétrica com base na tabela
    if tipo_de_instalacao.upper() == 'R':  # Para residências
        if kWh_consumida <= 500:
            preco_a_pagar = kWh_consumida * 0.40
            print(f"O preço pelo fornecimento de energia elétrica vai ficar em R$ {preco_a_pagar:.2f} reais")
        else:
            preco_a_pagar = kWh_consumida * 0.65
            print(f"O preço pelo fornecimento de energia elétrica vai ficar em R$ {preco_a_pagar:.2f} reais")
    
    elif tipo_de_instalacao.upper() == 'C':  # Para comércios
        if kWh_consumida <= 1000:
            preco_a_pagar = kWh_consumida * 0.55
            print(f"O preço pelo fornecimento de energia elétrica vai ficar em R$ {preco_a_pagar:.2f} reais")
        else:
            preco_a_pagar = kWh_consumida * 0.60
            print(f"O preço pelo fornecimento de energia elétrica vai ficar em R$ {preco_a_pagar:.2f} reais")
    
    elif tipo_de_instalacao.upper() == 'I':  # Para indústrias
        if kWh_consumida <= 5000:
            preco_a_pagar = kWh_consumida * 0.55
            print(f"O preço pelo fornecimento de energia elétrica vai ficar em R$ {preco_a_pagar:.2f} reais")
        else:
            preco_a_pagar = kWh_consumida * 0.60
            print(f"O preço pelo fornecimento de energia elétrica vai ficar em R$ {preco_a_pagar:.2f} reais")
    
    else:
        # Se o tipo de instalação não for reconhecido, exibe uma mensagem de valor inválido
        print('Valor inválido')

def main():
    # Chama a função para calcular o preço da energia elétrica
    preco_energia()

main()
