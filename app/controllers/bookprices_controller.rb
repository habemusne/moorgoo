require 'open-uri'
class BookpricesController < ApplicationController
  before_filter :check_user, :only=>[:index, :update]
  before_filter :check_book, :only=>:new

  def index
    @bookprices = current_user.bookprices.where(:status=>params[:status].to_i).order(updated_at: :desc)
    @sold = params[:status]
  end

  def new
    @bookprice = Bookprice.new
    @book_id = params[:book_id].to_i
    @book = Book.find(@book_id)
    # @prices = @book.bookprices
  end

  def update
    @bookprice = Bookprice.find(params[:id])
    @bookprice.update_attribute(:status, params[:bookprice][:status].to_i)
    redirect_to school_bookprices_path(:status=>@bookprice.status)
  end

  def create
    if current_user
      @bookprice = current_user.bookprices.create(bookprice_params)
      redirect_to school_book_path(@school.name, @bookprice.book)
    else
      @bookprice = Bookprice.create(bookprice_params)
      cookies.signed[:tempPrice] = {:value => @bookprice.id, :expires => 1.hour.from_now}
      flash[:notice] = "You are almost there! Just sign in or sign up, and we'll do the rest!"
      redirect_to new_user_session_path
    end
  end


  private
    def check_user
      redirect_to new_user_session_path unless user_signed_in?
    end

    def check_book
      redirect_to new_school_book_path unless params[:book_id]
    end

    def bookprice_params
      params.require(:bookprice).permit(:book_id, :price, :condition, :contact)
    end

end
