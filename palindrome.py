def PalindromeTwo(strParam):
  fwd = ''.join(x for x in strParam if x.isalnum())
  rev = ''.join(reversed(fwd))
  #print(rev)
  #print(fwd)
  if (fwd.lower() == rev.lower()):
    return "true"
  return "false"

# keep this function call here
print PalindromeTwo(raw_input())
