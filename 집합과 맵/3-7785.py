# N = int(input())
# pe = {}
#
# for _ in range(N):
#   p, c = input().split()
#
#   if c == 'enter':
#     pe[p] = 'enter'
#   else:
#     if pe[p]:
#       del pe[p]
#
# for people in sorted(pe, reverse=True):
#   print(people)

# part 2
import sys

pe = {}

for _ in range(int(sys.stdin.readline())):
  p, c = sys.stdin.readline().rstrip().split()

  if c == 'enter':
    pe[p] = 'enter'
  else:
    if pe[p]:
      del pe[p]

for people in sorted(pe, reverse=True):
  print(people)