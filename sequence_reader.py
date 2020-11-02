class SequenceReader:

    #TODO - add ReadFromFile, ReadFromGui
    def read_from_file(self, file_path):
        """
        file_path, expected content is a DNA sequence.
        UpperCase letters indicate positions that are not allowed to be changed.
        Note that IUPAC is supported
        :return:
        """
        #TODO - add input validation
        with open(file_path, 'r') as file:
            raw_seq = file.readlines()
            for line in raw_seq:
                if line.isspace():
                    continue
                return line.strip() #uses the first line that is not a space
        return None
