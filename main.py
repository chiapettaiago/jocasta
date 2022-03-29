import os
import time

print("Bem-vinde. Sou a Jocasta. Estou a disposição.")
while True:
    entrada = input('Em que posso ajudar?')
    if entrada == "verificar computador":
        print("Verificando sistema Windows...")
        os.system("sfc /scannow")
        print("Verificando problemas no disco rígido...")
        os.system("chkdsk /f")
        print("Correção de problemas encerrada. Para escaneamento profundo insira verificar computador profundamente.")
    elif entrada == "verificar computador profundamente":
        print("Iniciando verificação profunda do dispositivo")
        os.system("DISM /Online /Cleanup-Image /ScanHealth")
        reparo = input("Devo executar reparo completo?")
        if reparo == "sim":
            print("Executando...")
            os.system("DISM /Online /Cleanup-Image /RestoreHealth")
            print("Reparo completo. Vou reiniciar seu computador em alguns segundos.")
            time.sleep(5)
            os.system("shutdown -r")
            print("Até logo...")
            exit()
        else:
            print("Entendido. Como quiser...")
    elif entrada == "atualizar aplicativos":
        print("Como quiser...")
        os.system("winget upgrade --all")
    else:
        print("Comando não reconhecido...")
