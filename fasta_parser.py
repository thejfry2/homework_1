
# you have to be in the same directory as the test files for the program to acces the files it needs
#this is a function for reading the fasta file and turning the sequences into dictonary entrys
#test cases are stored in test.fa as seq 98 and 99, they should read ['C', 'U', 'A', 'U', 'G', 'U'] and 
seqNum = ""
transcript = []
sequences = {}
def read_fasta_file(file_path):
    """Reads a FASTA file and makes a dictionary of sequences, 
    with sequence IDs as keys and lists of bases as values."""
    sequences = {}
    current_seq_id = None
    
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                # New sequence header, get the sequence ID (without the '>')
                current_seq_id = line[1:]
                # makes an empty list for this sequence ID
                sequences[current_seq_id] = []
            else:
                # Append the sequence bases to the current sequence ID's list
                sequences[current_seq_id].extend(line)
    
    return sequences
# this is the funtion for converting the dictonary of sequences
def transcribe_sequence(seqNum, sequences_dict):
  seqNum = input("please input sequence number for transcription: ")
  seqNumStr = "seq"+str(seqNum)
  #does the transcription base by base by making a new list and appending to it
  bases = sequences_dict[seqNumStr]
  print("here is " + seqNumStr + " after transcription")
  transcript = []
  for base in bases:
    if base == "A":
      transcript.append("U")
    elif base == "T":
      transcript.append("A")
    elif base == "G":
      transcript.append("C")
    elif base == "C":
      transcript.append("G")
    else:
      transcript.append("error")
  print(transcript)
  while True: 
    rev = input("would you like the reverse transcript?(Y/N)")
    if rev == "Y":
      print("ok here is the reverse")
      transcript.reverse()
      print(transcript)
      break  
    if rev == "N":
      break  
    else:
      #if they put somthing else this will ask again
      print("Invalid input. Please enter Y or N. This is case sensitive")
      anotherone = input("would you like to transcribe another sequence?(Y/N)")
    if anotherone == "Y":
      print("ok")
    if anotherone == "N":
      print("ok, goodbye!")
      break


file_path = "test.fa"
sequences_dict = read_fasta_file(file_path)
print("fasta read")
transcribed_sequence = transcribe_sequence(seqNum, sequences_dict)
print(transcribed_sequence)

#testcaseP = ["G","A","T","C","A"] # postive test case
#testcaseN = ["U", "A", 'X', "B"] # negative test case
# testcase = input("would you like to see the positive and negative test cases for this code?(Y/N)")
# transcript = []
# if testcase == "Y": 
#     for base in testcaseP: #I should have made a funtion out of this but dont want to go back and change it
#         if base == "A":
#             transcript.append("U")
#         elif base == "T":
#              transcript.append("A")
#         elif base == "G":
#              transcript.append("C")
#         elif base == "C":
#              transcript.append("G")
#         else:
#              transcript.append("error")
# print("this is the postive test case, it should output C,U,A,G,U")
# print(transcript)
# transcript = []
# if testcase == "Y": 
#     for base in testcaseN: #I should have made a funtion out of this but dont want to go back and change it
#         if base == "A":
#             transcript.append("U")
#         elif base == "T":
#             transcript.append("A")
#         elif base == "G":
#             transcript.append("C")
#         elif base == "C":
#             transcript.append("G")
#         else:
#             transcript.append("error")
# print("this is the negative test case, it should output error,U,error,error")
# print(transcript)
# #I did not make postive and negative test cases for the reverse, because its a built in funtion.


# transcribed_sequence = transcribe_sequence(seqNum, sequences_dict)
# print(transcribed_sequence)