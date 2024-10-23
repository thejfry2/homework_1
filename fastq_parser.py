
#this function Reads a FastQ file and converts sequences into lists of bases stored in a dictionary.
""""test cases are stored in test.fa as seq 98 and 99, they should read 
['C', 'U', 'A', 'U', 'G', 'U'] and ['error', 'error', 'error', 'G', 'error'] respectivly"""


seqNum = ""
def read_fastq_file(file_path):

    sequences_dict = {}  # Dictionary to store sequences with sequence IDs as keys

    with open(file_path, "r") as file:
        while True:
            # Read the lines
            seq_id_line = file.readline().strip()
            sequence_line = file.readline().strip()
            plus_line = file.readline().strip()
            quality_line = file.readline().strip()

            # breaks loop at the end of the file
            if not seq_id_line:
                break
            
            # Extract sequence ID (remove '@' from the start)
            seq_id = seq_id_line[1:]

            # Convert the sequence line into a list of bases
            bases = list(sequence_line)

            # Store the sequence in the dictionary
            sequences_dict[seq_id] = bases

    return sequences_dict
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


file_path = "test.fq"
sequences_dict = read_fastq_file(file_path)
transcribed_sequence = transcribe_sequence(seqNum, sequences_dict)
print(transcribed_sequence)
