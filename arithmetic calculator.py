def arithmetic_arranger(problems, solve=False):

  #return error if more than 5 problems are given
  if len(problems) > 5:
    return 'Error: Too many problems.'

  frow = ''
  srow = ''
  sep = ''
  tot = ''
  for c, i in enumerate(problems):
    i = i.split(' ')
    op1 = i[0]
    sign = i[1]
    op2 = i[2]

    #return error if operator not + or -
    if sign not in '+-':
      return "Error: Operator must be '+' or '-'."

    #return error if numbers more than 4 digits
    if len(op1) > 4 or len(op2) > 4:
      return 'Error: Numbers cannot be more than four digits.'

    #return error if not only digits
    try:
      op1 = int(op1)
      op2 = int(op2)
    except: return 'Error: Numbers must only contain digits.'
    op1 = str(op1)
    op2 = str(op2)
    
    #calculating the total
    if sign == '+':
        total = str(int(op1) + int(op2))
    if sign == '-':
        total = str(int(op1) - int(op2))
        
    #creating the rows of the output
    if len(op1) > len(op2):
      width = ' '*(2 + len(op1))
    if len(op2) > len(op1):
      width = ' '*(2 + len(op2))
    if len(op2) == len(op1):
      width = ' '*(2 + len(op2))
    frow += ' '*(len(width) - len(op1)) + op1 + ' '*4
    srow += sign + ' '*(len(width) - (1 + len(op2))) + op2 + ' '*4
    sep += '-'*len(width) + ' '*4
    tot += ' '*(len(width) - len(total)) + total + ' '*4

  #removing excess whitespace at the end of each row
  frow = frow.rstrip(' ') 
  srow = srow.rstrip(' ') 
  sep = sep.rstrip(' ')
  tot = tot.rstrip(' ')

  #if parameter True is given, return also the solution, else don't
  if solve:
    problem = [frow, srow, sep, tot]
  else: 
    problem = [frow, srow, sep]
  
  #join the rows with the newline character
  arranged_problems = '\n'.join(problem)

  #return the result
  return arranged_problems    