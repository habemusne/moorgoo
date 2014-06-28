class BookpricesController < ApplicationController
  def new
    @bookprice = Bookprice.new
  end

  def create
    @book = processISBN
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


  private
    def bookprice_params
      params.require(:bookprice).permit(:isbn, :price, :condition, :contact)
    end

    def processISBN
      book = Book.find_by(:isbn => params[:bookprice][:isbn]) or fetch_book
      book
    end

    def fetch_book
    end
end
