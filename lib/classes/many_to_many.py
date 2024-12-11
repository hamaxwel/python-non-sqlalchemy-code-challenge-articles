class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Author name must be a non-empty string.")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        # Create a new Article instance and associate it with the author and magazine
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Magazine name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Category must be a non-empty string.")
        self._name = name
        self._category = category
        self._articles = []
        self.__class__.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors = {}
        for article in self._articles:
            authors[article.author] = authors.get(article.author, 0) + 1
        return [author for author, count in authors.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        if not cls.all_magazines:
            return None
        return max(cls.all_magazines, key=lambda mag: len(mag.articles()))


class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters.")
        self._author = author
        self._magazine = magazine
        self._title = title

        # Adding the article to the author's and magazine's records
        self._author._articles.append(self)
        self._magazine._articles.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        self._magazine = new_magazine


# Example usage
# Creating Author and Magazine instances
author1 = Author("John Doe")
magazine1 = Magazine("Tech Today", "Technology")
magazine2 = Magazine("Health Weekly", "Health")

# Adding articles to the author and magazines
article1 = author1.add_article(magazine1, "The Future of AI")
article2 = author1.add_article(magazine1, "Quantum Computing Basics")
article3 = author1.add_article(magazine2, "New Health Trends")

# Print Author's articles
print(f"Articles by {author1.name}:")
for article in author1.articles():
    print(f"- {article.title} in {article.magazine.name}")

# Print Author's topic areas
print(f"\nTopic Areas by {author1.name}: {author1.topic_areas()}")

# Print Magazine's contributors
print(f"\nContributors to {magazine1.name}:")
for contributor in magazine1.contributors():
    print(f"- {contributor.name}")

# Print Magazine's article titles
print(f"\nArticle titles in {magazine1.name}:")
for title in magazine1.article_titles():
    print(f"- {title}")

# Print Magazine's contributing authors
print(f"\nContributing authors to {magazine1.name} (more than 2 articles):")
for author in magazine1.contributing_authors():
    print(f"- {author.name}")

# Print the top publisher based on the number of articles
top_publisher = Magazine.top_publisher()
print(f"\nTop Publisher: {top_publisher.name} with {len(top_publisher.articles())} articles")


