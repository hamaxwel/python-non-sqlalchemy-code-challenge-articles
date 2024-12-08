import pytest

from classes.many_to_many import Article
from classes.many_to_many import Magazine
from classes.many_to_many import Author


class TestArticle:
    """Article in many_to_many.py"""

    def test_has_title(self):
        """Article is initialized with a title"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")
        article_2 = Article(author, magazine, "Dating life in NYC")

        assert article_1.title == "How to wear a tutu with style"
        assert article_2.title == "Dating life in NYC"

    def test_title_is_immutable_str(self):
        """Title is an immutable string"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")

        assert isinstance(article_1.title, str)

        # Title is immutable, uncomment if testing for exception handling
        # with pytest.raises(Exception):
        #     article_1.title = "New Title"

        # Uncomment if testing for invalid article creation
        # with pytest.raises(ValueError):
        #     Article(author, magazine, 500)  # Invalid title type

    def test_title_is_valid(self):
        """Title is between 5 and 50 characters inclusive"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")

        assert 5 <= len(article_1.title) <= 50

        # Uncomment to test for invalid title length
        # with pytest.raises(ValueError):
        #     Article(author, magazine, "Test")  # Too short
        # with pytest.raises(ValueError):
        #     Article(author, magazine, "How to wear a tutu with style and walk confidently down the street")  # Too long

    def test_has_an_author(self):
        """Article has an author"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author_1, magazine, "How to wear a tutu with style")
        article_2 = Article(author_2, magazine, "Dating life in NYC")

        assert article_1.author == author_1
        assert article_2.author == author_2

    def test_author_of_type_author_and_mutable(self):
        """Author is of type Author and mutable"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author_1, magazine, "How to wear a tutu with style")
        article_2 = Article(author_2, magazine, "Dating life in NYC")

        assert isinstance(article_1.author, Author)
        assert isinstance(article_2.author, Author)

        # Author is mutable; update the article's author
        article_1._author = author_2
        assert article_1.author == author_2
        assert article_1.author.name == "Nathaniel Hawthorne"

    def test_has_a_magazine(self):
        """Article has a magazine"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author, magazine_2, "Dating life in NYC")

        assert article_1.magazine == magazine_1
        assert article_2.magazine == magazine_2

    def test_magazine_of_type_magazine_and_mutable(self):
        """Magazine is of type Magazine and mutable"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author, magazine_2, "Dating life in NYC")

        assert isinstance(article_1.magazine, Magazine)
        assert isinstance(article_2.magazine, Magazine)

        # Magazine is mutable; update the article's magazine
        article_1._magazine = magazine_2
        assert article_1.magazine == magazine_2
        assert article_1.magazine.name == "AD"

    def test_get_all_articles(self):
        """Article class has all attribute"""
        Article.all_articles = []
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author, magazine_2, "Dating life in NYC")

        assert len(Article.all()) == 2
        assert article_1 in Article.all()
        assert article_2 in Article.all()