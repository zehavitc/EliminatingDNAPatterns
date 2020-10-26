

class PatternsReader:

    #TODO - add ReadFromFile, ReadFromGui
    def read_from_file(self, file_path):
        """
        file path, content expected is comma seperated patterns (IUPAC code is supported)
        :return:
        """
        res = []
        #TODO - add input validation
        with open(file_path, 'r') as file:
            for line in file.readlines():
                patterns = line.strip().split(',')  # using rstrip to remove the \n
                res.extend(patterns)
        return res

