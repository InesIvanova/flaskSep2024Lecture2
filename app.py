from decouple import config
from flask import Flask, request
from flask_migrate import Migrate
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (f"postgresql://"
                                         f"{config('DB_USER')}:"
                                         f"{config('DB_PASS')}@"
                                         f"{config('DB_HOST')}:"
                                         f"{config('DB_PORT')}/"
                                         f"{config('DB_NAME')}")


class Base(DeclarativeBase):
  pass


db = SQLAlchemy(app, model_class=Base)
api = Api(app)
migrate = Migrate(app, db)


class BookModel(db.Model):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    author: Mapped[str] = mapped_column(String(50), nullable=False)
    reader_id: Mapped[int] = mapped_column(ForeignKey("readers.id"), nullable=True)

    reader: Mapped['ReaderModel'] = relationship(back_populates='books')

    def __repr__(self):
        return f"<{self.pk}> {self.title} from {self.author}"

    def as_dict(self):
        return {"id": self.id, "title": self.title, "author": self.author}


class ReaderModel(db.Model):
    __tablename__ = 'readers'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    books: Mapped[list['BookModel']] = relationship(back_populates='reader')

class BooksResource(Resource):
    def get(self):
        # books = BookModel.query.all() # version 2
        books = db.session.execute(db.select(BookModel)).scalars() # version 3
        return [b.as_dict() for b in books]

    def post(self):
        data = request.get_json()
        book = BookModel(**data)
        db.session.add(book)
        db.session.commit()
        return book.as_dict(), 201


class BookResource(Resource):
    def get(self):
        # TODO homework
        pass

    def put(self):
        # TODO homework
        pass

    def delete(self):
        # TODO homework
        pass


api.add_resource(BooksResource, "/books")
# TODO Homework - add the Bookresource to respective binding url

