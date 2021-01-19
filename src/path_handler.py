import os

class PathHandler:
    def __init__(self):
        self.base_path = self.set_base_path(os.path.dirname(os.path.realpath(__file__)))
        self.content_path = self.base_path + '/content'
    
    def set_base_path(self, path):
        """
        Riceve in ingresso la posizione del file e restituisce la cartella di root
        """
        full_path = path.split('/')
        return '/'.join(full_path[:-1])

    def file_in_content(self):
        """
        Generatore del nome dei file PDF all'interno di {self.content_path}
        vengono generati full_path 
        -- fails silently
        """
        for filename in os.listdir(self.content_path):
            if '.pdf' not in filename:
                continue
            full_name = os.path.join(self.content_path, filename)
            try:
                yield full_name
            except OSError:
                pass

    

if __name__ == '__main__':
    ph = PathHandler()
    print(ph.base_path, ph.content_path)

    for file in ph.file_in_content():
        print(file)
