import unittest
from book import Book
from book_manager import BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.book_manager = BookManager()

    def test_add_book(self):
        """Test menambahkan buku"""
        book = Book("Pemrograman", "Andi", 2020)
        self.book_manager.add_book(book)
        self.assertEqual(1, self.book_manager.get_book_count())

    def test_remove_existing_book(self):
        """Test menghapus buku yang ada"""
        book = Book("Basis Data 1", "Erlangga", 2021)
        self.book_manager.add_book(book)

        removed = self.book_manager.remove_book("Basis Data 1")
        self.assertTrue(removed)
        self.assertEqual(0, self.book_manager.get_book_count())

    # Lengkapi Unit Test di bawah untuk buku yang memang tidak terdapat pada list
    def test_remove_non_existing_book(self):
        """Test menghapus buku yang tidak ada"""
        pass

    # Lengkapi Unit Test di bawah untuk mencari buku berdasarkan penulis
    def test_find_books_by_author(self):
        """Test mencari buku berdasarkan author"""
        pass

    # Lengkapi Unit Test di bawah untuk seluruh buku yang ada di dalam list
    def test_get_all_books(self):
        """Test mendapatkan semua buku"""
        pass


if __name__ == '__main__':
    unittest.main()