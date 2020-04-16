def checkVPS(ps):
   stack = []
   for i in range(len(ps)):
      if ps[0] == '(':
         stack.append(ps[0])      
      elif ps[0] == ')' and stack:
         del stack[-1]
      else:
         return "NO"

      del ps[0]

   if not stack:#empty
      return "YES"
   else:
      return "NO"


N = int(input())

for i in range(N):
   ps = list(input())
   print(checkVPS(ps))