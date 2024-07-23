umtexto="Um dois três quatro cinco"
indices="0123456789012345678901234"
negativ="5432109876543210987654321"
print(umtexto)
print(indices)
print(umtexto[3:12])
print('Um detalhe importante sobre o intervalo do slice é que limite superior não é incluido')
print(umtexto[13:25])
print('A omisão do primeiro número antes dos 2 pontos indica que deve considerar desde o início da string.')
print(umtexto[:12])
print('A omissão do segundo núimero depois dos 2 pontos indica que deve considerar até o final da string.')
print(umtexto[3:])
print('O índice negativo indica que a contagem inicia a partir do final da string e regra é sempre o número menor primeiro e depois o maior.')
print(umtexto[-12:-6])