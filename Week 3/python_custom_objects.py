class MyFirstClass:
    print("Who wrote this?")
    index = "Author-Book"

    def hand_List(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book)


whodunnit = MyFirstClass()
whodunnit.hand_List("Sun Tzu", "The Art of War")
