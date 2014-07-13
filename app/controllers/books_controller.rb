class BooksController < ApplicationController
  def index
    @books = Book.where(params[:bookSearchType].to_sym => params[:search])
    if @books.empty?
      flash[:alert] = 'No books found'
      redirect_to root_path
    end
  end

  def show
    @book ||= Book.find(params[:id])
  end


end
