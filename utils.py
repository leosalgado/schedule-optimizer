
def print_population(pop, subjects):
  import sys
  for k in range (10):
    print_days()
    for j in range(6):
      column_values = []
      for i in range(5):
        column_values.append(subjects[pop[k][i][j]])
      print(" ".join(f"{value:20}" for value in column_values))
    print()

def print_days():
  days = ['SEGUNDA', 'TERCA', 'QUARTA', 'QUINTA', 'SEXTA']
  print(" ".join(f'{day:20}' for day in days))
  print('-'*100)

def print_scores(score):
  print('Mio = ', score[0][1])