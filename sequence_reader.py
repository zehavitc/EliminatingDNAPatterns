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
            return raw_seq.strip()
        return None
