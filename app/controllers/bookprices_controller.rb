require 'open-uri'
class BookpricesController < ApplicationController
  before_filter :check_user, :only=>[:index, :update]

  def index
    @bookprices = current_user.bookprices.where(:status=>params[:status].to_i).order(updated_at: :desc)
    @sold = params[:status]
  end

  def new
    @bookprice = Bookprice.new
  end

  def update
    @bookprice = Bookprice.find(params[:id])
    @bookprice.update_attribute(:status, params[:bookprice][:status].to_i)
    redirect_to bookprices_path(:status=>@bookprice.status)
  end

  def create
    @book = processISBN
    if @book.nil?
      flash[:alert] = "Invalid ISBN!"
      redirect_to new_bookprice_path
    else
      if current_user
        @bookprice = current_user.bookprices.create(bookprice_params)
        @bookprice.update_attribute(:book_id, @book.id)
        redirect_to @book
      else
        @bookprice = Bookprice.create(bookprice_params)
        @bookprice.update_attribute(:book_id, @book.id)
        cookies.signed[:tempPrice] = {:value => @bookprice.id, :expires => 1.hour.from_now}
        redirect_to new_user_session_path
      end
    end
  end


  private
    def check_user
      redirect_to new_user_session_path unless user_signed_in?
    end

    def bookprice_params
      params.require(:bookprice).permit(:isbn, :price, :condition, :contact)
    end

    def processISBN
      book = Book.find_by(:isbn => params[:bookprice][:isbn]) || fetch_book(params[:bookprice][:isbn])
    end

    def fetch_book(isbn)
      url = "https://www.googleapis.com/books/v1/volumes?q=isbn:#{isbn}"
      result = JSON.load(open(url).read)
      if result["totalItems"] == 0
        nil
      else
        book = Book.create(
          :title => result["items"][0]["volumeInfo"]["title"],
          :isbn => isbn,
          :author => result["items"][0]["volumeInfo"]["authors"][0] || " ",
          :pic_url => result["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]
          )
      end
    end
end
