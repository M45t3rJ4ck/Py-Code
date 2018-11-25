# towers of hanoi moves

def hanoi (n, source, dest):
   if n > 0:
      hanoi (n-1, source, 6-source-dest)
      print("Move disc from", source, "to", dest)
      hanoi (n-1, 6-source-dest, dest)
   
hanoi (9, 1, 3)
