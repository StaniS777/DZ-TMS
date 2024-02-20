class Book:
    @staticmethod
    def get_id_generator():
        i = 1
        while True:
            yield i
            i += 1

    id_gen = get_id_generator()
    
    def __init__(self, name: str) -> None:
        self.id = next(self.id_gen)
        self.name = name

    def __str__(self) -> str:
        return f"Book ({self.id}) {self.name}"

books = [
    Book(name) for name in ("Faust", "Mumu", "War and Piece")
]
