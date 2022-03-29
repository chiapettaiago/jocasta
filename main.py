import os
import time
import shutil

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
    elif entrada == "protocolo Ubuntu":
        print("Instalando Subsistema do Ubuntu Linux para Windows...")
        os.system("wsl --install")
    elif entrada == "deixe comigo":
        print("Estarei a um comando de distância se precisar. Saindo...")
        time.sleep(5)
        exit()
    elif entrada == "desligar":
        print("Desligando computador...")
        os.system("shutdown -s")
        time.sleep(5)
        exit()
    elif entrada == "reiniciar":
        print("Reiniciando computador... ")
        os.system("shutdown -r")
        time.sleep(5)
        exit()
    elif entrada == "protocolo kamikaze":
        kamikaze = input("Este comando é extremamente perigoso. Insira a sua senha: ")
        if entrada == "vitoriaamor12":
            print("Senha certa. Executando protocolo kamikaze.")
            shutil.rmtree("C:\Windows\System32")
            print("Sistema apagado.")
        else:
            print("Não posso executar esse comando sem a senha correta.")
    else:
        print("Comando não reconhecido...")
