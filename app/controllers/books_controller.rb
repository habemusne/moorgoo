require 'open-uri'
class BooksController < ApplicationController

  def index
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
    if auto_mode?
      @book = processISBN
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
