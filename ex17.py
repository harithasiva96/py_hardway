from sys import argv
from os.path import exists

script, from_file, to_file = argv
   # Passing arguments to the corresponding variables.
print(f"Copying from {from_file} to {to_file}")
  # Assigning the opened file to a variable
in_file = open(from_file)
  #Assigning the read file in to another variable.
indata = in_file.read()
  #Give the length of the file in bytes
print(f"The input file is {len(indata)} bytes long")
  # 'exists' check whether the file exists or not and return 'yes' or 'no'.
print(f"Does the output file exist? {exists(to_file)}")
print(f"Ready, hit RETURN to continue, CTRL-C to abort.")
input()
  # Write on the required file.
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()