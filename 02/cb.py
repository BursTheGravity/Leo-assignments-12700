def string_times(str, n):
  return str*n

def front_times(str, n):
  ans = ""
  if len(str) < 3:
    ans = str*n
  else:
    ans = str[0:3]*n
  return ans

def string_bits(str):
  i = 0
  ans = ""
  for i in range (len(str)):
    if i % 2 == 0:
      ans += str[i:i+1]
  return ans

def lone_sum(a, b, c):
  ans = 0
  if a != b and a != c:
    ans += a
  if b != a and b != c:
    ans += b
  if c != a and c != b:
    ans += c
  return ans

def string_splosion(str):
  ans = ""
  for i in range (len(str)):
    ans += str[0:i+1]
  return ans

def cigar_party(cigars, is_weekend):
  if cigars >= 40:
    if is_weekend:
      return True
    elif cigars <= 60:
      return True
  return False

def caught_speeding(speed, is_birthday):
  if is_birthday:
    speed -= 5
  if speed <= 60: return 0
  elif speed > 60 and speed <= 80: return 1
  else: return 2

print ("Testing string_times('Oh Boy!', 2): ")
print (string_times('Oh Boy!', 2))
print ("Testing front_times('Ab', 4): ")
print (front_times('Ab', 4))
print ("Testing string_bits('Heeololeo'): ")
print (string_bits('Heeololeo'))
print ("Testing lone_sum(9, 2, 2): ")
print (lone_sum(9, 2, 2))
print ("Testing string_splosion('Code'): ")
print (string_splosion('Code'))
print ("Testing cigar_party(61, False): ")
print (cigar_party(61, False))
print ("Testing caught_speeding(85, True): ")
print (caught_speeding(85, True))
