# Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
# aproximado de download do arquivo usando este link (em minutos).

tamanho_do_arquivo = float(input("Tamanho do arquivo (MB): "))
velocidade_download = float(input("Velocidade da internet (Mbps): "))

tempo_segundos = tamanho_do_arquivo / (velocidade_download / 8)
tempo_minutos = tempo_segundos / 60
print('Tempo necessário para download: ', round(tempo_minutos,2), 'minutos')