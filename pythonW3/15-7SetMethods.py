# Set Methods
# isdisjoint() → Retorna se tem interseção entre dois conjuntos.
tecnologias1 = {'javascript', 'SQL', 'PHP'}
tecnologias2 = {'SQL', 'React', 'Excel'}
print('tecnologias 1 → 2', tecnologias1.isdisjoint(tecnologias2)) # tecnologias 1 → 2 False
print('tecnologias 2 → 1', tecnologias2.isdisjoint(tecnologias1)) # tecnologias 2 → 1 False
# Conclusão: Imprime FALSE se tem interseção entre os dois conjuntos

nomes1 = {'Pat','Dani','Bia'}
nomes2 = {'Ana', 'Cris', 'Fla'}
print('nomes 1 → 2', nomes1.isdisjoint(nomes2)) # nomes 1 → 2 True
print('nomes 2 → 1', nomes2.isdisjoint(nomes1)) # nomes 2 → 1 True
# Conclusão: imprime TRUE se não tem interseção entre os dois conjuntos

# issubset() → Retorna se os elementos de um conjunto contém todos os elementos de outro conjunto
especialidade = {'pediatria','oftamologia','otorrinolaringologista'}
medicina = {'endocrinologia','gastroenterologia','pediatria','oftamologia','otorrinolaringologista', 'ginecologia','ortopedia'}
print('especialidade está contido em medicina? ', especialidade.issubset(medicina)) # True
print('medicina está contido em especialidades? ', medicina.issubset(especialidade)) # False
# Se todos os elementos do 1º conjunto também estão presentes no 2º conjunto retorna True

# issuperset() → Retorna se o conjunto "maior" contém todos os elementos do conjunto "menor"
print('especialidade é o conjunto que envolve todos os elementos do conjunto medicina? →', especialidade.issuperset(medicina)) # False
print('medicina é o conjunto que envolve todos os elementos do conjunto especialidade? →', medicina.issuperset(especialidade)) # True