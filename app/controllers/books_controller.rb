class BooksController < ApplicationController
  def index
    @books = Book.where(:isbn => params[:search])
    if @books.nil?
      flash[:alert] = 'No books found'
      redirect_to root_path
    end
  end


end
