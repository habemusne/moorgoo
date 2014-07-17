class BooksController < ApplicationController
  def index
    @books = Book.similar_search( params[:bookSearchType], params[:search])
    if @books.empty?
      flash[:alert] = 'No books found'
      redirect_to root_path
    end
  end

  def show
    @book ||= Book.find(params[:id])
  end


end
