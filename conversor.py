import requests
import os
import time

def buscar_cotacoes():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    try:
        response = requests.get(url)
        dados = response.json()
        return {
            "USD": float(dados['USDBRL']['bid']),
            "EUR": float(dados['EURBRL']['bid']),
            "BTC": float(dados['BTCBRL']['bid'])
        }
    except:
        return None

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        limpar_tela()
        print("="*45)
        print("     💰 SISTEMA DE COTAÇÕES E CONVERSÃO 💰")
        print("="*45)
        print(" 1. Dólar (USD)")
        print(" 2. Euro (EUR)")
        print(" 3. Bitcoin (BTC)")
        print(" 4. Ver Todas as Moedas")
        print(" 5. SAIR")
        print("="*45)
        
        opcao = input("Escolha uma opção: ")

        if opcao == '5':
            print("\nEncerrando o sistema... Até logo!")
            time.sleep(1.5)
            break

        cotacoes = buscar_cotacoes()
        if not cotacoes:
            print("Erro ao buscar dados. Verifique a internet.")
            input("Pressione Enter para tentar novamente...")
            continue

        if opcao in ['1', '2', '3']:
            moedas = {"1": ("Dólar", "USD"), "2": ("Euro", "EUR"), "3": ("Bitcoin", "BTC")}
            nome, sigla = moedas[opcao]
            valor_moeda = cotacoes[sigla]

            print(f"\n✅ Valor Atual do {nome}: R$ {valor_moeda:,.2f}")
            
            # Sub-menu de conversão
            try:
                valor_input = float(input(f"Quanto em R$ você quer converter para {sigla}? "))
                resultado = valor_input / valor_moeda
                print(f"\n💰 Resultado: R$ {valor_input:.2f} equivale a {sigla} {resultado:.8f}")
            except ValueError:
                print("Valor inválido!")

        elif opcao == '4':
            print(f"\n--- QUADRO GERAL ---")
            print(f"💵 Dólar: R$ {cotacoes['USD']:.2f}")
            print(f"💶 Euro:  R$ {cotacoes['EUR']:.2f}")
            print(f"₿ BTC:   R$ {cotacoes['BTC']:,.2f}")
        
        else:
            print("\nOpção inválida!")

        input("\nPressione Enter para voltar ao menu...")

if __name__ == "__main__":
    main()