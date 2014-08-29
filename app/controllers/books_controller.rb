require 'open-uri'
class BooksController < ApplicationController

  def index
    params[:search] = Book.convertISBN(params[:search])
    @books = Book.similar_search(params[:search])

    if @books.empty?
      flash[:alert] = 'No books found'
      redirect_to @school
    end
    if @books.count == 1
      redirect_to school_book_path(@school.name, @books.first)
    end
    get_bookprices @books
  end

  def show
    @book ||= Book.where(:id=>params[:id])
    get_bookprices @book
  end

  def new
    @book = Book.new
  end

  def create
    params[:book][:isbn] = Book.convertISBN(params[:book][:isbn])

    if auto_mode?
      @book = Book.processISBN(params[:book][:isbn])
      if @book.nil?
        flash[:alert] = "Sorry, this ISBN is unrecognized. Please enter book info manually."
        redirect_to new_school_book_path
      else
        @book.update_attribute(:course, params[:book][:course].delete(' ').downcase)
        redirect_to new_school_bookprice_path(:book_id => @book.id)
      end
    else
      @book = Book.create(book_params)
      redirect_to new_school_bookprice_path(:book_id => @book.id)
    end
  end

  private
    def auto_mode?
      params[:save_mode] == "auto"
    end

    def book_params
      params.require(:book).permit(:author, :course, :title, :isbn)
    end

    def processISBN
      book = Book.find_by(:isbn => params[:book][:isbn]) || fetch_book(params[:book][:isbn])
    end

    def convertISBN(isbn)
      if isbn.length == 10
        isbn_13 = "978" + isbn.from(0).to(8) + ((10 - (9 + 3*7 + 8 + 3*(isbn.at(0).to_i) + isbn.at(1).to_i + 3*(isbn.at(2).to_i) + isbn.at(3).to_i + 3*(isbn.at(4).to_i) + isbn.at(5).to_i + 3*(isbn.at(6).to_i) + isbn.at(7).to_i + 3*(isbn.at(8).to_i)) % 10) % 10).to_s
      else
        if isbn == ""
          isbn_13 = "a"
        else
          isbn_13 = isbn
        end
      end
      return isbn_13
    end

    def fetch_book(isbn)
      url = "https://www.googleapis.com/books/v1/volumes?q=isbn:#{isbn}"
      result = JSON.load(open(url).read)
      if result["totalItems"] == 0
        nil
      else
        begin
          book = Book.new(
            :title => result["items"][0]["volumeInfo"]["title"],
            :isbn => isbn,
            :author => result["items"][0]["volumeInfo"]["authors"][0] || " ",
            :pic_url => result["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]
          )
        rescue
          nil
        end
      end
    end

    def get_bookprices(book_arr)
      @prices = {}
      book_arr.each do |b|
        @prices[b.id] = b.bookprices.valid
      end
    end

end